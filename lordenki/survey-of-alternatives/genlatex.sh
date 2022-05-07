#!/usr/bin/env zsh
(
hyperlinkpackage="[breaklinks]{hyperref}" 	# for ebook use only -- does not reliably break long links, so KDP will reject for print books
hyperlinkpackage="[hypens]{url}"						# for print book use only -- does not make links clickable

echo '\\documentclass[500paper]{kdp} % 5x8 inches
\\usepackage{geometry}
\\usepackage{layout}
\\usepackage{amsmath} % Advanced math typesetting
\\usepackage[utf8]{inputenc} % Unicode support (Umlauts etc.)
\\usepackage'"$hyperlinkpackage"'
\\usepackage{graphicx} % Add pictures to your document
\\usepackage{svg}
\\usepackage{rotating}
\\usepackage{listings} % Source code formatting and highlighting
\\usepackage{fancyhdr}
\\usepackage{marginnote}
\\renewcommand{\\marginfont}{\\tiny}
\\usepackage{imakeidx}
\\usepackage[backend=biber,
style=alphabetic,
sorting=ynt
]{biblatex}
\\usepackage{xurl}
\\usepackage[toc]{glossaries}'
echo '\\makeglossaries
\\glsnoexpandfields
\\makeindex[intoc]
\\addbibresource{bibliography.bib}'
cat gloss.txt | sed 's/\(^.*\): \(.*\)$/\\newglossaryentry{\1}{name={\1},description={\2}}/'
echo '\\begin{document}
\\frontmatter
\\author{John Ohno}\\title{Interfaces and Systems: A Survey of Alternatives}
\\def\\secondpage{\\clearpage\\null\\vfill
\\pagestyle{empty}
\\begin{minipage}[b]{0.9\\textwidth}
\\footnotesize\\raggedright
\\setlength{\\parskip}{0.5\\baselineskip}
Copyright \\copyright 2018--\\the\\year\\ John Ohno\\par
All rites reversed
\\end{minipage}
\\vspace*{2\\baselineskip}
\\cleardoublepage
\\rfoot{\\thepage}}
\\maketitle{}\\newpage{}\\secondpage
\\newpage{}
\\tableofcontents{}
\\listoffigures
\\listoftables
\\mainmatter'
echo '\\begin{sidewaysfigure}
	\\includesvg[width=8.5in]{gui_evolution}
\\caption{The evolution of user interfaces, showing the flow of ideas between related projects}
\\end{sidewaysfigure}'
)> book.latex
for i in intro.txt chapter*.txt ; do 
	pandoc -f markdown -t latex $i -o $i.latex
	sed -i 's/\\section{/\\chapter{/;s/\\subsection{/\\section{/' $i.latex
	sed -i 's/\\hypertarget{.*$//;s/\(\\label{.*}\)}/\1/' $i.latex
	sed -i 's/\(Big and Small Computing\)/\\textit{\1}\\cite{bigandsmallcomputing}/' $i.latex
	cut -d: -f 1 < gloss.txt | grep . | while read x ; do
		sed -i "s/$x/\\\\index{$x}\\\\gls{$x}/g" $i.latex
	done
	cut -d: -f 1 < gloss.txt | tr 'A-Z' 'a-z' | grep . | while read x ; do
		sed -i "s/$x/\\\\index{$x}\\\\gls{$x}/g" $i.latex
	done
	cat $i.latex >> book.latex
done
echo '\\chapter{Appendix A: Resources}' >> book.latex
cat ../resources-survey-of-alternatives.html | iconv -t "utf-8//IGNORE" | sed '
	s/<li>/\n<li>/g;
	s/<\/ul>\(.*\)<ul>$/<\/ul><h1>\1<\/h1><ul>/;
	s/href="\([^"]*\)">\([^>]*\)>/href="\1">\2><br><br>\&lt;<pre>\1<\/pre>\&gt;/' > resources.html
pandoc -f html -t latex resources.html | sed 's/\\hypertarget{.*$//;s/\(\\label{.*}\)}/\1/' > resources.latex
cat resources.latex >> book.latex
echo '\\chapter{Appendix B: Further Reading}' >> book.latex
cat further_reading.txt >> book.latex
echo '\\printglossaries' >> book.latex
echo '\\glsall' >> book.latex
echo '\\printbibliography' >> book.latex
echo '\\printindex' >> book.latex
echo '\\end{document}' >> book.latex
echo "R" | pdflatex book.latex 
biber book
echo "R" | pdflatex book.latex 
makeglossaries book
echo "R" | pdflatex book.latex 
biber book
echo "R" | pdflatex book.latex 
rm -f *.{bbl,blg,glo,idx,ilg,ind,ist,log,run.xml,toc,aux,bcf,glg,gls,lof,lot}
rm -f *.out
#rm -f *.latex
#xpdf book.pdf

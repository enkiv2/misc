#!/usr/bin/env zsh
(
cat prefix.latex
cat gloss.txt | sed 's/\(^.*\): \(.*\)$/\\newglossaryentry{\1}{name={\1},description={\2}}/'
echo '\\begin{document}'
cat frontmatter.latex
echo '\\mainmatter'
echo '\\begin{sidewaysfigure}
	\\includesvg[width=5in]{gui_evolution}
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
(
	echo '\\marginnote{The live version of this appendix is available from \\textless \\url{https://www.lord-enki.net/resources-survey-of-alternatives.html} \\textgreater}'
  first=""
	cat ../resources-survey-of-alternatives.txt | while read x ; do 
		if echo "$x" | grep -q '://' ; then
			echo "\\item"
			echo "  \\\\textless \\\\url{$x} \\\\textgreater"
		else 
      [ -z "$first" ] || echo "\\\\end{itemize}"
      first="no"
			echo "\\section{$x}"
			echo "\\\\begin{itemize}"
			echo "\\\\tightlist"
		fi
	done )> resources.latex
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

#!/usr/bin/env zsh

function genLatexMain() {
	echo '\\mainmatter'
	echo '\\begin{sidewaysfigure}
		\\includesvg[width=5in]{gui_evolution}
	\\caption{The evolution of user interfaces, showing the flow of ideas between related projects}
	\\end{sidewaysfigure}'

	echo "% Main body: chapters"
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
		cat $i.latex 
	done
}

function genLatexResources() {
	echo '\\marginnote{The live version of this appendix is available from \\textless \\url{https://www.lord-enki.net/resources-survey-of-alternatives.html} \\textgreater}'
	first=""
	cat ../resources-survey-of-alternatives.txt | while read x ; do 
		if echo "$x" | grep -q '://' ; then
			echo '\\item'
			echo '  \\textless \\url{'"$x"'} \\textgreater'
		else 
			[ -z "$first" ] || echo '\\end{itemize}'
			first="no"
			echo '\\section{'"$x"'}'
			echo '\\begin{itemize}'
			echo '\\tightlist'
		fi
	done 
}

function genLatexAppendices() {
	echo "% Appendices"
	echo '\\chapter{Appendix A: Resources}' 
	genLatexResources

	echo '\\chapter{Appendix B: Further Reading}'
	cat further_reading.txt
}

function genLatex() {
	cat prefix.latex
	cat gloss.txt | sed 's/\(^.*\): \(.*\)$/\\newglossaryentry{\1}{name={\1},description={\2}}/'

	echo '\\begin{document}'
	cat frontmatter.latex

	genLatexMain
	genLatexAppendices

	cat backmatter.latex
}

function genPDF() {
	echo "R" | pdflatex $1.latex 
	biber $1
	echo "R" | pdflatex $1.latex
	makeglossaries $1
	echo "R" | pdflatex $1.latex 
	biber $1
	echo "R" | pdflatex $1.latex 
}

function cleanup() {
	rm -f *.{bbl,blg,glo,idx,ilg,ind,ist,log,run.xml,toc,aux,bcf,glg,gls,lof,lot}
	rm -f *.out
	#rm -f *.txt.latex resources.latex book.latex
}

genLatex > book.latex
genPDF book
cleanup


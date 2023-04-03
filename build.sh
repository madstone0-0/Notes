#!/bin/bash

basedir=$(pwd)
# Calculus Notes
mkdir -p ./_Exported/Calc
cd ./_Raws/Calc || exit 1
for file in ./*.tex; do
	echo "$file"
	filename=$(basename "$file" .tex)
	pdflatex -output-directory="../../_Exported/Calc" "$file" >>"$basedir/latex.log"
done
cd "$basedir" || exit 1

echo "Cleaning Calc dir"
rm ./_Exported/Calc/*.aux ./_Exported/Calc/*.fls ./_Exported/Calc/*.toc ./_Exported/Calc/*.synctex.gz ./_Exported/Calc/*.fdb_latexmk ./_Exported/Calc/*.log

# Intro to Computing Info Systems Beyond Notes
mkdir -p "./_Exported/CompSci/Information Systems For Business and Beyond Notes"
for file in ./_Raws/CompSci/Information_Systems/*.md; do
	echo "$file"
	filename=$(basename "$file" .md)
	pandoc "$file" -o "./_Exported/CompSci/Information Systems For Business and Beyond Notes/$filename.pdf" --template=./Templates/eisvogel.tex --listings
done

# Intro to Computing Runestone Notes
mkdir -p "./_Exported/CompSci/Runestone Notes"
for file in ./_Raws/CompSci/Runestone/*.md; do
	echo "$file"
	filename=$(basename "$file" .md)
	pandoc "$file" -o "./_Exported/CompSci/Runestone Notes/$filename.pdf" --template=./Templates/eisvogel.tex --listings
done

# Personal Notes
# Intro to Machine Learning
mkdir -p "./_Exported/Personal/Intro To Machine Learning"
for file in ./_Raws/CompSci/Personal/Intro\ To\ Machine\ Learning/*.md; do
	echo "$file"
	filename=$(basename "$file" .md)
	pandoc "$file" -o "./_Exported/Personal/Intro To Machine Learning/$filename.pdf" --template=./Templates/eisvogel.tex --listings
done

# Algorithms
mkdir -p "./_Exported/Personal/Algorithms"
for file in ./_Raws/CompSci/Personal/Algorithms/*.md; do
	echo "$file"
	filename=$(basename "$file" .md)
	pandoc "$file" -o "./_Exported/Personal/Algorithms/$filename.pdf" --template=./Templates/eisvogel.tex --listings
done

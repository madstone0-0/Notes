#!/bin/bash

# Calculus Notes
mkdir -p ./_Exported/Calc
for file in ./_Raws/Calc/*.md; do
	echo "$file"
	filename=$(basename "$file" .md)
	pandoc "$file" -o "./_Exported/Calc/$filename.pdf" --template=./Templates/eisvogel.tex --listings
done

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

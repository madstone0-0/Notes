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

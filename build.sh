#!/bin/bash

basedir=$(pwd)
# Calculus Notes
mkdir -p ./_Exported/Calc
cd ./_Raws/Calc || exit 1
for file in ./*.tex; do
	echo "$file"
	filename=$(basename "$file" .tex)

	if hash latexmk &>/dev/null; then
		(
			latexmk -pdf -synctex=1 -interaction=nonstopmode -outdir="$basedir/_Exported/Calc" "$file" &>>"$basedir/latex.log"
			rm "$basedir/_Exported/Calc/$filename.aux" "$basedir/_Exported/Calc/$filename.fls" "$basedir/_Exported/Calc/$filename.toc" "$basedir/_Exported/Calc/$filename.synctex.gz" "$basedir/_Exported/Calc/$filename.fdb_latexmk" "$basedir/_Exported/Calc/$filename.log" &>/dev/null
		) &
	elif hash tectonic &>/dev/null; then
		(tectonic "$file" -o "$basedir/_Exported/Calc" &>>"$basedir/latex.log") &
	else
		echo "Cannot get latex compiler"
		exit 1
	fi
done
cd "$basedir" || exit 1

# Intro to Computing Info Systems Beyond Notes
mkdir -p "./_Exported/CompSci/Information Systems For Business and Beyond Notes"
for file in ./_Raws/CompSci/Information_Systems/*.md; do
	echo "$file"
	filename=$(basename "$file" .md)
	(pandoc --pdf-engine=tectonic "$file" -o "./_Exported/CompSci/Information Systems For Business and Beyond Notes/$filename.pdf" --template=./Templates/eisvogel.tex --listings) &
done

# Intro to Computing Runestone Notes
mkdir -p "./_Exported/CompSci/Runestone Notes"
for file in ./_Raws/CompSci/Runestone/*.md; do
	echo "$file"
	filename=$(basename "$file" .md)
	(pandoc --pdf-engine=tectonic "$file" -o "./_Exported/CompSci/Runestone Notes/$filename.pdf" --template=./Templates/eisvogel.tex --listings) &
done

# Personal Notes
# Intro to Machine Learning
mkdir -p "./_Exported/Personal/Intro To Machine Learning"
for file in ./_Raws/CompSci/Personal/Intro\ To\ Machine\ Learning/*.md; do
	echo "$file"
	filename=$(basename "$file" .md)
	(pandoc --pdf-engine=tectonic "$file" -o "./_Exported/Personal/Intro To Machine Learning/$filename.pdf" --template=./Templates/eisvogel.tex --listings) &
done

# Algorithms
mkdir -p "./_Exported/Personal/Algorithms"
for file in ./_Raws/CompSci/Personal/Algorithms/*.md; do
	echo "$file"
	filename=$(basename "$file" .md)
	(pandoc --pdf-engine=tectonic "$file" -o "./_Exported/Personal/Algorithms/$filename.pdf" --template=./Templates/eisvogel.tex --listings) &
done

# Fuck
mkdir -p "./_Exported/FuckDE"
for file in ./_Raws/FDE/*.md; do
	echo "$file"
	filename=$(basename "$file" .md)
	(pandoc --pdf-engine=tectonic "$file" -o "./_Exported/FuckDE/$filename.pdf" --template=./Templates/eisvogel.tex --listings) &
done

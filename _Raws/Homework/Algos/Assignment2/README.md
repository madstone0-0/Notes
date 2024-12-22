# StringMatch.py

## Usage
```
python3 StringMatch.py file|interactive
```

If run in `interactive` mode the program will prompt you for the text and pattern to search for and will output the result of the search. 
In `file` mode the program will look for and read `input.txt` and will find the pairs of input text and patterns to search for
and will output the result of each search to each line of the `output.txt` file.

# WordFind.py

## Usage

```
python3 WordFind.py
```

WordFind will look for and read the file `input_square.txt` and expects input in the following format:
```
Number of rows/columns n
WORD1 WORD2 ... WORDn # Space separated words
WORDn WORDn ... WORDn
Target words also space separated
```
And will output the found words in the word square in the file `found_words.txt` in the following format:
```
WORD1:  [i, j] Direction of the word either:
    - Horizontal Right
    - Horizontal Left
    - Vertical Down
    - Vertical Up
    - Diagonal Top Right
    - Diagonal Bottom Right
    - Diagonal Top Left
    - Diagonal Bottom Left
```

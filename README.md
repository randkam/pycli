# pdf-tools
tools for PDFs(merge, delete, extract, swap).

## Requirements
Before running any pdf tools, install `PyPDF2` via the following command:
```bash
pip3 install PyPDF2
```

## pdf merge
### Combines all PDFs in the `input/` dir and outputs `output/merged.pdf`
- Can be run via the following command: ```python main.py pdf merge -i input1.pdf input2.pdf -o output.pdf ``` where input and output files can be named accordingly
  

## Page swapper
### swaps pages in PDFs based on user selection
- Can be run via the following command: ```python main.py pdf swap -i input1.pdf -p 1 3 -o output.pdf``` where input and output files can be changed accordingly and the pages entered after p will be swapped.
- Pages should be sapced
- pages included will be swapped

- 
## Page Extractor
### Removes pages in PDFs based on user selection
- Can be run via the following command: ```python main.py pdf merge -i input.pdf -p (enter pages to keep) - output.pdf``` where input and output files can be changed accordingly and the pages entered after p wil be kept.
- Pages should be sapced
- pages included will be kept in output file 


## Page delete
### Removes pages in PDFs based on user selection
- Can be run via the following command: ```python main.py pdf merge -i input.pdf -p (enter pages to keep) - output.pdf``` where input and output files can be changed accordingly and the pages entered after p wil be kept.
- Pages should be sapced
- pages included will not be kept in output file

#File-tools
tools for files(DeleteFilesContainingString, Merge)
## file merge
### Combines all files in a given folder and outputs them merged together
- Can be run via the following command: ```python main.py file merge -f folder1 -o output.pdf ``` where folder and output file can be named accordingly
- make sure all files in folder are of same type
  

## Remove files including string
### removes all files in a given folder that include a given string
- Can be run via the following command: ```python main.py file swap -i input1.pdf -p 1 3 -o output.pdf``` where input and output files can be changed accordingly and the pages entered after p will be swapped.
- Pages should be sapced
- pages included will be swapped


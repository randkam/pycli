import argparse
import PdfTools
import folderTools
'''
pycli:
 - pdf
   - merge
   - pageswap
   - pagedelete
   - pagekeep
 - files
   - find
   - delete
   - contains
'''

# create the top-level parser
parser = argparse.ArgumentParser(prog='pyCLI')

subparsers1 = parser.add_subparsers(help='sub-command help')

# create the parser for the "a" command
pdfparser = subparsers1.add_parser('pdf', help='PDF Tools')

pdfsubparsers = pdfparser.add_subparsers()

pdf_mergeparser = pdfsubparsers.add_parser('merge', help='merge multiple pdfs')
pdf_mergeparser.add_argument('-i', '--input',
                             help='Input files',
                             required=True,
                             nargs='+')
pdf_mergeparser.add_argument('-o',
                             '--output',
                             help='Output file',
                             required=True)
pdf_mergeparser.set_defaults(func=PdfTools.mergePDFs)

pdf_pageswapparser = pdfsubparsers.add_parser('pageswap', help='swap 2 pages')
pdf_pageswapparser.add_argument('-i',
                                '--input',
                                help='Input file',
                                required=True)
pdf_pageswapparser.add_argument('-o',
                                '--output',
                                help='Output file',
                                required=True)
pdf_pageswapparser.add_argument('-p','--pages',help='pages to swap',required=True,nargs=2)
pdf_pageswapparser.set_defaults(func=PdfTools.swapPages)

pdf_pagedeleteparser = pdfsubparsers.add_parser('pagedelete',
                                                help='delete pages from pdf')
pdf_pagedeleteparser.add_argument(
    '-i',
    '--input',
    help='Input files',
    required=True,
)
pdf_pagedeleteparser.add_argument('-p',
                                  '--pages',
                                  help='Page to delete',
                                  required=True,
                                  nargs='+')
pdf_pagedeleteparser.add_argument('-o',
                                  '--output',
                                  help='Output file',
                                  required=True)
pdf_pagedeleteparser.set_defaults(func=PdfTools.removePages)

pdf_pageretainparser = pdfsubparsers.add_parser('pageretain',
                                                help='retain pages from pdf')
pdf_pageretainparser.add_argument(
    '-i',
    '--input',
    help='Input file',
    required=True,
)
pdf_pageretainparser.add_argument('-p',
                                  '--pages',
                                  help='Page to keep',
                                  required=True,
                                  nargs='+')
pdf_pageretainparser.add_argument('-o',
                                  '--output',
                                  help='Output file',
                                  required=True)
pdf_pageretainparser.set_defaults(func=PdfTools.keepPages)

# create the parser for the "b" command
folderParser = subparsers1.add_parser('file', help='b help')
folderSubparsers = folderParser.add_subparsers()

folderdeltype = folderSubparsers.add_parser('scandelete', help= 'delete files which include cetain words')
folderdeltype.add_argument('-f','--folder', help = 'input folder', required = True)
folderdeltype.add_argument('-w','--word', help= 'delete files inclding this word/character file(ex. b, txt,...etc)', required= True)
folderdeltype.set_defaults(func= folderTools.delType)

folderMergeTxt = folderSubparsers.add_parser('mergetxt', help = 'merge txt files in folder')
folderMergeTxt.add_argument('-f','--folder',help='input folder', required=True)
folderMergeTxt.add_argument('-o','--output',help='output file', required=True)
folderMergeTxt.set_defaults(func = folderTools.mergeTxt)


# args = parser.parse_args(['pdf', 'pagedelete','-i','bomba/Greek.pdf', '-p', '1', '-o', 's.pdf'])
args = parser.parse_args()


args.func(args)

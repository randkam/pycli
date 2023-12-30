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
pdf_mergeparser.set_defaults(func=PdfTools.mergePDF)

pdf_pageswapparser = pdfsubparsers.add_parser('pageswap', help='swap 2 pages')
pdf_pageswapparser.add_argument('-i',
                                '--input',
                                help='Input file',
                                required=True)
pdf_pageswapparser.add_argument('-o',
                                '--output',
                                help='Output file',
                                required=True)
pdf_pageswapparser.set_defaults(func=PdfTools.swap)

pdf_pagedeleteparser = pdfsubparsers.add_parser('pagedelete',
                                                help='delete pages from pdf')
pdf_pagedeleteparser.add_argument(
    '-i',
    '--input',
    help='Input files',
    required=True,
)
pdf_pagedeleteparser.add_argument('-p',
                                  '--page',
                                  help='Page to delete',
                                  required=True,
                                  nargs='+')
pdf_pagedeleteparser.add_argument('-o',
                                  '--output',
                                  help='Output file',
                                  required=True)
pdf_pagedeleteparser.set_defaults(func=PdfTools.removePage)

pdf_pageretainparser = pdfsubparsers.add_parser('pageretain',
                                                help='retain pages from pdf')
pdf_pageretainparser.add_argument(
    '-i',
    '--input',
    help='Input files',
    required=True,
)
pdf_pageretainparser.add_argument('-p',
                                  '--page',
                                  help='Page to keep',
                                  required=True,
                                  nargs='+')
pdf_pageretainparser.add_argument('-o',
                                  '--output',
                                  help='Output file',
                                  required=True)
pdf_pageretainparser.set_defaults(func=PdfTools.keepPage)

# create the parser for the "b" command
folderParser = subparsers1.add_parser('folder', help='b help')
folderSubparsers = folderParser.add_subparsers()
folderdelfile = folderSubparsers.add_parser('deletefile',help = 'delete files from folder')
folderdelfile.add_argument('-f','--folder',help = 'input folder',required = True)
folderdelfile.add_argument('-n','--name',help = 'name of file(s) to delete', required= True, nargs = '+')
folderdelfile.set_defaults(func= folderTools.delfile)

folderdeltype = folderSubparsers.add_parser('scandelete', help= 'delete files which include cetain words')
folderdeltype.add_argument('-f','folder', help = 'input folder', required = True)
folderdeltype.add_argument('-w','--word', help= 'delete files inclding this word/character file(ex. b, txt,...etc)', required= True)
folderdeltype.set_defaults(func= folderTools.delType)
args = parser.parse_args()


args.func(args)

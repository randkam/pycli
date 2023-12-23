import argparse

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

def merge_pdfs(args):
    print(args)

# create the top-level parser
parser = argparse.ArgumentParser(prog='pyCLI')

subparsers1 = parser.add_subparsers(help='sub-command help')

# create the parser for the "a" command
pdfparser = subparsers1.add_parser('pdf', help='PDF Tools')

pdfsubparsers = pdfparser.add_subparsers()

pdf_mergeparser = pdfsubparsers.add_parser('merge', help='merge multiple pdfs')
pdf_mergeparser.add_argument('-i', '--input', help='Input files', required=True, nargs='+')
pdf_mergeparser.add_argument('-o', '--output', help='Output file', required=True)
pdf_mergeparser.set_defaults(func=merge_pdfs)

pdf_pageswapparser = pdfsubparsers.add_parser('pageswap', help='swap 2 pages')

pdf_pagedeleteparser = pdfsubparsers.add_parser('pagedelete', help='delete pages from pdf')

pdf_pageretainparser = pdfsubparsers.add_parser('pageretain', help='retain pages from pdf')

# create the parser for the "b" command
parser_b = subparsers1.add_parser('files', help='b help')

args = parser.parse_args(['pdf', 'merge', '-i', 'a.pdf', 'b.pdf', 'g.pdf', '-o', 'c.pdf'])
args.func(args)
# args = parser.parse_args()

# print(args)


#https://docs.python.org/3/library/argparse.html#action
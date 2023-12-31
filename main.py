import argparse
from parsers.MainParser import createSubParsers

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
createSubParsers(parser)

# args = parser.parse_args(['pdf', 'pagedelete','-i','ww9.pdf', '-p', '1', '-o', 's.pdf'])
args = parser.parse_args()


args.func(args)

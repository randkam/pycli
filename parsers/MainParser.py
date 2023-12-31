from parsers.PDFParser import createPdfParser

def createSubParsers(parser):
    subparsers = parser.add_subparsers(help='sub-command help')
    pdfParser = subparsers.add_parser('pdf', help='PDF Tools')
    folderParser = subparsers.add_parser('file', help='b help')

    createPdfParser(pdfParser)
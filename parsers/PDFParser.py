import PdfTools

def createPDFMergeParser(pdfsubparsers):
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

def createPDFSwapParser(pdfsubparsers):
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

def createPDFDeleteParser(pdfsubparsers):
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

def createPDFRetainParser(pdfsubparsers):
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

def createPdfParser(pdfparser):
    pdfsubparsers = pdfparser.add_subparsers()

    createPDFMergeParser(pdfsubparsers)
    createPDFSwapParser(pdfsubparsers)
    createPDFDeleteParser(pdfsubparsers)
    createPDFRetainParser(pdfsubparsers)
    
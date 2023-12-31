import FileTools

def createPdfParser(fileParser):
    fileSubParser = fileParser.add_subparsers()

    deleteFilesContainingStringParser = fileSubParser.add_parser('scandelete', help= 'delete files which include cetain words')
    deleteFilesContainingStringParser.add_argument('-f','--folder', help = 'input folder', required = True)
    deleteFilesContainingStringParser.add_argument('-w','--word', help= 'delete files including this word/character in the filename', required= True)
    deleteFilesContainingStringParser.set_defaults(func= FileTools.deleteFilesContainingString)

    mergeFilesOfSameTypeParser = fileSubParser.add_parser('mergetxt', help = 'merge txt files in folder')
    mergeFilesOfSameTypeParser.add_argument('-f','--folder',help='input folder', required=True)
    mergeFilesOfSameTypeParser.add_argument('-o','--output',help='output file', required=True)
    mergeFilesOfSameTypeParser.set_defaults(func = FileTools.mergeFilesOfSameType)
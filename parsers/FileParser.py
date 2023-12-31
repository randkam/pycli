# folderSubparsers = folderParser.add_subparsers()

# folderdeltype = folderSubparsers.add_parser('scandelete', help= 'delete files which include cetain words')
# folderdeltype.add_argument('-f','--folder', help = 'input folder', required = True)
# folderdeltype.add_argument('-w','--word', help= 'delete files inclding this word/character file(ex. b, txt,...etc)', required= True)
# folderdeltype.set_defaults(func= folderTools.delType)

# folderMergeTxt = folderSubparsers.add_parser('mergetxt', help = 'merge txt files in folder')
# folderMergeTxt.add_argument('-f','--folder',help='input folder', required=True)
# folderMergeTxt.add_argument('-o','--output',help='output file', required=True)
# folderMergeTxt.set_defaults(func = folderTools.mergeTxt)
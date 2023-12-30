import os


def delfile(arg):
    for filename in os.listdir(arg.folder):
        if os.path.isfile(os.path.join(arg.name, filename)):
            if filename == arg.name:
                os.remove(os.path.join(arg.name, filename))


def delType(arg):
    for filename in os.listdir(arg.folder):
        if arg.type in filename:
            os.remove(os.path.join(arg.folder, filename))
        
def mergeTxt(arg):
    files = []
    for (_dirpath, _dirnames, filenames) in os.walk(arg.folder):
        files.extend(filenames)
        break
  
    txtList = []
    for i in files:
     if i.endswith(".txt"):
       txtList.append(i)  
    with open(arg.outputfile, "w") as newFile:
      for i in txtList:
        fileInFolder = os.path.join(arg.folder,i)
        with open(fileInFolder, "r") as file:
          content = file.read()
          newFile.write(content)
          newFile.write("\n")
  
    




import os

def deleteFilesContainingString(arg):
    for filename in os.listdir(arg.folder):
        if arg.word in filename:
            os.remove(os.path.join(arg.folder, filename))
        
def mergeFilesOfSameType(arg):
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
  
    




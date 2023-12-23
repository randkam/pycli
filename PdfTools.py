from PyPDF2 import PdfReader, PdfWriter

def keepPage(input_File, output_File, list):
  input_Pdf = PdfReader(open(input_File, 'rb'))
  output_Pdf = PdfWriter()

  for i in range(len(input_Pdf.pages)):
      if i in list:
          p = input_Pdf.pages[i]
          output_Pdf.add_page(p)

  with open(output_File, 'wb') as f:
      output_Pdf.write(f)
def removePage(input_File, output_File, page):
    input_Pdf = PdfReader(open(input_File, 'rb'))
    output_Pdf = PdfWriter()

    for i in range(len(input_Pdf.pages)):
        if i != page:
            p = input_Pdf.pages[i]
            output_Pdf.add_page(p)

    with open(output_File, 'wb') as f:
        output_Pdf.write(f)

def mergePDF(input_File, output_File, pageToAdd):
  original_Pdf = PdfReader(open(input_File, 'rb'))
  extra_Pdf = PdfReader(open(pageToAdd, 'rb'))
  output_Pdf = PdfWriter()

  for i in range(len(original_Pdf.pages)):
      p = original_Pdf.pages[i]
      output_Pdf.add_page(p)

  for i in range(len(extra_Pdf.pages)):
      p = extra_Pdf.pages[i]
      output_Pdf.add_page(p)

  with open(output_File, 'wb') as f:
      output_Pdf.write(f)


toDo = input("What would you like to do with PDF\n1. remove a page(s)\n2. merge two PDF's\n3.select pages from PDF\n4.swap pages\n")
if toDo == '1':
    input_File = input("Enter the name of the PDF file you want to remove a page from: ")
    pToRemove = int(input("Enter page to be removed: "))
    removePage(input_File, "output.pdf", pToRemove)
elif toDo == '2':
    firstFile = input("Enter name of  first PDF file: ")
    secondFile = input("Enter name of second PDF file: ")
    mergePDF(firstFile, "output.pdf", secondFile)
elif toDo == '3':
  input_File = input("Enter the name of the PDF file you want to remove a page from: ")
  keepGoing = True
  pList = []
  while keepGoing:
    pAdd = input("enter page to be kept, enter d when done: ")
    if pAdd == 'd':
      keepGoing = False
    else:
      pList.append(int(pAdd))
  keepPage(input_File, "output.pdf", pList)
elif toDo == '4':
   input_File = input("enter file which you like to reverse order")
   

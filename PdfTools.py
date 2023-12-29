from PyPDF2 import PdfReader, PdfWriter


def swap(arg):
  input_File = arg.input
  output_File = arg.output
  input_Pdf = PdfReader(open(input_File, 'rb'))
  output_Pdf = PdfWriter()

  p = [input_Pdf.pages[1], input_Pdf.pages[0]]

  output_Pdf.add_page(p[0])
  output_Pdf.add_page(p[1])

  with open(output_File, 'wb') as f:
    output_Pdf.write(f)


def keepPage(arg):
  input_File = arg.input
  output_File = arg.output
  list = arg.page
  for i in range(len(list)):
    list[i] = int(list[i]) - 1
  input_Pdf = PdfReader(open(input_File, 'rb'))
  output_Pdf = PdfWriter()

  for i in range(len(input_Pdf.pages)):
    if i in list:
      p = input_Pdf.pages[i]
      output_Pdf.add_page(p)

  with open(output_File, 'wb') as f:
    output_Pdf.write(f)


def removePage(arg):
  input_File = arg.input
  output_File = arg.output
  input_Pdf = PdfReader(open(input_File, 'rb'))
  output_Pdf = PdfWriter()
  pages = arg.page

  for i in range(len(input_Pdf.pages)):
    valid = 0
    for j in range(len(pages)):
      currentP = int(pages[j]) - 1
      if i != currentP:
        valid += 1
    if valid == len(pages):
      p = input_Pdf.pages[i]
      output_Pdf.add_page(p)

  with open(output_File, 'wb') as f:
    output_Pdf.write(f)


def mergePDF(arg):
  input_Files = arg.input
  output_File = arg.output
  original_Pdf = PdfReader(open(input_Files[0], 'rb'))
  extra_Pdf = PdfReader(open(input_Files[1], 'rb'))
  output_Pdf = PdfWriter()

  for i in range(len(original_Pdf.pages)):
    p = original_Pdf.pages[i]
    output_Pdf.add_page(p)

  for i in range(len(extra_Pdf.pages)):
    p = extra_Pdf.pages[i]
    output_Pdf.add_page(p)

  with open(output_File, 'wb') as f:
    output_Pdf.write(f)


# Some Changes

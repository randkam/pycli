from PyPDF2 import PdfReader, PdfWriter

def swap(input_File, output_File):
    input_Pdf = PdfReader(open(input_File, 'rb'))
    output_Pdf = PdfWriter()

    p = [input_Pdf.pages[1],input_Pdf.pages[0]]

    output_Pdf.add_page(p[0])
    output_Pdf.add_page(p[1])

    with open(output_File, 'wb') as f:
        output_Pdf.write(f)

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

def mergePDF(input_Files, output_File):
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


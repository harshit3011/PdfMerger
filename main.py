import PyPDF2
pdffiles =["cool.pdf","Receipt.pdf"]
merger = PyPDF2.PdfMerger()
for filename in pdffiles:
    pdfFile = open(filename,'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write('merged.pdf')

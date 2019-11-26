import PyPDF2
f=open("new.pdf","w+")
pdfr=PyPDF2.pdfFileReader(f)
print(pdfr.numpages)
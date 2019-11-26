from zipfile import *
f=ZipFile('myfile.zip',"w",ZIP_DEFLATED)
f.write("student.csv")
f.close()
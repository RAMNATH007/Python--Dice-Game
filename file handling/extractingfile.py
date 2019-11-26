from zipfile import *
with ZipFile("myfile.zip","r") as zipobj:
    zipobj.extractall('hello')

from PyPDF2 import PdfFileWriter, PdfFileReader
from getpass import getuser
import os.path, os
output = PdfFileWriter()
user = getuser()


def newdirectory(path):
    if os.path.exists(path=path) is False:
        new_path = os.mkdir(path=path)
        return new_path
    else:
        return path


def insert(pathfrom, limits: int):
    tempsplit = pathfrom.split("/")
    file = tempsplit[len(tempsplit) -1]
    path = newdirectory(f'/home/{user}/combine/temp') + file
    input = PdfFileReader(open(pathfrom, "rb"))
    pages = input.getNumPages()
    output.appendPagesFromReader(input)
    for limit in range(limits):
        output.addBlankPage(595, 842)

    out = open(path, "wb")
    output.write(out)
    out.close()
    return path



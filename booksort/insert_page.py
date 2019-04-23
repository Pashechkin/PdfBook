from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()


def insert(pathfrom, limits: int):
    tempsplit = pathfrom.split("/")
    file = tempsplit[len(tempsplit) -1]
    path = '/home/pavel/Документы/combine/temp/' + file
    input = PdfFileReader(open(pathfrom, "rb"))
    pages = input.getNumPages()
    output.appendPagesFromReader(input)
    for limit in range(limits):
        output.addBlankPage(595, 842)

    out = open(path, "wb")
    output.write(out)
    out.close()
    return path




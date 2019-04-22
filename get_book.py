from PyPDF2 import PdfFileReader, PdfFileWriter, PageRange
output = PdfFileWriter()


def get(path, pages: list, output_path):
    with open(path, 'r') as readfile:
        file = PdfFileReader(path)
        for list in pages:
            page = file.getPage(list)
            with open(output_path, "wb") as writefile:
                insert = output.insertPage(page=page, index=pages.index(list))
                output.write(writefile)


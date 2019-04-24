from PyPDF2 import PdfFileReader, PdfFileWriter

output = PdfFileWriter()


def get(path, pages: list, output_path):
    file = PdfFileReader(path)
    if file.isEncrypted:
        file.decrypt('')
    for lst in pages:
        page = file.getPage(lst-1)
        with open(output_path, "wb") as writefile:
            insert = output.insertPage(page=page, index=pages.index(lst))
            output.write(writefile)

    return "Sorting successfully done!"

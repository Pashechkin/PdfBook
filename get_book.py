from PyPDF2 import PdfFileReader, PdfFileWriter

output = PdfFileWriter()


def get(path, pages: list, output_path):
    file = PdfFileReader(path)

    for list in pages:
        page = file.getPage(list)

        with open(output_path, "wb") as writefile:
            insert = output.insertPage(page=page, index=pages.index(list))
            output.write(writefile)

    print("Sorting successfully done!")
    return None

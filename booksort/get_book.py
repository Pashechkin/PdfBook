from PyPDF2 import PdfFileReader, PdfFileWriter

output = PdfFileWriter()


def get(path, pages: list, output_path):
    file = PdfFileReader(path)

    for lst in pages:
        print(lst)
        page = file.getPage(lst-1)
        print(page)
        with open(output_path, "wb") as writefile:
            insert = output.insertPage(page=page, index=pages.index(lst))
            output.write(writefile)

    print("Sorting successfully done!")
    return None

import PyPDF2


def bookPDF():
    file = input()
    pages = int(input())
    book_file = open(f"{file}", "rb")
    read_pdf = PyPDF2.PdfFileReader(book_file)
    number_of_pages = read_pdf.getNumPages()
    print(number_of_pages)
    a = []
    if number_of_pages // 4:
        p = [i for i in range(1, number_of_pages + 1)]
        print(p)
        print(type(len(p)))
        print(type(pages))
        z = p[: len(p): pages]
        print(z)
        for i in z:
            s = p[z[i]: z[i + 1]: 1]
            print(s)



bookPDF()
#bookPDF("/home/lyusm/Документы/Linux.pdf")
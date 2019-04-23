from PyPDF2 import PdfFileReader, PdfFileWriter
from booksort.lib.slicer import slicer
from collections import deque
from booksort.get_book import get
from booksort.insert_page import insert


def book(pathfrom, pages):
    read = PdfFileReader(pathfrom)
    number = read.getNumPages()
    limit = 0

    while number % 4 != 0:
        number += 1
        limit += 1
    print(number, limit)
    path = ''

    if limit > 0:
        path = insert(pathfrom, limits=limit)

    newfile = PdfFileReader(path)
    numbers = newfile.getNumPages()
    numpages = [page for page in range(1, numbers+1)]
    srt = deque(slicer(numpages, pages*4))
    return_lst = []

    for nums in srt:
        dq = deque(nums)
        print(dq)
        while len(dq) is not 0:
            return_lst.append(dq.pop())
            return_lst.append(dq.popleft())
            return_lst.append(dq.popleft())
            return_lst.append(dq.pop())
    print(return_lst)
    return return_lst

from PyPDF2 import PdfFileReader
from booksort.lib.slicer import slicer
from collections import deque
from booksort.get_book import get


def book(pathfrom, pages, pathto):
    read = PdfFileReader(pathfrom)
    print(read.getNumPages())
    numpages = [page for page in range(1, read.getNumPages()+1)]
    srt = deque(slicer(numpages, pages*4))
    return_lst = []
    for nums in srt:
        dq = deque(nums)
        while len(dq) is not 0:
            return_lst.append(dq.pop())
            return_lst.append(dq.popleft())
            return_lst.append(dq.popleft())
            return_lst.append(dq.pop())
    print(return_lst)
    combine = get(path=pathfrom, pages=return_lst, output_path=pathto)

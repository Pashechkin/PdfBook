from booksort.get_book import get
from booksort.pagesorter import book


def main(input, output, pages):
    new_verison = book(pathfrom=input, pages=pages)
    new_pdf = get(path=new_verison[1], pages=new_verison[0], output_path=output)
    return None

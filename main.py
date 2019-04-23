#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from booksort.get_book import get
from booksort.pagesorter import book
from booksort.lib.slicer import slicer


@click.command()
@click.option('--input', help="paste path")
@click.option('--output', help="paste output path")
@click.option('--pages', default=10, help="paste pages")
def main(input, output, pages):
    print(input)
    new_verison = book(pathfrom=input, pages=pages)
    print(new_verison)
    new_pdf = get(path=input, pages=new_verison, output_path=output)
    return None


if __name__ == "__main__":
    main()
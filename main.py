#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from booksort.get_book import get
from booksort.pagesorter import book
from booksort.lib.slicer import slicer


@click.command()
@click.option('-i', '--input', help="paste path")
@click.option('-o', '--output', help="paste output path")
@click.option('-p', '--pages', default=10, help="paste pages")
def main(input, output, pages):
    new_verison = book(pathfrom=input, pages=pages)
    new_pdf = get(path=new_verison[1], pages=new_verison[0], output_path=output)
    return None


if __name__ == "__main__":
    main()
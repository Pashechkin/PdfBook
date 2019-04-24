from setuptools import setup, find_packages
from os.path import join, dirname
import booksort


setup(
    name="bookcombiner",
    version=booksort.__version__,
    packages=find_packages(),
    entry_points={
        'console_scripts':
            ['bookcombiner = booksort.main:main']
    },
    install_requires=[
        'click==7.0', 'PyPDF2==1.26.0'
    ],
    dependency_links=['https://github.com/Pashechkin/PdfBook.git'],
    include_package_data=True,
    zip_safe=False
)



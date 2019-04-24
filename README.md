# Book Combiner
### Description
This program will help you to print books you like.
Also, the format of the document will be structured and sheets will be sorted like a booklet format.

### Setup
```
git clone

cd BookCombiner/booksort

pip install virtualenv

cd BookCombiner

virtualenv [name of your env]

source [name]/bin/activate

./[name]/bin/python setup.py install
```

### User`s guide
Program has **3 options**:

- *-**i** {***path to pdf file***}*
- *-**o** {***path to new sorted pdf file***}*
- *-**p** {***amount of pages what will be in one notebook of your book***}*

Example:
```
bookcombiner -i /home/{user}/Test.pdf -o /home/{user}/Sorted_test.pdf -p 10
```


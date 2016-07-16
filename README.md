# Search within Books

## A small python TCP server that manipulates and servers data retrieved from books.

### Description

Folder 'books' contains several books in .txt format downloaded from https://www.gutenberg.org.
File `start-tcp-server.py` implements a python SocketServer which, by processing books data, can return the n most
common words, and the book titles a certain word appears into, followed by the occurrence of the word in each book.
File `search_books.py` implements all the backend process for the server. It stores data retrieved from the books 
inside a certain structure, and it draws results about:

1. The n most common words inside all books
2. Which books a word W appears into. Books are ordered by the number of appearances of the word W)

### Example of usage:

```
# this command should start the server
python start-tcp-server.py --host localhost --port 9999
```

In another terminal connect to the server

```
nc locahost 9999
```

and send the first command:

```
common 10
```

The server replies with the 10 most common words, for example:
```
und 883768
die 779996
der 752828
in 462536
zu 334216
den 330914
sie 330585
er 300633
das 299255
von 264353
```

The second command should be invoked like:

```
search word
```

The server replies with the filenames that `word` appears into, ordered by the number of appearances.
For example:

```
18731-8.txt 20
18731-0.txt 20
21917-8.txt 6
22627-8.txt 6
21917-0.txt 6
29336-0.txt 3
```

### Notes 

- First of all, taking into consideration that the slowest section of this program is the file i/o, I decided to
implement the "read and store" function as common for the two methods. Thus, at the very beginning of the server, data
is stored inside a structure *once and for all*, and, for that time on, data exist in the memory. This is a very 
convenient way of manipulating our data, because they're static and do not change during time. So, the two methods only 
retrieve data from the memory and do not have to do with any i/o.

- Data from files are read and stored inside `store_data()` function.

- At first, all digits and punctuation are removed. The `remove_numbers_and_punctuation()` function does this job.
This function slows the program approximately by 10%, because it is implemented for every word inside a book.

- Then, our data are stored inside a data structure. The data structure is a dictionary with books names as keys, and 
as values a `Counter()` structure for each word and their occurrence inside each book.
    
    Example of our structure:
    ```
    example_data_structure = {
        'book1.txt': {
            'word1': 456,
            'word2': 123,
            ...
        }
        'book2.txt': {
            'word3': 256,
            'word4': 100
            ...
        }
        ...
    }
    ```

- The two methods, `common` and `search` query the structure above. Both return a list of tuples which later on, is 
logged to us by the server.

- Code complexity. It scales with more books. (TODO)

- Concerns about implementation: The structure where our data are stored, is the key for code efficiency. Python 
dictionaries act like hash tables, which makes iteration a lot easier. They also have the "key - value" structure, 
which is something convenient for our case.

- Limitations. Storing data does approximately 10-11 seconds to run. This is something that definitely needs 
improvement.
## Search within Books

File books.tar.gz contains several books in text format downloaded from https://www.gutenberg.org.
Implement in *python* using *only* facilities from the standard library a simple TCP Server that does the following:

1. has a method that returns the n most common words
2. has a method that returns in which books a word W appears into. The results (books) should be ordered by the number of appearances of the word W)

Example of usage:
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
The server should reply with the 10 most common words, example:
```
and 1000
with 999
I 998
...
```

The second command should be invoked like:
```
search word
```
And the server should reply with the filenames that ```word``` appears into (ordered by the number of appearances)
example:
```
1.txt 30
2.txt 10
3.text 1

### Notes 

- Read the txt files
- Split the files into words and remove numbers and punctuation
- Store the words in an appropriate data structure
- query the data structure you created to answer the queries.
- First start with a naive approach that works and optimize later
- What is the time complexity of your solution? Does it scale with more books?
- If you have some concerns about your implementation or you have a better
  solution write the better solution in a comment if you do not implement it.
- Your solution does not have to be perfect but you need to know the limitations
  and comment them
- Use python 2.7.x and only facilities from the standard library. Do not
  use any kind of DBMS (sqlite included)
- If you have any questions feel free to contact us.

# -*- coding: utf-8 -*-
import SocketServer
from search_books.search_books import *


class MyTCPHandler(SocketServer.StreamRequestHandler):

    books_data = store_data('books/')

    def handle(self):
        _handlers = {'common': self.common_cmd,
                     'search': self.search_cmd}
        server_input_data = self.rfile.readline().strip()
        l = server_input_data.split()
        if len(l) >= 2:
            command, args = l[0], l[1:]
            f = _handlers.get(command, None)
            if f:
                ans = f(*args)
            else:
                ans = 'Invalid command'
        else:
            ans = 'Invalid Usage'
        self.request.sendall(ans + '\r\n')

    def common_cmd(self, *args):
        """
        Returns a string with the n most common words inside all books.
        Server will log the words with the format:
        "word occurences"
        """
        ans = []
        result = most_common_words(self.books_data, int(args[0]))
        for word, occurrence in result:
            ans.append("{} {}".format(word, occurrence))
        return '\n'.join(ans)

    def search_cmd(self, *args):
        """
        Returns a string with all the books a specific word appears
        into. Server will log the results with the format:
        "book occurence_of_the_word"
        """
        ans = []
        result = search_word(self.books_data, str(args[0]))
        for book, occurrence in result:
            ans.append("{} {}".format(book, occurrence))
        return '\n'.join(ans)

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999

    # Allows the reuse of the address, so that we can test changes easily.
    SocketServer.TCPServer.allow_reuse_address = True

    # Initialize server class. Storing whole books data takes some time.
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    print "Server initialization DONE!"

    # Server waits for input.
    server.serve_forever()

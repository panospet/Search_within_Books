# -*- coding: utf-8 -*-
import SocketServer
from search_books.search_books import *


class MyTCPHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        _handlers = {'common': self.common_cmd,
                     'search': self.search_cmd}
        data = self.rfile.readline().strip()
        l = data.split()
        if len(l) >= 2:
            command, args = l[0], l[1:]
            f = _handlers.get(command, None)
            print f
            if f:
                ans = f(*args)
            else:
                ans = 'Invalid command'
        else:
            ans = 'Invalid Usage'
        self.request.sendall(ans + '\r\n')

    def common_cmd(self, *args):
        """Add your code here for the common command
        This function should return a string with the
        most n most common words in the books
        """
        ans = []
        result = most_common_words('books/', int(args[0]))
        for word, occurrence in result:
            ans.append(word + " " + str(occurrence))
        return '\n'.join(ans)

    def search_cmd(self, *args):
        """Add your code here for the search command
        Should return a a string with the documents the
        word appears into"""
        ans = []
        result = search_word_in_books('books/', str(args[0]))
        for book, occurrence in result:
            ans.append(book + " " + str(occurrence))
        return '\n'.join(ans)

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999

    SocketServer.TCPServer.allow_reuse_address = True
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()

#!/usr/bin/env python
try:
    import SocketServer
except:
    import socketserver as SocketServer

import socket

GOPHER_ITEM_TYPES=["+", "g", "I", "T", "h", "i", "s", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

class GopherInvalidTypeException(Exception):
    def __init__(self):
        Exception.__init__(self)

class GopherItem:
    def __init__(self, itemType, desc, selector, host, port):
        if not(itemType in GOPHER_ITEM_TYPES):
            raise GopherInvalidTypeException
        self.itemType=itemType
        self.desc=desc
        self.selector=selector
        self.host=host
        self.port=str(port)
    def __str__(self):
        return self.itemType+("\t".join([self.desc, self.selector, self.host, self.port]))
    def get(self):
        try:
            return open(self.selector, 'r').read()+"\r\n.\r\n"
        except:
            return ".\r\n"

class GopherInfoItem(GopherItem):
    def __init__(self, desc):
        GopherItem.__init__(self, "i", desc, "fake", "(NULL)", "0")

class GopherSubmenu(GopherItem):
    def __init__(self, desc, selector, host, port, items=[]):
        GopherItem.__init__(self, "1", desc, selector, host, str(port))
        self.items=items
        self.selectorTable={}
        if(len(items)>0):
            self.generateSelectorTable()
    def generateSelectorTable(self):
        self.selectorTable={}
        for item in items:
            selectorTable[item.selector]=item
    def get(self):
        return "\r\n".join(map(str, self.items)+[".", ""])
    def insertItem(self, item):
        self.items.append(item)
        self.generateSelectorTable()
    def reply(self, selector):
        if(selector==""):
            return self.get()
        if not (selector in selectorTable):
            return ".\r\n"
        resp=selectorTable[selector]
        if(type(resp)==GopherSubmenu):
            return resp.get()
        if(type(resp)==GopherInfoItem):
            return resp.desc+"\r\n.\r\n"
        if(type(resp)==file):
            return resp.read()+"\r\n.\r\n"
        if(type(resp)==str):
            return resp+"\r\n.\r\n"
        if(type(resp)==GopherItem):
            return resp.get()
        return ".\r\n"

class GopherHandler(SocketServer.BaseRequestHandler):
    def __init__(self, server):
        SocketServer.BaseRequestHandler.__init__(self)
        self.gopherServer=server
    def handle(self):
        self.data=self.request.recv(1024).strip()
        self.request.sendall(self.gopherServer.reply(data))
        self.socket.close()

class MinimalGopherServer(GopherSubmenu):
    def __init__(self, host, port, items=[]):
        GopherSubmenu.__init__(self, "", "", host, str(port), items)
        self.server=SocketServer.TCPServer((host, port), GopherHandler(self))
    def serve_forever(self):
        self.server.serve_forever()




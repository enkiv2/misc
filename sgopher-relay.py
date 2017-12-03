#!/usr/bin/env python

try:
    import SocketServer
except:
    import socketserver as SocketServer

import socket
import os, sys
import tempfile

global server
server=None

class SGopherHandler(SocketServer.BaseRequestHandler):
    def __init__(self, *args, **kw_args):
        SocketServer.BaseRequestHandler.__init__(self, *args, **kw_args)
    def crypt(self, data, key, decrypt=True):
        mode="e"
        if(decrypt):
            mode="d"
        keyfile=tempfile.NamedTemporaryFile(delete=False)
        temp=tempfile.NamedTemporaryFile(delete=False)
        resfile=tempfile.NamedTemporaryFile(delete=False)
        keyfile.write(key)
        keyfile.flush()
        temp.write(data)
        temp.flush()
        keyfile.close()
        temp.close()
        resfile.close()
        os.system("openssl aes-256-cbc -salt -a  -"+mode+" -kfile "+keyfile.name+" -in "+temp.name+" -out "+resfile.name)
        res=None
        with open(resfile.name, "r") as f:
            res=f.read()
        for f in [resfile, keyfile, temp]:
            os.unlink(f.name)
        return res
    def rsacrypt(self, data, key, pub=True, decrypt=True):
        keyfile=tempfile.NamedTemporaryFile(delete=False)
        temp=tempfile.NamedTemporaryFile(delete=False)
        resfile=tempfile.NamedTemporaryFile(delete=False)
        keyfile.write(key)
        keyfile.flush()
        temp.write(data)
        temp.flush()
        keyfile.close()
        temp.close()
        resfile.close()
        pubflag=""
        if(pub):
            pubflag="-pubin"
        mode=""
        if(decrypt):
            mode="de"
        os.system("openssl rsautl -"+mode+"crypt "+pubflag+" -inkey "+keyfile.name+" -in "+temp.name+" -out "+resfile.name)
        res=None
        with open(resfile.name, "r") as f:
            res=f.read()
        for f in [resfile, keyfile, temp]:
            os.unlink(f.name)
        return res
    def newkey(self):
        keyfile=tempfile.NamedTemporaryFile(delete=False)
        os.system("openssl rand 32 -out "+keyfile.name)
        with open(keyfile.name, "r") as f:
            res=f.read()
        os.unlink(keyfile.name)
        return res
    def handle(self):
        self.data=self.request.recv(4096)
        key=self.rsacrypt(self.data.split("\r\n")[0], server.private_key, pub=False)
        data=self.crypt(self.data.split("\r\n")[1], key)
        chunks=data.split("\r\n")
        remotePubKey=chunks[0]
        (selector, host, port)=chunks[1].split("\t")
        s=socket.socket()
        s.open((host, int(port)))
        s.sendall(selector+"\r\n")
        page=[]
        ret=s.recv(4096)
        while(len(ret)>0):
            page.append(ret)
            ret=s.recv(4096)
        s.close()
        respkey=newkey()
        self.request.sendall(self.rsacrypt(respkey, remotePubKey, decrypt=False)+"\r\n"+self.crypt("".join(page), respkey, decrypt=False))
        self.socket.close()

class SGopherServer():
    def __init__(self, host, port, private_key):
        self.private_key=private_key
        self.server=SocketServer.TCPServer((host, int(port)), SGopherHandler)
    def serve_forever(self):
        self.server.serve_forever()

def main():
    global server
    if(len(sys.argv)<2):
        print("Usage: sgopher-relay /path/to/private/key [host [port]]")
        sys.exit(1)
    host="127.0.0.1"
    port="7001"
    with open(sys.argv[1], 'r') as f:
        pk=f.read()
    if(len(sys.argv)>2):
        host=sys.argv[2]
    if(len(sys.argv)>3):
        port=sys.argv[3]
    server=SGopherServer(host, port, pk)
    server.serve_forever()

if __name__=="__main__":
    main()


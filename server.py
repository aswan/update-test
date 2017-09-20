#!env python

import os
import shutil
import sys
import zipfile
import SimpleHTTPServer
import SocketServer

if len(sys.argv) != 3:
    raise Exception("Need 2 arguments")

host = sys.argv[1]
port = sys.argv[2]

def subst(fname):
    infp = open(fname, "r")
    raw = infp.read()
    infp.close()

    outfp = open("output/" + fname, "w")
    outfp.write(raw.replace("@HOST@", host).replace("@PORT@", port))
    outfp.close()

try:
    shutil.rmtree("./output")
except:
    pass
os.mkdir("./output")

shutil.copy("install.html", "output/install.html")
subst("update.json")

os.mkdir("output/v1")
zipfp = zipfile.ZipFile("output/v1.xpi", "w")
for fname in os.listdir("v1"):
    subst("v1/" + fname)
    zipfp.write("output/v1/" + fname, fname)
zipfp.close()
    
os.mkdir("output/v2")
zipfp = zipfile.ZipFile("output/v2.xpi", "w")
for fname in os.listdir("v2"):
    subst("v2/" + fname)
    zipfp.write("output/v2/" + fname, fname)
zipfp.close()

os.chdir("output")

server = SocketServer.TCPServer((host, int(port)), SimpleHTTPServer.SimpleHTTPRequestHandler)
server.serve_forever()

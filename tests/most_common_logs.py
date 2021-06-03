"""
Take a server log, parse out invalid responses (404, 500, etc.), and return the three most common files.

File: server.log:
[01/Aug/1995:00:54:59 -0400] "GET /images/abc.gif HTTP/1.0" 200 20
[01/Aug/1995:00:54:59 -0400] "GET /images/abc.gif HTTP/1.0" 200 20
[01/Aug/1995:00:54:59 -0400] "GET /images/abc.gif HTTP/1.0" 200 20
[01/Aug/1995:00:54:59 -0400] "GET /images/abc.gif HTTP/1.0" 200 20
[01/Aug/1995:00:54:59 -0400] "GET /images/abc.gif HTTP/1.0" 404 20
[01/Aug/1995:00:54:59 -0400] "GET /images/xyz.gif HTTP/1.0" 200 10
[01/Aug/1995:00:54:59 -0400] "GET /images/xyz.gif HTTP/1.0" 200 10
[01/Aug/1995:00:54:59 -0400] "GET /images/xyz.gif HTTP/1.0" 500 0
[01/Aug/1995:00:54:59 -0400] "GET /images/axz.gif HTTP/1.0" 200 30
[01/Aug/1995:00:54:59 -0400] "GET /images/axz.gif HTTP/1.0" 200 30
"""

import re
from collections import OrderedDict

log_file_path = r"./server.log"

files = {}

with open(log_file_path, "r") as file:
    for line in file:

        line = line.split()

        fi = line[3]
        resp = line[5]
        bytes = line[6]

        if resp == '200':
            if fi not in files:
                u = {fi: [1, int(bytes)]}
                files.update(u)
                print("added %s" % u)
            else:
                v = files[fi][0] + 1
                b = int(files[fi][1]) + int(bytes)
                del files[fi]
                u = {fi: [v, b]}
                files.update(u)
                print("updated %s" % u)


    files = OrderedDict([
      (x, files[x])
      for x in sorted(files, key=lambda x: files[x][1], reverse=True)
    ])

    flist = list(files.items())[:10]

    for i in flist:
        print("file: %s, occurences: %s, bytes: %s" % (i[0], i[1][0], i[1][1]))

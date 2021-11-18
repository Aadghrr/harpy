#!/usr/bin/python3 -i

import os, sys
from src.har import HTTPArchiveFile
from src.filter import Filter

if __name__=='__main__':
    if len(sys.argv)==0:
        print('Pass in a HAR file')
        os.exit()
    HAR_FILE = sys.argv[1]
    har = HTTPArchiveFile(HAR_FILE)

    def help():
        print("example()\nfilter('response.status.404',...)\n")

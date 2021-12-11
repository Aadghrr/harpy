#!/usr/bin/python3 -i

import sys
from src.har import HTTPArchiveFile
from src.filter import Filter

if __name__=='__main__':
    if len(sys.argv)<=1:
        print('Pass in a HAR file')
        sys.exit(1)
    HAR_FILE = sys.argv[1]
    har = HTTPArchiveFile(HAR_FILE)

    def help():
        print("example()\nfilter('response.status.404',...)\n")

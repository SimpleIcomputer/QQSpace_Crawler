#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'main function'
import fileoperation as fo
import crawler as sp
import sys
__author__ = 'SimpleIcomputer'


def main():
    try:
        a = input()
        contant = fo.contant_init()
        s_ready = sp.crawler_init(contant)
        if s_ready is False:
            sys.exit()
        dataframe = sp.crawling()
        fo.write2file(dataframe)
        sys.exit()
    except Exception as e:
        print(e)
        temp = input()
        sys.exit()


if __name__ == '__main__':
    main()

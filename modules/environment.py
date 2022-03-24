#-*- coding:utf8 -*-

import os

def run(**args):
    print "[*] In Environment module"
    return str(os.environ)
    
if __name__ == '__main__':
            run()

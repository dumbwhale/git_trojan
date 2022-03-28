#-*- coding:utf8 -*-
import os
def run(**args):

    print ("[*] In dirlister modules.")
    files = os.listdir(".")
    return str(files)


#!/usr/bin/env python3

import os
from Crypto.Protocol.KDF import PBKDF2

TARGET = '515906a567c9cdda27c06bb26daedcbf'

flag = input('Flag: ')
flag_hash = PBKDF2(flag, b'the-way-flag', count=10000)
if flag_hash == bytes.fromhex(TARGET):
    print('Well done! Have a shell!')
    os.system("/bin/sh")
else:
    print('Invalid flag')

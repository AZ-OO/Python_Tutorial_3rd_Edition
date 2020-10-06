"""
11.3 バイナリデータレコードの処理
"""

# structモジュールは、可変長の日無いレコードを処理する関数であるpack()と
# unpack()を提供する。

# 以下は、zipfileモジュールを使わずにZIPファイルの各ヘッダ情報にループをかける例
import struct

with open('myfile.zip', 'rb') as f:
    dat = f.read()

start = 0
for i in range(3): # 先頭から3つのファイルのヘッダを示す
    start += 14
    fields = struct.unpack('IIIHH', data[start:start+16])
    crc32, comp, size, uncomp_size, fileamesize, extra_size = fields

    start += 16
    filename = data[start:start + fileamesize]
    start += fileamesize
    extra = data[start:start + extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size # 次のヘッダまでスキップ





"""
10.9 データ圧縮
"""

# データのアーカイブ化と圧縮でよく使われるフォーマットの直接的なサポートが
# zlib、gzip、bz2、lzma、zipfile、tarfileといったモジュールにより提供されている

import zlib
s = b'witch which has which witches wrist watch'
print(len(s)) # <-- 41
t = zlib.compress(s)
print(len(t)) # <-- 37
print(zlib.decompress(t)) # <-- b'witch which has which witches wrist watch'
print(zlib.crc32(s)) # <-- 226805979


import json, zlib

# socket传输游戏信息，涉及到长字符串问题

JSONEncoder = json.JSONEncoder()
JSONDecoder = json.JSONDecoder()


# 字符串压缩
def compress_data(data: dict):
    str_data = ''.join(JSONEncoder.encode(data).split())
    print(len(str_data))
    level = zlib.compress(str_data.encode('utf-8'))
    print(len(level))
    return zlib.compress(level)


# 字符串解压缩
def decompress_data(zs):
    ds = zlib.decompress(zs)
    level = zlib.decompress(ds)
    return JSONDecoder.decode(level.decode('utf-8'))


if __name__ == '__main__':
    x = {str(i): i * 20 for i in range(30 ** 2)}
    length = len(''.join(JSONEncoder.encode(x).split()))

    print(f"Length x: {length}")
    compress_x = compress_data(x)

    decompress_x = decompress_data(compress_x)
    print(decompress_x == x)

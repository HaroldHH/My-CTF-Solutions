from math import ceil, sqrt
from Crypto.Util.number import long_to_bytes

# Reference : https://bomotodo.wordpress.com/2017/04/09/asis-quals-2017-dlp-158-points/

p = 0xa1c8e1e9b2301cb1f5d424ec6d959d7f275e11507b2177d55f3dc1268c9a3164b72832f362975023f09623814f80fe0ffad179d0e51c40b8a1f882d1f5f28e71
y = 0x6fa0fcc8c9c5f695a5709243698d7640c27c45352375919d538137333ab3a2c748cae5e7c1294d6ffc4007476f6fec6421c992f9fe1919b381306300caa2260953e48f2ec0de7b8c6417faa42001a748b1b367f5211095ddd6bf4e681f7e7ad787e0a7f562f6f0307d6a8d7e8d18cd59bd7572f0c4f430f0fd4fc61503b203f3bcd6dd0b0f84bbdbd42126d95b525fe77e4be62c6dbd083dbcaa284b20a9ea6faf9cbaf20dd88b0180417c9021fa1dcb52b2348c4376bd6b9b38a6c860086af

flag = ((y % (p**2)) - 1)//p
print("[+] Flag : " + str(long_to_bytes(flag)))

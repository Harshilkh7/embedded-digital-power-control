from automation.protocol import crc8, encode, decode

def test_crc_deterministic():
    assert crc8(b"ABC") == crc8(b"ABC")

def test_round_trip():
    payload = b"V=3.30,D=0.66"
    assert decode(encode(payload)) == payload

def test_corruption_rejected():
    f = bytearray(encode(b"HELLO")); f[-1] ^= 0xFF
    try: decode(bytes(f))
    except ValueError: return
    assert False

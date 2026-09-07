def crc8(data):
    crc = 0
    for b in data:
        crc ^= b
        for _ in range(8):
            crc = ((crc << 1) ^ 0x07) & 255 if crc & 0x80 else (crc << 1) & 255
    return crc

def encode(payload):
    if len(payload) > 255: raise ValueError("payload too large")
    return bytes([0xAA, len(payload)]) + payload + bytes([crc8(payload)])

def decode(frame):
    if len(frame) < 3 or frame[0] != 0xAA: raise ValueError("bad header")
    n = frame[1]
    if len(frame) != n + 3: raise ValueError("bad length")
    payload = frame[2:-1]
    if frame[-1] != crc8(payload): raise ValueError("CRC mismatch")
    return payload

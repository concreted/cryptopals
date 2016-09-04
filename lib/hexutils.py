import binascii

def hex_to_base64(hex_string):
    binary_string = binascii.unhexlify(hex_string)
    base64_string = binascii.b2a_base64(binary_string)
    return base64_string

def xor(hex_string_a, hex_string_b):
    pass

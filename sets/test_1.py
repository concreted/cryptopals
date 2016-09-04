import unittest

from lib import hexutils as h

class Set1(unittest.TestCase):

    def test_1_convert_hex_to_base64(self):
        hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        base64_string = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t\n"

        self.assertEqual(base64_string, h.hex_to_base64(hex_string))

    def test_2_fixed_xor(self):
        string_1 = "1c0111001f010100061a024b53535009181c"
        string_2 = "686974207468652062756c6c277320657965"
        1_xor_2 = "746865206b696420646f6e277420706c6179"

        self.assertEqual(1_xor_2, h.xor(string_1, string_2))

if __name__ == '__main__':
    unittest.main()

import unittest
import otp


class TestOtp(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_str2bits2str(self):
        test_str = 'aaaabjkdc'
        bits_res = otp.str2bits(test_str)
        res_str = otp.bits2str(bits_res)

        self.assertEquals(test_str, res_str)

    def test_keygen(self):
        n = 10
        key = otp.keygen(n)
        self.assertTrue(isinstance(key, list))
        self.assertTrue(len(key) == 10)

    def test_encAndDec(self):
        msg = 'helloworld'
        key = otp.keygen(15)
        ciphertext = otp.enc(msg, key)
        plaintext = otp.dec(ciphertext, key)
        self.assertTrue(msg == plaintext)


if __name__ == "__main__":
    unittest.main()
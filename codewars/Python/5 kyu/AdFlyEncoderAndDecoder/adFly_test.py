from adFly import adFly_decoder, addFly_encoder
import unittest

class TestAdFlyEncoderAndDecoder(unittest.TestCase):

    def test(self):
        self.assertEqual(adFly_decoder('O=T0ZToPdRHJRmwdcOz1oGvTL22lFzkRZhih5GsbezSw9kndbvyR50wYawHIAF/SdhT1'), 
        "http://yahoo.com")
        self.assertEqual(adFly_decoder('N=z0dDoMdyHIRmwac1zMolvWLz2RFmkMZiiZ5HsZeySw9kndbvyR50wYawHIAF/SdhT1'),
        'http://google.com')
        self.assertEqual(adFly_decoder('lololol'),
        'Invalid')
        self.assertEqual(adFly_decoder(adFly_encoder('http://yahoo.com')), 
        "http://yahoo.com")
        self.assertEqual(adFly_decoder(adFly_encoder('http://google.com')),
        'http://google.com')
        self.assertEqual(adFly_decoder(adFly_encoder('Hello World')),
        'Hello World')
        self.assertEqual(adFly_decoder(adFly_encoder('23456')),
        '23456')
        self.assertEqual(adFly_decoder(adFly_encoder('Come on I don\'t know')),
        'Come on I don\'t know')
        self.assertEqual(adFly_decoder(adFly_encoder('Very Good Job')),
        'Very Good Job')
        self.assertEqual(adFly_decoder(adFly_encoder('http://youtube.com')),
        'http://youtube.com')
        
if __name__ == '__main__':
    unittest.main()
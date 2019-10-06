from getVolumeOfCuboid import getVolumeOfCuboid
import unittest
class TestGetVolumeOfCuboid(unittest.TestCase):
    
    def test(self):
        self.assertEqual(getVolumeOfCuboid(2, 5, 6), 60)
        self.assertEqual(getVolumeOfCuboid(6.3, 3, 5), 94.5)
        
if __name__ == '__main__':
    unittest.main()
from rooms import rooms
import unittest
class TestGrasshopperCreateTheRooms(unittest.TestCase):
    
    def test(self):
        self.assert(len(rooms) >= 3, 'Should have at least three rooms')
        for name in rooms.values(): 
            self.assertIsInstance(name, dict, f'{name} should be a dictionary')
        for name in rooms.values(): 
            self.assert(len(name) >= 3, f'Not enough properties for room: {name}')

if __name__ == '__main__':
    unittest.main()
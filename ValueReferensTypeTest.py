import unittest

class TestValueTypes(unittest.TestCase):
    def test_about_numbers(self):
        def ismenenie(x):
            x += 2
            return x
        firstznach = 7
        self.assertEqual(firstznach, 7)  
        self.assertEqual(ismenenie(firstznach), 9)  

    def test_about_id(self):
        def id_in_pamat(x):
            first_id = id(x)
            x += 2
            second_id = id(x)

            self.assertNotEqual(first_id, second_id)
        value = 7
        id_in_pamat(value)

    def test_string(self):
        def ismenenie_string(s):
            s += " Korra"
            return s
        first_string = "Sofa"
        self.assertEqual(first_string, "Sofa")  
        self.assertEqual(ismenenie_string(first_string), "Sofa Korra")   

    def test_bool(self):
        def naoborot(b):
            b = not b
            return b
        firstperem = True
        self.assertEqual(firstperem, True)   
        self.assertEqual(naoborot(firstperem), False)

      
        
if __name__ == '__main__':
    unittest.main()
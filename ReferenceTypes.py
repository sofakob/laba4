import unittest

class TestReferenceTypes(unittest.TestCase):
    def test_kortech(self):
        def zminuemo_kortech(p):
            p += (4,)
            return p
        first_kortech = (1, 2, 3)
        self.assertEqual(first_kortech, (1, 2, 3))  
        self.assertEqual(zminuemo_kortech(first_kortech), (1, 2, 3, 4))

    def test_list(self):
        def zminemo_list(lst):
            lst.append(4)
            return lst
        first_list = [1, 2, 3]
        self.assertEqual(first_list, [1, 2, 3])
        self.assertEqual(zminemo_list(first_list), [1, 2, 3, 4])  
 

    def test_slov(self):
        def zminemo_slov(j):
            j["key"] = "value"
            return j
        first_slov = {"a": 1, "b": 2}
        izmeneno = zminemo_slov(first_slov)
        self.assertEqual(first_slov, {"a": 1, "b": 2, "key": "value"})  
        self.assertEqual(izmeneno, {"a": 1, "b": 2, "key": "value"})  

    def test_mnogestvo(self):
        def zminemo_mnogestvo(r):
            r.add(4)
            return r
        mnogestvo = {1, 2, 3}
        self.assertEqual(mnogestvo, {1, 2, 3}) 
        self.assertEqual(zminemo_mnogestvo(mnogestvo), {1, 2, 3, 4}) 


if __name__ == '__main__':
    unittest.main()
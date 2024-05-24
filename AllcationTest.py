import unittest
# У пітоні не можливо точно визначити, що об'єкт зберігається в списку або хіпі. Абстракція керування па'яті ускладнює взаємодію з нею в пітоні


class TestObectov(unittest.TestCase):

    def test_stack(self):
        a1 = 20
        a2 = 20
        b1 = "Sofa"
        b2 = "Sofa"

        self.assertEqual(id(a1), id(a2))
        self.assertEqual(id(b1), id(b2))
        
#малі числа та короткі строки напевно будуть мати однаковий індифікатор
    
    def test_hippi(self):
        spisok = [1, 2, 3, 4]
        slovnik = {"s": 1, "c": 2}

        class MyClass:
            pass

        obj = MyClass()

        self.assertNotEqual(id(spisok), id(slovnik))
        self.assertNotEqual(id(spisok), id(obj))
        self.assertNotEqual(id(slovnik), id(obj))
#об'єкти хіпі напевно будуть мати різні індефікатори    

if __name__ == "__main__":
    unittest.main()
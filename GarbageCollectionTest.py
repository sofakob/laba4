import gc
import unittest
import psutil

class TestGarbageCollection(unittest.TestCase):
    def setUp(self):
        # Отримуємо інформацію про поточний процес
        self.process = psutil.Process()

    def get_rss_memory(self):
         #отримання пам'яті RSS поточного процесу
        return self.process.memory_info().rss

    def create_large_object(self, size_in_mb):
        #створення великого об'єкта bytearray заданого розміру в МБ.
        return bytearray(1024 * 1024 * size_in_mb)

    def test_garbage_collection(self):
        
        large_object = self.create_large_object(256)  

        #Міряємо використання пам'яті перед видаленням об'єкта
        h1 = self.get_rss_memory()

        # Видаляємо об'єкт
        del large_object

        #Викликаємо збірку сміття
        gc.collect()

        #Міряємо використання пам'яті після видалення об'єкта і збору сміття
        h2 = self.get_rss_memory()

        #Перевіряємо, що h2 < h1
        self.assertLess(h2, h1, "Пам'ять не була правильно звільнена після збору сміття.")

if __name__ == '__main__':
    unittest.main()

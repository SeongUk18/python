import unittest
from abc_ex import Dog, Cat


class TestAnimal(unittest.TestCase):

    def setUp(self):
        self.dog = Dog()
        self.cat = Cat()

    def test_dog_sound(self):
        self.assertEqual(self.dog.sound(), "Bark")

    def test_dog_move(self):
        self.assertEqual(self.dog.move(), "Run")

    def test_cat_sound(self):
        self.assertEqual(self.cat.sound(), "Meow")

    def test_cat_move(self):
        self.assertEqual(self.cat.move(), "Jump")


if __name__ == '__main__':
    unittest.main()

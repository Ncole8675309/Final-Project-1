from Recursion_Controls import *
import unittest
#it should be noted, I replaced the thrown errors with error windows and stopped the computation from running
#this way it wouldn't crash the program when an error occurred and would instead let the user know of the issue

#if testing with this program is wanted, comment out all "e.msgbox" lines and uncomment the raises' error lines
class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(one(2, 1), 3)
        self.assertEqual(one(5, 1), 15)
        self.assertEqual(one(200, 1), 20100)
        self.assertEqual(one(5, 3), 12)
        self.assertEqual(one(200, 200), 200)

        with self.assertRaises(TypeError):
            one(1.1, 1)
            one(1, 1.1)
            one(.5, 0)
            one(0, .1)
            one("3", 0)
            one(0, "17")
            one(0, False)
            one(True, 12)

        with self.assertRaises(ValueError):
            one(-3, -2)
            one(0, 50)

    def test_two(self):
        self.assertEqual(two(1, 1), 1)
        self.assertEqual(two(1, 50), 1)
        self.assertEqual(two(5, 2), 25)
        self.assertEqual(two(50, 1), 50)
        self.assertEqual(two(5, 3), 125)
        self.assertEqual(two(-5, 3), -125)
        self.assertEqual(two(-5, 2), 25)
        self.assertEqual(two(0, 8), 0)

        with self.assertRaises(TypeError):
            two(1, 1.1)
            two(1.1, 1)
            two(1.1, 1.1)
            two("5", 3)
            two(5, "3")
            two(3, True)
            two(False, 18)

        with self.assertRaises(ValueError):
            two(1, 0)
            two(3, -5)

    def test_three(self):
        self.assertEqual(three(1, 1), "1")
        self.assertEqual(three(3, 1), "3 2 1")
        self.assertEqual(three(20, 1), "20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1")
        self.assertEqual(three(5, -4), "5 4 3 2 1 0 -1 -2 -3 -4")

        with self.assertRaises(TypeError):
            three("3", 0)
            three(0, "3")
            three(3.3, 0)
            three(0, -1.0)
            three(True, 0)
            three(0, False)

        with self.assertRaises(ValueError):
            three(2, 3)
            three(-1, 1)
            three(0, 50)

if __name__ == "__main__":
    unittest.main()
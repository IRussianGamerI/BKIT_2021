import unittest
import main


class TestBisquare(unittest.TestCase):
    def test_discriminant(self):
        self.assertEqual(main.discriminant(1, 2, 1), 0)
        self.assertEqual(main.discriminant(1, 2, 3), -8)
        self.assertEqual(main.discriminant(5, 0, 5), -100)

    def test_solve_square(self):
        self.assertEqual(main.solve_square(1, 4, 3), {-3, -1})
        self.assertEqual(main.solve_square(1, 2, 1), {-1})
        self.assertEqual(main.solve_square(100, 1, 100), set())
        with self.assertRaises(ZeroDivisionError):
            main.solve_square(0, 1, 1)

    def test_solve_bisquare(self):
        self.assertEqual(main.solve_bisquare(1, 4, 3), set())
        self.assertEqual(main.solve_bisquare(1, -4, 0), {0, 2, -2})


if __name__ == '__main__':
    unittest.main()

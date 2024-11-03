import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books_1(self):
        input = [data.Book(["Stephen King"], "IT"),data.Book(["JK Rowling"], "Harry Potter")]
        result = lab6.selection_sort_books(input)
        expected = [data.Book(["JK Rowling"], "Harry Potter"), data.Book(["Stephen King"], "IT")]
        self.assertEqual(expected, result)

    def test_selection_sort_books_2(self):
        input = [data.Book(["Dr. Seuss"], "Cat in the Hat"),data.Book(["EB White"], "Stuart Little"),
                    data.Book(["Edward Ashton"], "Mickey 7")]
        result = lab6.selection_sort_books(input)
        expected = [data.Book(["Dr. Seuss"], "Cat in the Hat"), data.Book(["Edward Ashton"], "Mickey 7"),
                 data.Book(["EB White"], "Stuart Little")]
        self.assertEqual(expected, result)

    # Part 2
    def test_swap_case_1(self):
        input = "Bananas"
        result = lab6.swap_case(input)
        expected = "bANANAS"
        self.assertEqual(expected, result)

    def test_swap_case_2(self):
        input = "aPPLe100"
        result = lab6.swap_case(input)
        expected = "ApplE100"
        self.assertEqual(expected, result)

    # Part 3
    def test_str_translate_1(self):
        input = "Beaches"
        result = lab6.str_translate(input, "e", "x")
        expected = "Bxachxs"
        self.assertEqual(expected, result)

    def test_str_translate_2(self):
        input = "Abracadabra"
        result = lab6.str_translate(input, "b", "t")
        expected = "Atracadatra"
        self.assertEqual(expected, result)

    def test_str_translate_3(self):
        input = "Abracadabra"
        result = lab6.str_translate(input, "a", "o")
        expected = "obrocodobro"
        self.assertEqual(expected, result)

    # Part 4
    def test_histogram_1(self):
        input = "eat to live do not live to eat"
        result = lab6.histogram(input)
        expected = {"eat": 2, "to": 2, "live": 2, "do": 1, "not": 1}
        self.assertEqual(expected, result)

    def test_histogram_2(self):
        input = "onion pepper corn orange onion onion corn beansprout"
        result = lab6.histogram(input)
        expected = {"onion": 3, "pepper": 1, "corn": 2, "orange": 1, "beansprout": 1}
        self.assertEqual(expected, result)




if __name__ == '__main__':
    unittest.main()

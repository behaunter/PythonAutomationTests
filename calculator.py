import unittest
import random


# print("Input number A")
# first_number = int(input())
# print("Choose math action:")
# print("+")
# print("-")
# print("*")
# print("/")
# user_action = input()
# print("Input number B")
# second_number = int(input())

class Calculator(unittest.TestCase):
    def test_calculate_all_actions(self):
        self.assertEqual(self.calculate('+', 2, 2), 4)
        self.assertEqual(self.calculate('*', 2, 2), 4) 
        self.assertEqual(self.calculate('-', 2, 2), 0) 
        self.assertEqual(self.calculate('/', 2, 2), 1)   

    def test_not_string_user_action(self):
        self.assertEqual(self.calculate('b', 2, 2), "not expect argument")

    def test_random_sum(self):
        first_random_int = random.randint(0, 10000)
        second_random_int = random.randint(0, 10000)
        int_sum = first_random_int + second_random_int
        self.assertEqual(self.calculate('+', first_random_int, second_random_int), int_sum)

    def test_random_div(self):
        fir_random_int = random.randint(0, 10000)
        sec_random_int = random.randint(1, 10000)
        int_div = fir_random_int / sec_random_int
        self.assertEqual(self.calculate('/', fir_random_int, sec_random_int), int_div)

    def test_random_mult(self):
        first_random_mult = random.randint(0, 10000)
        second_random_mult = random.randint(0, 10000)
        int_mult = first_random_mult * second_random_mult
        self.assertEqual(self.calculate('*', first_random_mult, second_random_mult), int_mult)

    def calculate(self, user_action, first_number, second_number):
        if user_action == "+":
            return (first_number + second_number)
        elif user_action == "-":
            return (first_number - second_number)
        elif user_action == "*":
            return (first_number * second_number)
        elif user_action == "/":
            # if second_number == 0:
            while second_number == 0:
                print("Input number B. NumberB MUST be NOT 0")
                print("Input number B")
                second_number = int(input())
            return (first_number / second_number)
        else:
            return "not expect argument"


    # print(calculate(user_action, first_number, second_number))

if __name__ == '__main__':
    unittest.main()
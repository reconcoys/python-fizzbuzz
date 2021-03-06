from nose.tools import assert_equals


class TestFizzBuzz:
    def __init__(self):
        pass

    def test_when_one_return_one(self):
        from fizz_buzz import FizzBuzz
        fb = FizzBuzz()
        result = fb.fizzbuzz(1)
        assert_equals(1, result)

    def test_when_two_return_two(self):
        from fizz_buzz import FizzBuzz
        fb = FizzBuzz()
        result = fb.fizzbuzz(2)
        assert_equals(2, result)

    def test_when_multiple_of_three_return_fizz(self):
        from fizz_buzz import FizzBuzz
        fb = FizzBuzz()
        result = fb.fizzbuzz(9)
        assert_equals('fizz', result)

    def test_when_multiple_of_five_return_buzz(self):
        from fizz_buzz import FizzBuzz
        fb = FizzBuzz()
        result = fb.fizzbuzz(10)
        assert_equals('buzz', result)

    def test_when_multiple_of_five_and_three_return_fizzbuzz(self):
        from fizz_buzz import FizzBuzz
        fb = FizzBuzz()
        result = fb.fizzbuzz(15)
        assert_equals('fizzbuzz', result)
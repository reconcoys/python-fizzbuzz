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
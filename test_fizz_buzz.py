from nose.tools import assert_equals


class testFizzBuzz:


    def test_when_one_return_one(self):
        from fizz_buzz import FizzBuzz
        fb = FizzBuzz()
        result = fb.fizzbuzz(1)
        assert_equals(1, result)
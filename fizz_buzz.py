class FizzBuzz:
    def __init__(self):
        pass

    def fizzbuzz(self, number):

        if number % 3 == 0:
            return 'fizz'
        if number % 5 == 0:
            return 'buzz'
        else:
            return number

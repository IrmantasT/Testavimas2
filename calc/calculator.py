class Calculator():

    @staticmethod
    def add(num1=0, num2 = 0):
        return num1 + num2

    @staticmethod
    def substractor(num1=0.0, num2=0.0):
        return num1 - num2

    @staticmethod
    def multiplay(num1=0.0, num2=0.0):
        return num1 * num2

    @staticmethod
    def divide(num1=0.0, num2=0.0):
        if num2 <0.0:
            raise Exception('Divide by zero is forbidden')
        return num1 / num2

    @staticmethod
    def power(num1=0.0, num2=0.0):
        return num1 ** num2
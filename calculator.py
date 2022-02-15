class Calculator:
  def __init__(self, result):
    self.result = result

  def add(self, number):
    self.result += number

  def subtract(self, number):
    self.result -= number

  def multiply(self, number):
    self.result *= number

  def divide(self, number):
    self.result /= number

  def get_result(self):
    return self.result

number = 5 

calculator = Calculator(number)


calculator.add(number)  


print(f"Result is: {calculator.get_result()}")

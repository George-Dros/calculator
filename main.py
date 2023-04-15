from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  
 "+": add,
 "-": subtract,
 "*": multiply,
 "/": divide
}


print(logo)

def calculator():
  continue_calculating = True
  num1 = float(input("What's the first number?: "))
    
  for operation in operations:
    print(operation)
      
    
  while continue_calculating == True:
      
    operation_symbol = input("Pick an operation from the line above: ")
      
    num2 = float(input("What's the next number?: "))
    answer = operations[operation_symbol](num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    next_calculation = input(f"type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:").lower()
    
    if next_calculation == 'n':
      continue_calculating = False
      calculator()
    
    elif next_calculation == 'y':
      num1 = answer
      

calculator()

      








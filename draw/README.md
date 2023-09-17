```
import random
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

class Level:

    def chance(self,user_input):
        if user_input == "easy":
            return EASY_LEVEL_ATTEMPTS
        elif user_input == "hard":
            return HARD_LEVEL_ATTEMPTS
        else:
            return EASY_LEVEL_ATTEMPTS
        

    def level_choice(self):
        user_level = input("Choose your playing level? 'easy' or 'hard'-")
        self.chance(user_input=user_level)
    




class Guess(Level):

    def __init__(self):
        super().__init__()
        self.computer_number = random.randint(1,100)

    def user_guess(self):
        self.guess_process(self.computer_number)


    

    def check_number(self,user_num,comp_num,attempts):
        if user_num == comp_num:
            game_on = False
            print("you guessed correct!")
            print(f"The Correct Nubmer is {comp_num}")
        elif user_num > comp_num:
            print("Too High")
            return attempts  - 1
        elif user_num < comp_num:
            print("Too Low")
            return attempts  - 1
        
       
    def attempts_check(self,comp_num):
        game_on = True
        while user_number != comp_num :
            print(f"You have {attempts} left")
            user_number = int(input("Make a guess: ")) 
            self.check_number(user_num=user_number,comp_num=self.computer_number,attempts=self.attempts)

```
















-----------------------------
```
"""
You are building a weather application that needs to store temperature data for different cities. Create a dictionary where the keys are city names and the values are lists of temperature readings. Perform the following tasks:

Add temperatures for at least 3 cities.
Add a new temperature to an existing city.
Remove the last temperature from a city.
Print the average temperature for each city.
"""

temperature_database = {
    "kolkata": [33,40,30,24],
    "raiganj": [34,38,29],
    "chennai": [22,37,25,29]
}
print(temperature_database)

temperature_database["raiganj"].append(50)
print(temperature_database)

temperature_database["raiganj"].pop()
print(temperature_database)

for temparature in temperature_database:
    toatal_temperature = 0
    values = temperature_database[temparature]
    values_length = len(values)
    for value in values:
        toatal_temperature += value
    avarage = round(toatal_temperature/values_length,2)
    print(avarage)
```


"""
Problem 3: Sales Analytics

You have sales data in the form of a list of dictionaries, where each dictionary represents a sale with 'product', 'quantity', and 'price'. Calculate the total sales for each product and store it in a dictionary where the product names are keys, and the total sales are values.

Problem 4: English to Spanish Dictionary

Create a simple English-to-Spanish dictionary. You should be able to add new word translations, update existing ones, and look up translations by providing an English word as input.

Problem 5: Student Records

You are managing student records. Create a dictionary where the keys are student IDs, and the values are dictionaries containing 'name', 'age', and 'grades'. Implement functions to:

Add a new student record.
Update a student's information (name, age, or grades).
Remove a student record by ID.
Calculate the average grade for a given student.
These problems cover various aspects of dictionary manipulation and usage. Solving them will help you gain a deep understanding of dictionaries in Python and their practical applications. Feel free to start with any problem that interests you the most!    
"""





---
> dir(__builtins__)

['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

---
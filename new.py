myInput = int(input("Enter a number:\n"));
try:
    result = 100 / myInput;
    print(f'Result is {result}');
except Exception as e:
    print(f'e is {e}')
finally:
    print("This is the final line to be printed")
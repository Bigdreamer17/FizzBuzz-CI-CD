def fizzbuzz(number: int):
    """
    Return A Fizz if the number is divisible by 3
    Return A Buzz if the number is divisible by 5   
    Return A FizzBuzz if the number is divisible by 3 and 5
    Return the number if the number is not divisible by 3 or 5
    """
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)
    
if __name__ == "__main__":
    userInput = int(input("Enter a number: "))
    print(fizzbuzz(userInput))
def fizzbuzz(number: int):
    """
    Returns a string based on the number given
    ---------- IF THE NUMBER IS DIVISIBLE BY 3, 5, OR BOTH ----------
    ---------- IF THE NUMBER IS DIVISIBLE BY 3 Return "Fizz"----------
    ---------- IF THE NUMBER IS DIVISIBLE BY 5 Return "Buzz"----------
    ---------- IF THE NUMBER IS DIVISIBLE BY 3 AND 5 Return "FizzBuzz"----------
    ---------- IF THE NUMBER IS NOT DIVISIBLE BY 3 OR 5 Return the number itself ----------
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
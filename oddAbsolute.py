def calculateAbsolute():

    # This first line is provided for you
    try:
        in_num  = int(input("Enter a number: "))
        if in_num > 21:
            result = (in_num - 21) * 2
        else: result = 21 - in_num
    except:
        result = "Please enter a numeric character."
    print("Result:", result)

    # end assignment

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()

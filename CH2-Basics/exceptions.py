# TODO: This code will cause an error because you can't devide by zero
# x = 10 / 0

# TODO: Exceptions provide a way of catching errors and then handling them 
try:
    x = 10/0
except:
    print("Well that didn't work!")

# TODO: YOu can also catch specific exceptions
try:
    answer = input("What should I devide 10 by?")
    num = int(answer)
    print(10/num)
except ZeroDivisionError as e:
    print("You can't devide by zero!")
    print(e)
except ValueError as e:
    print("YOu didn't give me a valid number")
finally:
    print("This code always runs")
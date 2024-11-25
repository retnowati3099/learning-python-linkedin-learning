def main():
    x, y = 100, 100

    # conditional flow uses if, elif, else
    if x < y:
        result = "x is less than y"
    elif x == y:
        result = "x is the same as y"
    else:
        result = "x is greater than y"
    print(result)

    #conditional statement let you use "a if c else b"
    result = "x is less than y" if x < y else "x is greater or equal to y"
    print(result)

if __name__ == "__main__":
    main()
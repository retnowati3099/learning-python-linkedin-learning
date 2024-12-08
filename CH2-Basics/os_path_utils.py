import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    # print the name of the os
    print(os.name)

    # check for item existence and type
    print("Item exists:", path.exists("text.txt"))
    print("Item is a file:", path.isfile("text.txt"))
    print("Item is a directory:", path.isdir("text.txt"))

if __name__ == "__main__":
    main()
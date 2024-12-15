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

    # work with file path
    print("Item's path:", path.realpath("text.txt"))
    print("Item's path and name:", path.split(path.realpath("text.txt")))

    # get the modification time
    t = time.ctime(path.getmtime("text.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("text.txt")))

    # calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("text.txt"))
    print(td)

if __name__ == "__main__":
    main()
def main():
    # open a file for writing and create it if it doesn't exist
    # my_file = open("text.txt", "w+")

    # open the file for appending text to the end
    # my_file = open("text.txt", "a+")

    # write some lines of data to the file
    # for i in range(10):
        # my_file.write("A line " + str(i + 1) + "\n")
        # my_file.write("A new line\n")

    # close the file when done
    # my_file.close()

    # open the file back up and read the contents
    my_file = open("text.txt", "r")
    if my_file.mode == "r":
        # contents = my_file.read()
        # print(contents)

        # read the file line by line
        fl = my_file.readlines()
        for x in fl:
            print(x)

if __name__ == "__main__":
    main()
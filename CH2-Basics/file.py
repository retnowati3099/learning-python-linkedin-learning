def main():
    # open a file for writing and create it if it doesn't exist
    my_file = open("text.txt", "w+")

    # write some lines of data to the file
    for i in range(10):
        my_file.write("A line" + str(i) + "\n")

    # close the file when done
    my_file.close()

if __name__ == "__main__":
    main()
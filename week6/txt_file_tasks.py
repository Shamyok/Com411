import os
import csv

def run_task2():
    def cwd():
        print("The current working directory is: ", os.getcwd())
        print("The directory contains the following files", os.listdir(os.getcwd()))

    def run():
        print("Processing...")
        cwd()
    run()

    def display_chars(filepath, numchars):
        with open(filepath) as txtfile:
            filetxt = txtfile.read(numchars)
            print(f"The first 5 characters are: \n{filetxt}")

    display_chars("library.txt", 5)

    def display_line(filepath):
        with open(filepath) as txtfile:
            filetxt = txtfile.readline()
            print(filetxt)
    display_line("library.txt")

    def display_text(filepath):
        with open(filepath) as txtfile:
            filetxt = txtfile.read()
            print(filetxt)
    display_text("library.txt")

    if __name__ == "__main__":
        run_task2()

def search(filename):
    print("Searching...")
    with open(filename) as txtfile:
        for line in txtfile:
            print(f"Looked in {line.strip()}")

search("library.txt")

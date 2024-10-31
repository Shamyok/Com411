import os
import csv


def cwd():
    print("The current working directory is: ", os.getcwd())
    print("The directory contains the following files", os.listdir(os.getcwd()))

def run():
    print("Processing...")
    cwd()
run()
from matplotlib import pyplot as plt
import random

def display_line(x,y):
    plt.plot(x,y)
    plt.show()

def run_task1():
    x_values = [1,2,3,4,5]
    y_values = [1,4,9,16,25]
    display_line(x_values,y_values)

def small():
    x = [3,3,4,4,3]
    y = [3,4,4,3,3]
    plt.xlabel("x values")
    plt.ylabel("y values")

    plt.plot(x,y,"ro--")


def medium():
    x = [2,2,5,5,2]
    y = [2,5,5,2,2]
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.plot(x,y,"gs--")

def large():
    x = [1,1,6,6,1]
    y = [1,6,6,1,1]
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.plot(x,y,"b-p")

def coordinate():
    x = int(input("Enter the x coordinate: "))
    y = int(input("Enter the y coordinate: "))
    return x,y

def path():
    print("Retrieving path...")
    x_values = []
    y_values = []
    for i in range (4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])
    return [x_values,y_values]

def runtask_3():
        values = path()
        x = values[0]
        y = values[1]
        plt.xlabel("x values")
        plt.ylabel("y values")
        plt.plot(x,y,"ro--")
        plt.show()


def data():
    paths = {}
    line = input("Would you like the line :,-- or -")
    color = input("What color would you like (R,G,B)?")
    marker = input("What marker would you like (o,s or ^)")
    paths['line_style'] = line
    paths['color'] = color
    paths['marker'] = marker
    return paths

def generate():
    lines = input("How many lines you would like?")
    for i in range(int(lines)):
        values = data()
        x = random.sample(range(1,20),10)
        y = random.sample(range(1,20),10)
        plt.show()

def run():
    print("Running...")
    generate()
    print("Done!")

run()
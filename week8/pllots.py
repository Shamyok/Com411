from matplotlib import pyplot as plt

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

small()
medium()
large()

plt.show()


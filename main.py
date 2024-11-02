import week1.input_tasks as wk1_input
import week1.output_task as wk1_output

def run_week_one():
    print("Which program in Week 1 do you wish to run?")
    response = input()
    if response == "simple_message":
        wk1_input.simple_message()
    elif response == "multiline_message":
        wk1_output.multiline_message()

def run():
    while True:
        print("What would you like to do?")
        print("[a] Run week 1 program")
        print("[q] Quit")
        response = input()

        if response == "a":
            run_week_one()
        elif response == "q":
            break
        else:
            print("Please enter a valid response.")

run()
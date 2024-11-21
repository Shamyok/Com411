class Robot:
    MAX_ENERGY = 100
    def __init__(self):
        self.name = "Robot"
        self.age = 0
        self.energy = Robot.MAX_ENERGY

    def display(self):
        print(f"I am {self.name}, I have {self.energy} energy.")

    def __repr__(self):
        return f"name={self.name}, age={self.age}, energy={self.energy}"

    def __str__(self):
        return f"I am {self.name}, I have {self.energy} energy."
def observed():
    observations = {"car","Sky Scraper","Sky Scraper", "Bike", "House","House"}
    return observations

def run_task1():
    print(observed())

def observed_items():
    observations = []
    for i in range(7):
        item = input(f"Please enter an observation:")
        observations.append(item)
    return observations

def run_task2():
    print("Counting observations")
    observation_list = observed_items()
    counting = set()
    for item in observation_list:
        counting.add((item, observation_list.count(item)))
    for observation in counting:
        print(observation)

run_task2()
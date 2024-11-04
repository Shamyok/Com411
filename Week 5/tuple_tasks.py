def likelihood():
    likelihoods = min(50, 38, 27, 99, 4)
    return likelihoods

def run_task1():
    likelihood_list = likelihood()
    print(f"Minimum likelihood of falling:{likelihood_list}%")

if __name__ == "__main__":
    run_task1()

def likelihood_min_max():
    min_value = min(50,38, 27, 99, 4)
    max_value = max(50,38, 27, 99, 4)
    return min_value, max_value
def run_task2():
    min_likelihood, max_likelihood = likelihood_min_max()
    print(f"Minimum likelihood of falling:{min_likelihood}%")
    print(f"Maximum likelihood of falling:{max_likelihood}%")
run_task2()


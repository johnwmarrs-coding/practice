import random
def generate_random_integer_lists(num_tests, min_val = 0, max_val = 100, length=100):
    test_data=[]
    for t in range(0, num_tests):
        test_list = []
        for i in range(0, length):
            test_list.append(random.randint(min_val, max_val))
        test_data.append(test_list)

    return test_data
        

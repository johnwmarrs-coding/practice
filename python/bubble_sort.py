from utils import generate_random_integer_lists
def bubble_sort(data_to_sort):
    data = data_to_sort.copy()
    # repeatedly swap adjacent elements to put largest elements towards the end
    for i in range(0, len(data)):
        for j in range(0, len(data) - i): # After each iteration, one element will move to its correct spot at the end
            if j + 1 < len(data) and data[j] > data[j+1]:
                # The current element is greater than the next, so you should swap them
                j_original = data[j]
                data[j] = data[j+1]
                data[j+1] = j_original
    return data

def main():
    num_tests = 1000
    test_data = generate_random_integer_lists(num_tests)
    
    tests_passed = 0
    for i in range(0, len(test_data)):
        if (bubble_sort(test_data[i]) == sorted(test_data[i])):
            tests_passed += 1
        else:
            print('Failed for test ' + str(i))
    print(str(tests_passed) + ' / ' + str(num_tests) + ' passed.')


    


if __name__ == '__main__':
    main()
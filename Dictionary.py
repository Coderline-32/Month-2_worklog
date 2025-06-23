def sort_dict():

    scores = {
        "Alice": 88,
        "Bob": 95,
        "Charlie": 70
    }
    sorted_dict = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
    print(sorted_dict)

def add_key():
    d = {0: 10, 1: 20}
    d[2] = 30
    d[3] =40
    print(d)
def concantenate_dict():
    dict1 = {1: 10, 2: 20}
    dict2 = {3: 30, 4: 40}
    dict3 = {5: 50, 6: 60}

    dict4 ={}

    for d in (dict1, dict2, dict3):
        print(d)
        dict4.update(d)
    print(dict4)
def check_key_existence():
    fruits = {
        "apple": 34,
        "banana": 78,
        "cherry": 21,
        "date": 56,
        "elderberry": 90,
        "fig": 45,
        "grape": 67,
        "honeydew": 12,
        "kiwi": 83,
        "lemon": 39
        }
    check_fruit = input("Enter the key: ").lower()
    
    if check_fruit in fruits:
         print("present")
    else:
        print("absent")

def dict_num_squares(x):
    for i in range(1, x+1):
        print(f"{i}: {i**2}")

def add_in_dict():
    n = {
        1: 3,
        2: 7,
        3: 12,
        4: 1,
        5: 9,
        6: 4,
        7: 14,
        8: 2,
        9: 6,
        10: 13
        }
    sum = 0
    for i in n:
        sum += n[i]
    print(sum)

def multiply_in_dict():
    n = {
        1: 3,
        2: 7,
        3: 12,
        4: 1,
        5: 9,
        6: 4
    }
    product =1
    for i in n:
        product *= n[i]
    print(product)

def remove_key():
    n = {
        1: 3,
        2: 7,
        3: 12,
        4: 1,
        5: 9,
        6: 4
    }
    if 1 in n:
        del n[1]
    print(n)
def map_two_lists():
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 90, 78]

    zipped_dict = dict(zip(names, scores))
    print(zipped_dict)

def max_and_min():
    students = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
    max_value = max(students.values())
    print(max_value)
    for name, value in students.items():
        if value > students["Alice"]:
            print(f"{name}:{value}")
def check_dict_empty():
    cars = {}

    if not bool(cars):
        print("Dictionary is empty")
def add_dict():
    from collections import Counter

    d1 = {'a': 100, 'b': 200, 'd': 300}
    d2 = {'a': 300, 'b': 200, 'd': 400}

    d3 = Counter(d1) + Counter(d2)
    sorted_d3 = dict(sorted(d3.items()))
    print(sorted_d3)

def distinct_dict():
    data = [{"IV":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    distinct_data = []
    for i in data:
        separate_values = list(i.values())[0]
        if separate_values not in distinct_data:
            distinct_data.append(separate_values)
    distint_data = set(distinct_data)
    print(distint_data)


def sep_int_from_string():
    data = ("Jack", "Sam", 78, 89)
    marks = []
    names = []
    for i in data:
        if isinstance(i, int):
            marks.append(i)
        else:
            names.append(i)

    print(tuple(names), tuple(marks))

def add_item_tuple():
    my_tuple = (1, 2, 3)
    new_tuple = my_tuple + (4,)
    changed_tuple = list(new_tuple)
    changed_tuple.append(6)
    new_tuple = tuple(changed_tuple)
    print(changed_tuple)
    print(new_tuple)
    print(new_tuple[:-4])
def clone_tuple():
    original_tuple = (1, 2, 3, 4, 5)
    cloned_tuple = original_tuple[:]
    print(cloned_tuple)
def check_repeated():
    my_tuple = (1, 2, 1, 3, 3, 4, 5, 4)
    unrepeat_list = []
    repeated_list = []
    
    for i in my_tuple:
        if i not in unrepeat_list:
            unrepeat_list.append(i)
        else:
            repeated_list.append(i)
    unrepeat_tuple = tuple(unrepeat_list)
    print(repeated_list)
    print(unrepeat_tuple)
def slice_tuple():
    my_tuple = (1, 2, 1, 3, 3, 4, 5, 4)
    sliced_tuple = my_tuple[3:8]
    print(sliced_tuple)
def find_index(check_index):
    names = ("John", "Sam", "Jack", "Samson", "Collins", "Mike", "Lawi")
    
    for i in range(len(names)):
        if check_index == names[i]:
            print(f"index is {i}")
            break
        else:
            print("Name not in the list or incorrect spelling")
            break
def to_dict():
    students = (("Jack", 78), ("Sam", 89), ("John", 85), ("Zipporah", 87))
    student_details = dict(students)
    for i in students:
        print(i)
    print(student_details)

    keys = ("Name", "Age", "City")
    values = ('Jack', 20, "Dodoma")

    person_details = dict(zip(keys, values))
    print(person_details)

def unzip_tuple():
    tuplex = ((1,2), (2,3), (3,4), (4,5), (5,6))
    listx = list(zip(*tuplex))
    print(listx)
unzip_tuple()

def reverse_tuple():
    my_tuple =(1,2,3,4,5,6,7,8)
    new_tuple = my_tuple[::-1]
    print(new_tuple)

def convert_to_dict():
    l = [("x", 1), ("x", 2), ( "x", 3), ("y", 1), ("y", 2), ("z", 1)]
    d = {}
    for a,b in l:
        d.setdefault(a, []).append(b)
    print(d)
convert_to_dict()
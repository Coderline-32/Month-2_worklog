def to_set():
    my_list = [1,2,3,4,5,6]
    my_set = set(my_list)
    print(my_set)
def add_to_set():
    my_set = {1, 2, 3, 4, 5, 6}
    my_set.add(7)
    my_set.remove(1)
    print(my_set)
def remove_from_set(i):
    my_set = {1, 2, 3, 4, 5, 6}
    if i in my_set:
        my_set.remove(i)
    else:
        print("Item not in the list")
    print(my_set)
def intersection():
    set_x = {"Apple", "Mango"}
    set_y = {"Mango", "Pineapple"}

    print("Original set elements:")
    print(f"Set-X = {set_x}")
    print(f"Set-X = {set_y}")

    print("Intersection of sets:")
    set_z =set_x & set_y
    print(f"Intersection is {set_z}")
def union():
    set_x = {"Apple", "Mango"}
    set_y = {"Mango", "Pineapple"}

    set_z =set_x.union(set_y)
    print(set_z)


def difference():
    set_x = {"Apple", "Mango"}
    set_y = {"Mango", "Pineapple"}
    set_z0 =set_x.difference(set_y)
    set_z1 = set_y.difference(set_x)
    set_z2 = set_z0.union(set_z1) 
    
    print(set_z2)
def isSubset():
    set_x = {"Apple", "Mango"}
    set_y = {"Mango", "Pineapple"}
    set_z = {"Pineapple"}

    print("Checking if set_x is subset of set_y")
    print(set_x.issubset(set_y))

    print("Checking if set_z is subset of set_y")
    print(set_z.issubset(set_y))
    set_x1 =set_x.copy()
    print(set_x1)
def freeze_set():
    set1 = frozenset([1,2,3,4,5,5])
    set2 = frozenset([5,6,7,8,9])
    set3 = set1.union(set2)
    print(set3)
def not_common():
    set1 ={1,2,3,4,5,6,7,8,9}
    set2 = {10,11,12,13,14,15}
    set3 = set1 & set2
    if not set1 & set2:
        print("No simlar items in the list")
    else:
        print(f"The intersection is: {set3}")
    
def rem_intersection():
    sn1 = {1, 2, 3, 4, 5}
    sn2 = {4, 5, 6, 7, 8}

    for i in sn1 & sn2:
        sn1.remove(i)
    print(sn1)
    print(sn2)

def count_appearance():
    words = ['Red', 'Green', 'Red', 'Blue', 'Red', 'Red', 'Green']
    words_set = set(words)
    words_count = {}
    for word in words:
        words_count[word] = (words.count(word)) 
    print(words_count)
count_appearance()
    

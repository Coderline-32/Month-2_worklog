def reverse_list():

    random_list = [42, "apple", 3.14, 87, "banana", 0.99, "chatgpt", 12, 7.5, "zebra"]

    reverse_list = random_list[::-1]
    print(reverse_list)

def find_larg_small_number():
    numbers = [3,4,5,2,6,7,8,9,10]
    numbers.sort()
    print(numbers)
    k = 2
    n = 3

    largest_number = (numbers[-k])
    smallest_number = (numbers[n-1])


    print(f"The kth largest number when k = {k} is {largest_number}")
    print(f"The nth smallest number when n = {n} is {smallest_number}")

def check_palindrome():
    palindrome_list = words = [
    "madam",
    "hello",
    "racecar",
    "world",
    "level",
    "python",
    "noon",
    "openai",
    "civic",
    "chatgpt",
    "radar",
    "mirror"
    ]
    for palindrome in palindrome_list:
        
        if palindrome == palindrome[::-1]:
            print(f"{palindrome}  is a palindrome")
        else:
            print(f"{palindrome}.Not a palindrome")

def remove_duplicates():
    words_with_duplicates = [
    "madam",
    "hello",
    "racecar",
    "world",
    "madam",
    "level",
    "python",
    "noon",
    "openai",
    "civic",
    "hello",
    "radar",
    "world",
    "refer",
    "cloud",
    "rotor",
    "planet",
    "deified",
    "reviver",
    "civic"
    ]
    seen = set()
    words_without_duplicates = []

    for word in words_with_duplicates:
        if word not in seen:
            seen.add(word)
            words_without_duplicates.append(word)
    print(words_with_duplicates)
    print(words_without_duplicates)

def find_subSequence():
    random_numberss = [7, 19, 3, 88, 15, 23, 5, 71, 60, 12, 99, 34, 8, 27, 1, 64, 50, 36, 90]
    subsequent_numbers = []

    for i in random_numberss:
        if not subsequent_numbers or i > subsequent_numbers[-1]:
            subsequent_numbers.append(i)
            

    print("Subsequence of numbers greater than the previous one:")
    print(subsequent_numbers)
    subsequence = []
    for i in range(len(random_numberss)):
        subsequence = [random_numberss[i]]
       
       
        for j in range(i+1, len(random_numberss)):
            if not subsequence or random_numberss[j] > subsequence[-1]:
                subsequence.append(random_numberss[j])

        print(f"Subsequence starting at index {i}: {subsequence}")
   




find_subSequence()
check_palindrome()
remove_duplicates()
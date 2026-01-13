from typing import Counter
def python_set1():  
    print(" ")
    print("Table of Contents:")
    print("------------------------------------------------------------ ")
    print("1. Return the first duplicate in a list: Lines 15 to 22")
    print("2. Check wheter a number is a palindrome or not: Lines 24 to 27")
    print("3. Sort a dictionary by values: Lines 29 to 31")
    print("4. Return all prime numbers in a given range: Lines 33 to 43")
    print("5. Convert a list of numbers to a string: Lines 45 to 47")
    print("------------------------------------------------------------ ")
    my_input = input("Enter one choice number:(1/2/3/.....):  ")
    print("------------------------------------------------------------ ")
    match my_input:
        case "1":
            def first_duplicate(lst):
                seen = set()
                for num in lst:
                    if num in seen:
                        return num
                    seen.add(num)
                return None
            print(first_duplicate([2, 3, 3, 1, 5, 2]))
        case "2":
            def is_palindrome(num):
                return str(num) == str(num)[::-1]
            print(is_palindrome(121))
            print(is_palindrome(123))
        case "3":
            def sort_dict_by_values(d):
                return dict(sorted(d.items(), key=lambda item: item[1]))
            print(sort_dict_by_values({'apple': 3, 'banana': 1, 'cherry': 2}))
        case "4":
            def primes_in_range(start, end):
                primes = []
                for num in range(start, end + 1):
                    if num > 1:
                        for i in range(2, int(num**0.5) + 1):
                            if num % i == 0:
                                break
                        else:
                            primes.append(num)
                return primes
            print(primes_in_range(10, 50))
        case "5":
            def list_to_string(lst):
                return ''.join(map(str, lst))
            print(list_to_string([1, 2, 3, 4, 5]))
    print("Like to see other programs in this set (y/n)? ")
    if input().lower() == 'y':
        python_set1()
    else:
        return
#------------------------------------------------------------------------
def python_set2():  
    print(" ")
    print("Table of Contents:")
    print("------------------------------------------------------------ ")
    print("1. Move zeros to end: Lines 68 to 70")
    print("2. Check sub string: Lines 72 to 74")
    print("3. Find Min and Max: Lines 76 to 78")
    print("4. Count Digits: Lines 80 to 87")
    print("5. Reverse list in Place: Lines 89 to 93")
    print("------------------------------------------------------------ ")
    my_input = input("Enter one choice number:(1/2/3/.....):  ")
    print("------------------------------------------------------------ ")
    match my_input:
        case "1":
            def move_zeros(lst):
                return [x for x in lst if x != 0] + [0]*lst.count(0)
            print(move_zeros([0,1,0,3,12]))
        case "2":
            def is_substring(s,sub):
                return sub in s
            print(is_substring("python codes","codes"))
        case "3":
            def min_max(lst):
                return min(lst),max(lst)
            print(min_max([8,3,43,23,9,1,3,6]))
        case "4":
            def count_digits(n):
                n = abs(n)
                count = 0
                while n > 0:
                    n //= 10
                    count += 1
                return count
            print(count_digits(123456787654321))
        case "5":
            def reverse_list(lst):
                lst.reverse()
                return lst
            nums = [1,2,3,4,5,3]
            print(reverse_list(nums))
    print("Like to see other programs in this set (y/n)? ")
    if input().lower() == 'y':
        python_set2()
    else:
        return
#------------------------------------------------------------------------
def python_set3():  
    print(" ")
    print("Table of Contents:")
    print("------------------------------------------------------------ ")
    print("1. Check if any two numbers add upto a target: Lines 114 to 121")
    print("2. Remove all occurances of an element: Lines 123 to 125")
    print("3. Find length withiout len(): Lines 127 to 132")
    print("4. Convert two list to one dictionary: Lines 134 to 146")
    print("5. Find common prefix: Lines 138 to 146")
    print("------------------------------------------------------------ ")
    my_input = input("Enter one choice number:(1/2/3/.....):  ")
    print("------------------------------------------------------------ ")
    match my_input:
        case "1":
            def has_pair(nums,target):
                seen = set()
                for n in nums:
                    if target - n in seen:
                        return True
                    seen.add(n)
                return False
            print(has_pair([2,7,11,15,12],9))
        case "2":
            def remove_all(lst,x):
                return [i for i in lst if i != x]
            print(remove_all([0,1,0,3,12],0))
        case "3":
            def str_length(s):
                count = 0
                for _ in s:
                    count += 1
                return count
            print(str_length("lakaparampil"))
        case "4":
            def list_to_dict(keys,values):
                return dict(zip(keys,values))
            print(list_to_dict(['a','b'],[1,2]))
        case "5":
            def common_prefix(strs):
                if not strs:
                    return ""
                prefix = strs[0]
                for s in strs[1:]:
                    while not s.startswith(prefix):
                        prefix = prefix[:-1]
                return prefix
            print(common_prefix(["flower","flow","flight"]))
    print("Like to see other programs in this set (y/n)? ")
    if input().lower() == 'y':
        python_set3()
    else:
        return
#------------------------------------------------------------------------
def python_set4():  
    print(" ")
    print("Table of Contents:")
    print("------------------------------------------------------------ ")
    print("1. Check if a number is power of two: Lines 170 to 173")
    print("2. Remove all spaces, tabs, new lines from a string: Lines 175 to 177")
    print("3. Find first non repeating character: Lines 179 to 186")
    print("4. Rotate list by k position to the right: Lines 188 to 193")
    print("5. Check wheter paranthesis are balanced: Lines 195 to 207")
    print("------------------------------------------------------------ ")
    my_input = input("Enter one choice number:(1/2/3/.....):  ")
    print("------------------------------------------------------------ ")
    match my_input:
        case "1":
            def is_power_of_two(n):
                return n > 0 and (n & (n - 1)) == 0
            print(is_power_of_two(16))
            print(is_power_of_two(18))
        case "2":
            def remove_spaces(s):
                return ''.join(s.split())
            print(remove_spaces("  Hello \n World \t "))
        case "3":
            from collections import Counter
            def first_unique(s):
                count = Counter(s)
                for char in s:
                    if count[char] == 1:
                        return char
                return None
            print(first_unique("swiss"))
        case "4":
            def rotate_list(lst,k):
                k = k % len(lst)
                print(lst[-k:])
                print(lst[:-k])
                return lst[-k:] + lst[:-k]
            print(rotate_list([1,2,3,4,5],2))
        case "5":
            def is_balanced(s):
                stack = []
                mapping = {')': '(', '}': '{', ']': '['}
                for char in s:
                    if char in mapping.values():
                        stack.append(char)
                    elif char in mapping.keys():
                        if not stack or stack[-1] != mapping[char]:
                            return False
                        stack.pop()
                return not stack
            print(is_balanced("({[]})"))
            print(is_balanced("({[})"))
    print("Like to see other programs in this set (y/n)? ")
    if input().lower() == 'y':
        python_set4()
    else:
        return
#------------------------------------------------------------------------
def python_set5():  
    print(" ")
    print("Table of Contents:")
    print("------------------------------------------------------------ ")
    print("1. find the second largest element in a list: Lines 228 to 230")
    print("2. Check if a string has all unique characters: Lines 232 to 234")
    print("3. Find GCD of two numbers: Lines 236 to 239")
    print("4. count uppercase and lowercase letters in a string: Lines 241 to 245")
    print("5. find the longest word in a sentence: Lines 247 to 250")
    print("------------------------------------------------------------ ")
    my_input = input("Enter one choice number:(1/2/3/.....):  ")
    print("------------------------------------------------------------ ")
    match my_input:
        case "1":
            def second_largest(lst):
                return sorted(set(lst))[-2]
            print(second_largest([3,1,4,4,5,5,2]))
        case "2":
            def has_unique_chars(s):
                return len(set(s)) == len(s)
            print(has_unique_chars("hello"))
        case "3":
            import math
            def gcd(a,b):
                return math.gcd(a,b)
            print(gcd(48,18)) 
        case "4":
            def count_case(s):
                upper = sum(1 for c in s if c.isupper())
                lower = sum(1 for c in s if c.islower())
                return upper, lower
            print(count_case("Hello World!"))
        case "5":
            def longest_word(s):
                words = s.split()
                return max(words, key=len)
            print(longest_word("The quick brown fox jumps over the lazy dog"))
    print("Like to see other programs in this set (y/n)? ")
    if input().lower() == 'y':
        python_set5()
    else:
        return
#------------------------------------------------------------------------
# Main Program Starts Here
print("Welcome to Python Programming Study Programs")
python_set1()
print("Proceed and see other programs in next; set-2 (y/n)? ")
if input().lower() == 'y':
    python_set2()
print("Proceed and see other programs in next; set-3 (y/n)? ")
if input().lower() == 'y':
    python_set3()
print("Proceed and see other programs in next; set-4 (y/n)? ")
if input().lower() == 'y':
    python_set4()
print("Proceed and see other programs in next; set-5 (y/n)? ")
if input().lower() == 'y':
    python_set5()
else:
    exit()
#------------------------------------------------------------------------
# End of the Main Program
#------------------------------------------------------------------------
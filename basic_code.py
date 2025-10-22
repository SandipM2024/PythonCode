#No-1 Reverse a string without using slicing.
def reverse_string(string):
    reverse=""
    for i in string:
        reverse = i + reverse
    return reverse
print(reverse_string("sandip"))

# with slice
word="Sandip"
reverse=word[::-1]
print(reverse)



# Check if a string is a palindrome.
def is_palindrome(word):
    return word == word[::-1]
   
print(f"palindrome are : {is_palindrome("madam")}")



#No-2 Find factorial of a number (iterative & recursive).
def factorial_iterative(number):
    fact=1
    if number==0:
        return 1
    for i in range(1, number+1):
        fact *=i
    return fact
   

print(f"factoriar using iterative:, {factorial_iterative(5)}")

def factorial_recursive(number):
     return 1 if number == 0 else number * factorial_recursive(number - 1)
   
print(f"factorial using recursive: {factorial_recursive(5)}")



#No-3 Generate Fibonacci series up to n terms.
def fibonacci_series(n):
    a, b=0, 1
    for i in range(1 , n+1):
        print(a, end=" ")  
        a, b=b, a+b
    print()  # move to next line after series
print(fibonacci_series(10))



#No-4 Check if a number is prime.
def is_prime(n):
    # 0, 1 and negative numbers are not prime
    if n <= 1:
        return False
        
    # 2 and 3 are prime numbers
    if n <= 3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n%i == 0 or n % (i+2) == 0:
            return False
        i +=6
    return True
    
    
num = 29
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
    
    
# Loop only up to √n:

# If a number has a factor greater than √n, the corresponding smaller factor will already have been found.

# 6k ± 1 rule:

# All prime numbers greater than 3 are of the form 6k ± 1.
# Example: 5, 7, 11, 13, 17...
    # Check for factors from 5 to √n



#No-5 Find all prime numbers between two numbers.
def is_prime(n):
    if n<=1:
        return False
    if n <= 3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    i=5
    while i*i <= n:
        if n*i == 0 or n*(i+2) == 0:
            return False
        i += 6
    return True


def find_prime_between_number_range(start, end):
    prime=[]
    for n in range(start, end+1):
        if is_prime(n):
            prime.append(n)
    return prime




#No-6 Count vowels and consonants in a string.
def count_vowels_consonats(word):
    v, c=0,0
    for latter in word.lower():
        if latter.isalpha():
            if latter in ['a','e','i','o', 'u']:
                v +=1
            else:
                c +=1
    return v, c

v,c = count_vowels_consonats("Eandip")
print("number of vowels:", v)
print("number of consonat:", c)




#No-7 Swap two numbers without using a third variable.

a,b=2, 3
def swap_number(a, b):
    print(f"before swap a: {a} & b:{b}")
    a=b
    b=a
    print(f"after swap a: {a} & b:{b}")
swap_number(a, b)

#No-8 Swap two numbers with using a third variable.
def swap_with_third_variable(a,b):
    print(f"before swap a: {a} & b:{b}")
    c=a
    a=b
    b=c
    print(f"after swap a: {a} & b:{b}")
    
swap_with_third_variable(a,b)




#No-9 Check if a number is an Armstrong number.
def is_armstrong(number):
    lennumber=len(str(number))
    # result=0
    # for digit in str(number):
    #     result += int(digit)**lennumber
    result =sum(int(digit)**lennumber for digit in str(number))
    return number == result
print(f"armstrong are {is_armstrong(153)}")



#No-10 Find the largest number in a list.
def get_largest_number(number_list):
    largest_number=number_list[0]
    for number in number_list:
        if largest_number <= number:
            largest_number= number
    return largest_number

number_list=[20, 30,45, 38, 98, 11,87]
print(f"Largest number of the list: {get_largest_number(number_list)}")



#No-11 Find the smallest number in a list.
def get_smallest_number(number_list):
    smallest_number=number_list[0]
    for number in number_list:
        if smallest_number >= number:
            smallest_number= number
    return smallest_number

number_list=[20, 30,45, 38, 98, 11,87]
print(f"Smallest number of the list: {get_smallest_number(number_list)}")



##No-12 Count frequency of each character in a string.
def count_frequency_of_each_character(string):
    f_dict={}
    for char in string:
        f_dict[char]=f_dict.get(char, 0) + 1
    print("Character frequencies:")
    for char, freq in  f_dict.items():
        print(f"'{char}': {freq}")
    return f_dict
print(f"Count frequency of each character in a string are {count_frequency_of_each_character("sasimita")}")
    

# Use by Counter fucntion 
from collections import Counter
def count_frequency_of_each_character_use_counter(string):
    frequency=Counter(string)
    for char, freq in  frequency.items():
        print(f"'{char}': {freq}")
    # return f_dict
    
count_frequency_of_each_character_use_counter("Hello Sasimita")




##No-13 Reverse a list without using reverse().
# By using Slice
def reverse_list_with_slice(lst):
    return lst[::-1]

lst=[1,2,3,4,5,6,7,8,8,9,0]
print(f"Reverse a list using slice: {reverse_list_with_slice(lst)}")


# without slice
def reverse_list_without_slice(lst):
    start=0
    end=len(lst) - 1
    while start <= end:
        lst[start], lst[end] = lst[end], lst[start]
    return lst

lst=[1,2,3,4,5,6,7,8,8,9,0]
print(f"Reverse a list without using reverse: {reverse_list_with_slice(lst)}")


# use reverse 
def reverse_list(lst):
    lst=[1,2,3,4,5,6,7,8,9,0]
    return list(reversed(lst))
lst=[1,2,3,4,5,6,7,8,8,9,0]
print(f"Reverse a list with using reverse: {reverse_list(lst)}")



#No-14 Merge two sorted lists into one sorted list.

# Method 1: Two-Pointer Technique (Efficient O(n + m))
def merge_sorted_lists(list1, list2):
    i, j = 0, 0
    merged_list=[]
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    # # Add remaining elements
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list
    


list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
result = merge_sorted_lists(list1,list2)
print("Merged Sorted List:", result)


# Method 2: Using sorted() (Simpler but Less Efficient)
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

merged_list = sorted(list1 + list2)
print("Merged Sorted List:", merged_list)


# Method 3: Using heapq.merge() (Best for Iterators)
import heapq

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

merged_list = list(heapq.merge(list1, list2))
print("Merged Sorted List:", merged_list)






#15. Find the sum of digits of a number.
def sum_of_digits(number):
    sum=0
    for i in str(number):
        sum += int(i)
    return sum
num = int(input("Enter a number: "))
print(f"sum of digits of {num} is : {sum_of_digits(num)}")

# Function to calculate the sum of digits (bast approse)
def sum_of_digits(number):
    number=abs(number)
    total =0
    while number > 0:
        digit = number % 10
        total +=digit
        number //= 10
    return total
# Example usage
num = int(input("Enter a number: "))
print(f"The sum of digits of {num} is: {sum_of_digits(num)}")

# Alternative (Python One-Liner):
num = int(input("Enter a number: "))
print("Sum of digits:", sum(map(int, str(abs(num)))))











#No-1 Remove all duplicate characters from a string.
def remove_duplicate_from_string(string):
    remove=""
    for word in string:
        if word not in remove:
            remove +=word
    return remove
string=input("Enter a string: ")
print(f"Remove all duplicate characters from {string} is : {remove_duplicate_from_string(string)}")


#No-2 Find first non-repeating character in a string.
def first_non_repeating_char(string):
    freq={}
    for char in string:
        freq[char] = freq.get(char, 0) + 1
    print(freq)
    for char in freq:
        if freq[char] == 1:
            return  char
string = "sasimit"
print(f"first non-repeating character in {string} are:  {first_non_repeating_char(string)}") 

#No-3 Check if two strings are anagrams.
def are_analag(str1, str2):
    if len(str1) != len(str2):
        return False
    char_count={}
    for char in str1:
        char_count[char] = char_count.get(char, 0) +1
    print(char_count)
    for char in str2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    return True
print(f"analag are: {are_analag("abc", "cba")}")

# Solution 2: Using collections.Counter (More Efficient)
from collections import Counter
def are_analog(str1, str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    return Counter(str1) == Counter(str2)
str1="abc"
str2="cab"
print(f"analog are: {are_analog(str1, str2)}")


# Solution 2: Using sorted()
def are_analog(str1, str2):
    str1=str1.replace(" ", "").lower()
    str2=str2.replace(" ", "").lower()
    return sorted(str1)==sorted(str2)
str1="abc"
str2="cab"
print(f"analog are: {are_analog(str1, str2)}")




#No-4 Count occurrences of a substring in a string.
# 3. Manual Loop Method (Overlapping Support)
def count_substring(text, substring):
    count=0
    for i in range(len(text)-len(substring) +1):
        # print(text[i:i+len(substring)], i)
        if text[i:i+len(substring)] == substring:
            count +=1
    return count
            
text="aaaa"
substring="aa"
print("Occurrences:", count_substring(text, substring))
 

# **2. Counting Overlapping Substrings
import re

text = "aaaa"
substring = "aa"

count = len(re.findall(f"(?={re.escape(substring)})", text))
print(f"Occurrences of '{substring}' (including overlaps):", count)


#1. Using str.count() (Simple & Direct)
text = "hello world, hello python, hello AI"
substring = "hello"

count = text.count(substring)
print(f"Occurrences of '{substring}':", count)



#No-5 Convert a string to title case without using .title().
# using title()
string ="Sandip mohapatra"
print(string.title())

# **1. Using .split() and .capitalize()
def to_title_case(text):
    words=string.split()
    return " ".join(word[0].upper() +  word[1:].lower() if word else "" for word in words)
        
string = "sandip mohapatra"
print(to_title_case(string))

# 2. Without .capitalize() (Manual Implementation)
def to_title_case(string):
    words = string.split()
    title_cased_words = []
    for word in words:
        if word:
            title_cased_words.append(word[0].upper() + word[1:].lower())

    return " ".join(title_cased_words)    

string = "sandip mohapatra"
print(to_title_case(string))


# 3. Using List Comprehension (Short Version)
text = "hELLO worLD"
result = " ".join([w[0].upper() + w[1:].lower() for w in text.split() if w])
print(result)


# 4. Handling Multiple Spaces & Punctuation
import re

def to_title_case(text):
    return re.sub(r"[A-Za-z]+", lambda match: match.group(0)[0].upper() + match.group(0)[1:].lower(), text)

text = "   hello   world! THIS is, python.  "
print(to_title_case(text))



# No-6 Check if two strings are rotations of each other.
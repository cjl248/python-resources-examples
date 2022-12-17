"""
Personal list of Python notes, resources and examples gathered while preparing
for the technical challenge and coming from a Ruby background.
"""

from functools import reduce
from itertools import accumulate
# from itertools import iter
# from collections import OrderedList

# EXAMPLE OF STRING SUBSTITUTION
# s = 'christian julian liendo'; l = ''.join((s.replace(' ', ', ')))
# print(f"STRING SUBSTITUTION: {l}")


# DIFFERENT WAYS OF LOOPING
# print("\n\nLOOPING")
# a = [1,2,3,4,5]
# cubed = lambda x: x*x*x

# example of for loop using helper fn with range
# for_loop = [cubed(i)+1 for i in range(0, 5)]

# example of map, filter combo returning iterable on iterable
# filtered_map = [num*num for num in range(0, 20) if num % 2 == 0]

# example of using list constructor with lambda
# list_lambda = list(filter(lambda x: x+3, range(2, 25)))

# example of reduce with lambda
# reduced = reduce(lambda acc, curr: acc + curr, a)

# example of for loop using helper fn with range
# print(f"example of for loop using helper fn with range: {for_loop}")

# example of map, filter combo returning iterable on iterable
# print(f"example of map, filter combo returning iterable on iterable: {filtered_map}")

# example of using list constructor with lambda
# print(f"example of using list constructor with lambda: {list_lambda}")

# example of reduce with lambda
# print(f"example of reduce with lambda{reduced}")

# example of reversing a list
# print(f"example of reversing a list: {a[::-1]}")


# BOOLEANS AND ISINSTANCE
# print("\n\nBOOLEANS AND ISINSTANCE") 

# m = None
# n = 1.0
# p = "hi"
# print(f"None dir: {dir(m)}")
# print(f"isinstance1: {isinstance(n, int)}")
# print(f"isinstance2: {isinstance(n, (int, float))}")
# print(f"isinstance_string: {isinstance(p, str)}")


# DICTIONARIES
# print("\n\nDICTIONARIES") 

# FOR LOOP ITERATION LIST TO DICT W STRIP
# unwanted_chars = ".,-_"
# to_count = "I am drinking too much coffee. Drinking too much coffee is bad."
# formatted = to_count.lower()
# string_list = formatted.split(' ')
# word_count = {}

# for raw_word in string_list:
# 	word = raw_word.strip(unwanted_chars)
# 	if word not in word_count:
# 		word_count[word] = 0
# 	word_count[word] += 1
# print(f"FOR LOOP ITERATION LIST TO DICT EXAMPLE: {word_count}")

# DELETE EXAMPLE
# formatted_word_count = word_count.copy()
# for k, v in word_count.items():
# 	if v == " ":
# 		del formatted_word_count[k]
# print(f"DELETE EXAMPLE: {formatted_word_count}")

# SORTING EXAMPLE
# sorted_word_count = dict(sorted(formatted_word_count.items(), key=lambda item: item[1], reverse=True))
# print(f"SORTING EXAMPLE: {sorted_word_count}")

# JOINING EXAMPLE
# joined_str = ' '.join(list(sorted_word_count.keys()))
# print(f"JOINING EXAMPLE: {joined_str}")
# print(f"DICTIONARY (D <- L) EXAMPLE PROBLEM: {joined_str.capitalize()+'.'}")



################
# KEY CONCEPTS #
################


# INT & FLOAT #
# 
# FLOAT FORMAT EXAMPLE: print("%.6f" % float(0.03484958934))
# CONSTRUCTORS: int(), float()


# STRINGS #
# 
# PRINT EXAMPLE: print("Hello", "how are you", sep=". ", end="?")
# FORMAT: print(f"str: {var}")
# REPLACE: 'helloooll'.replace('ll', 'xxx')
# JOIN(S <- LIST): joined_str = ' '.join(list(sorted_word_count.keys()))
# JOIN(S <- DICTIONARY): joined_str = ' '.join(list(sorted_word_count.keys()))
# STRIP CHARS: word = raw_word.strip(".,-_")
# CAPITALIZE FIRST CHAR: joined_str.capitalize()
# ALL LOWERCASE: formatted = "CHRIS".lower()
# FORMATTING: print(f"example of reversing a list: {a[::-1]}")


# LISTS #
# 
# RANGE EXAMPLE: start = 0; l = [num for num in range(start, 4)]; print(f"l-list: {l}"); print(f"l-length: {len(l)}")
# SPLIT(L <- S): string_list = formatted.split(' ')
# FOR LOOP: for_loop = [cubed(i)+1 for i in range(0, 5)]
# MAP, FILTER COMBO: filtered_map = [num*num for num in range(0, 20) if num % 2 == 0]
# REDUCE W LAMBDA: reduced = reduce(lambda acc, curr: acc + curr, a)
# LIST CONSTRUCTOR W LAMBDA: list_lambda = list(filter(lambda x: x % 5  == 0, range(2, 25+1))); print(list_lambda)
# REVERSE LIST: print(f"example of reversing a list: {a[::-1]}")
# INDEX OF: val_list = list(my_dict.values()).index("dog")
 

# DICTIONARIES #
# 
# FLOAT FORMAT & KEY ASSIGNMENT: result = {}; line = 3; score = "{:10.6f}".format(12/14); result[str(line)] = score; print(f"KEY ASSIGNMENT: {result}")
# UPDATE: dictionary = {k1: v1, k2:v2}.update({k1, v1, k3, v3})
# CHECK IF VAL IN DICT: if word in dicttionary:
# SET KEY,VAL: word_count_dict[word] = 0
# INCREMENT VAL: word_count_dict[word] += 1
# COPY DICT: copy_dictionary = dicttionary.copy()
# DELETE KEY,VAL FROM COPY: del copy_dictionary[k]
# SORTING AND REVERSING: sorted_dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

# MISC #
# 
# DEFINE HELPER METHOD: def helper(arg1, arg2...):




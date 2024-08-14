# def create_phone_number(n):
#     digits = "(" + ''.join(str(e) for e in n[0:3]) + ")" + " " \
#         + ''.join(str(f) for f in n[3:6]) + "-" + ''.join(str(g)\
#         for g in n[6:10])
#     return(digits)

# def meeting(s):
#     unsorted_names = []
#     fully_sorted_names = []
    
#     names_separated = s.split(";")
#     for names in names_separated:
#         names_further_separated = names.split(":")
#         reversed_names = names_further_separated[::-1]
#         combined_names = ", ".join(reversed_names)
#         uppercase_names = combined_names.upper()
#         unsorted_names.append(uppercase_names)
#     sorted_names = sorted(unsorted_names)
#     for names_sorted in sorted_names:
#         fully_sorted_names.append("(")
#         fully_sorted_names.append(names_sorted)
#         fully_sorted_names.append(")")
#     print(''.join(fully_sorted_names))

# meeting("Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;\
# Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill")

# import string


# def pig_it(text):
#     words = text.split(" ")
#     pig_words = []
#     for word in words:
#         if word in string.punctuation:
#             pig_word = word
#             pig_words.append(pig_word)
#         else:
#             pig_word = word[1:len(word)] + word[0] + "ay"
#             pig_words.append(pig_word)
#     print(" ".join(pig_words))
# pig_it("This Is A Test")

# def two_sum(numbers, target):
#     for i in range(0, len(numbers)):
#         for j in range(0, len(numbers)):
#             if i != j:
#                 if numbers[i] + numbers[j] == target:
#                     print([i,j])
# two_sum([1, 2, 3], 4)

# def sort_array(source_array):
#     sorted_array = []
#     unordered_odds_dict = {

#     }
#     for number in source_array:
#         if number % 2 == 0:
#             even_index = source_array.index(number)
#             sorted_array.insert(even_index, number)
#         else:
#             odd_index = source_array.index(number)
#             sorted_array.insert(odd_index, number)
#             unordered_odds_dict.update({odd_index:number})
#     print(unordered_odds_dict)
#     print(sorted_array)
#
# sort_array([5, 3, 1, 8, 0])


# def delete_nth(order,max_e):
#     new_list = []
#     for i in order:
#         if new_list.count(i) < max_e:
#             new_list.append(i)
#     print(new_list)

# delete_nth([1, 2, 3, 1, 1], 2)


# def find_nb(m):
#     count = 0
#     i = 1
#     while count < m:
#         count += i ** 3
#         if count == m:
#             print(i)
#         i += 1
#     print("-1")

# find_nb(1071225)


# def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
#     for number in range(a, b + 1):
#         for digit in range(0, len(number)):
            
#     #return []


# """
# Given the triangle of consecutive odd numbers:

#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

# 1 -->  1
# 2 --> 3 + 5 = 8
# """

# def row_sum_odd_numbers(n):
#     num = 1
#     count = 1
#     tick = n
#     total = 0
#     odds = []
#     value = 0

#     for i in range(n):
#         total += tick
#         tick -= 1

#     while count <= total:
#         odds.append(num)
#         num += 2
#         count += 1

#     nth_row = odds[len(odds)-n::]
#     for j in nth_row:
#         value += j

#     print(value)

# row_sum_odd_numbers(5)



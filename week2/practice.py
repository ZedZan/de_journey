# def filter_by_country(dict_list, country_name ) -> list[dict] :
#     list_country =[]
#     for r in dict_list:
#         if r["country"] == country_name :
#             list_country.append(r)
#     return list_country


# data = [
#     {"name": "Alice", "country": "France"},
#     {"name": "Bob", "country": "UK"},
#     {"name": "Carol", "country": "France"},
# ]

# result = filter_by_country(data, "France")
# print(result)


# def calculate_stats(numbers: list[float]):
#     return {"min" : min(numbers),"max": max(numbers),"total": sum(numbers), "average":(sum(numbers)/ len(numbers))}

# print(calculate_stats([10, 20, 30, 40]))


# def count_by_category(records: list[dict]):
#     results = {}
#     for r in records:
#         category = r["category"]
#         if category in results:
#             results[category] += 1
#         else:
#             results[category] = 1
#     return results


# records = [
#     {"name": "iPhone", "category": "Electronics"},
#     {"name": "Samsung", "category": "Electronics"},
#     {"name": "Nike", "category": "Clothing"},
# ]
# print(count_by_category(records))
# # → {"Electronics": 2, "Clothing": 1}


# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False


# def sum_list(numbers):
#     no = 0
#     for n in numbers:
#         no += n
#     return no


# def reverse_string(s):
#     reverse = []
#     for r in s:
#         reverse.insert(0, r)
#     return "".join(reverse)

# def count_vowels(s):
#     vowels =["a", "e", "i", "o" , "u"]
#     counting = 0
#     for r in s:
#         if r in vowels:
#             counting += 1
#     return counting

# def flattten(nested):
#     flattened = []
#     for outer_list in nested :
#         for inner_list in outer_list:
#              flattened.append(inner_list)
#     return flattened

# def most_frequent(lst):
#     counting = {}
#     for l in lst:
#         if l in counting:
#             counting[l] +=1
#         else:
#             counting[l] = 1
#     return max(counting, key=counting.get)


# def celsius_to_fahrenheit(c):
#     return (c * 9/5) +32

# def remove_duplicates(lst):
#     dup = []
#     for l in lst:
#         if l not in dup :
#             dup.append(l)
#     return dup

# def word_count(sentence):
#     counting ={}
#     split_sentence = sentence.split()
#     for r in split_sentence:
#         if r in counting:
#             counting[r] +=1
#         else :
#             counting[r] = 1
#     return counting


# def is_palindrome(s) :
#     reversed = s[::-1]
#     if s == reversed:
#         return True
#     else:
#         return False


# def get_evens(numbers):
#     even =[]
#     for i in numbers:
#         if i %2 == 0:
#             even.append(i)
#     return even

# def merge_dicts(d1, d2) :
#     merged = {}
#     merged = d1.copy()
#     for key, value in d2.items():
#         if key in merged:
#             merged[key] = merged.get(key, 0) +value
#         else:
#             merged[key] = value
#     return merged

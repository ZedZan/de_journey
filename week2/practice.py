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

# def capitalize_words(sentence):
#     return " ".join(w.capitalize() for w in sentence.split())


# def safe_divide(a, b):
#     if b == 0:
#         return 0
#     else:
#         return a/b


# def chunk_list(lst, size) :
#     chunk = []
#     for l in range(0, len(lst), size):
#         chunk.append(lst[l:l+size])
#     return chunk


# def sum_digits(n) :
#     s= str(n)
#     l = 0
#     for i in range(len(s)):
#         l += int(s[i])
#     return l

# def filter_above(numbers, threshold):
#     filtred = []
#     for i in range(len(numbers)) :
#         if numbers[i] > threshold:
#             filtred.append(numbers[i])
#     return filtred


# def zip_dicts(key, values):
#     ziped = {}
#     for i in range(len(key)):
#         ziped[key[i]] = values[i]
#     return ziped
# from math import sqrt
# def is_prime(n) :
#     if n <= 1:
#         return False
#     elif n<=3 :
#         return True
#     elif n%2 ==0  or n%3 == 0:
#         return False

#     i= 2
#     while i<= sqrt(n):
#         if n%i == 0:
#             return False
#         i +=1
    
#     return True


# def flatten_dict(d):
#     flat ={}
#     for key, value in d.items():
#         if isinstance(value, dict):
#             for inner_key, inner_value in value.items():
#                 flat[inner_key] = inner_value
#         else:
#             flat[key] = value


#     return flat

# def running_average(numbers):
#     lst = []
#     runnig_sum = 0
#     count = 0
#     for i in numbers:
#         runnig_sum += i
#         count +=1
#         average = runnig_sum / count
#         lst.append(average)
#     return lst

# def clamp(n, min_val, max_val):
#     if n < min_val:
#         n= min_val
#     if n> max_val:
#         n= max_val
#     return n

# def unique_chars(s):
#     u = set()
#     for i in s:
#         u.add(i)
#     return len(u)

# def rotate_list(lst, n):
#     if not lst:
#         return lst

#     n = n % len(lst)   # normalize n
#     return lst[-n:] + lst[:-n]
# from datetime import datetime
# class Loggedblock:
#     def __init__(self, name):
#         self.name = name
    
#     def __enter__(self):
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         with open("context.log", "a") as f:
#             f.write(f"[ENTER] {self.name} - {timestamp} \n")
#         return self
#     def __exit__(self, exc_type, exc, tb):
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         with open("context.log", "a") as f:
#             f.write(f"[EXIT] {self.name} - {timestamp} \n")
#         return False

# def group_by(data, key):
#     result = {}
#     for item in data:
#         group_value =  item[key]
#         if group_value not in result :
#             result[group_value] = []
#         result[group_value].append(item)
#     return result
# import time
# def timed(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} took {(end - start):.2f} seconds")
#         return result
#     return wrapper
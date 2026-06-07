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
# import time 
# def retry(max_attempts, delay):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for attempt in range(max_attempts):
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception:
#                     if attempt == max_attempts -1 :
#                         raise
#                     time.sleep(delay)
#         return wrapper
#     return decorator 


# import time

# def retry(func, max_attempts, delay):
#     for attempt in range(max_attempts):
#         try:
#             return func()
#         except Exception:
#             if attempt == max_attempts-1:
#                 raise
#             time.sleep(delay)

# def flatten(nested):
#     flat = []
#     for item in nested :
#         if isinstance(item, list):
#             for inner_item in item:
#                 flat.append(inner_item)
#         else:
#             flat.append(item)

# def merge_dicts(base, override):
#     merged = base.copy()
#     merged.update(override)
#     return merged

# def filtred(records):
#     filtre = {}
#     for r in records :
#         if r["name"] != None and r["sales"] != None:
#             filtre[r["name"]] = filtre.get(r["name"], 0) + r["sales"]
#     return filtre



# def sales(records):
#     result = {}
#     for r in records :
#         if r["amount"] != None:
#             customer = r["customer"]
#             month = r["month"]
#             amount = r["amount"]
#             if customer not in result:
#                 result[customer] = {}
#             if month not in result[customer]:
#                 result[customer][month] = 0.0
#             result[customer][month] += amount
#     return result

# def validated(records, required_fields):
#     result = {"valid": [], "invalid" : []}
#     for r in records:
#         missing = []
#         for field in required_fields:
#             if r.get(field) is None:
#                 missing.append(field)
        
#         if missing:
#             bad = r.copy()
#             bad["missing_fields"] = missing
#             result["invalid"].append(bad)
#         else:
#             result["valid"].append(r)
#     return result
# def tasks(tasks):
#     in_degree = {}
#     deps_by_name = {}
#     for task in tasks:
#         name = task["name"]
#         deps = task["depends_on"]
#         deps_by_name[name] = deps
#         in_degree[name] = len(deps)
    
#     queue = [name for name, deg in in_degree.items() if deg == 0]

#     result = []
#     while queue :
#         current = queue.pop(0)
#         result.append(current)

#         for name, deps in deps_by_name.items():
#             if current in deps :
#                 in_degree[name] -= 1
#                 if in_degree[name] == 0:
#                     queue.append(name)
    
#     return result 


# def validated(records, rules):
#     result = {"valid": [], "invalid" : []}
#     for r in records:
#         failed = []
#         for i, rule in enumerate(rules):
#             if rule(r) is False:
#                 failed.append(i)
#         if not failed:
#             result["valid"].append(r)
#         else:
#             new_record = r.copy()
#             new_record["failed_rules"] = failed
#             result["invalid"].append(new_record)
    
#     return result 
# from string import Formatter
# def rendered(template, params):
#     place_holder = []
#     for _, field_name, _, _ in Formatter().parse(template):
#         if field_name is not None :
#             place_holder.append(field_name)
    
#     for name in place_holder:
#         if name  not in params:
#             raise ValueError(f"Missing key: {name}")
        
#     return template.format(**params)

# def versioning(records):
#     latest ={}
#     for r in records:
#         rid = r["id"]
#         if rid not in latest :
#             latest[rid] = r
#         else:
#             if r["version"] > latest[rid]["version"]:
#                 latest[rid] = r
#     return list(latest.values())

# def stats(num) -> dict:
#     values = [n for n in num if n is not None]
#     count = len(values)
#     mean = sum(values) / count
#     minimum = min(values)
#     maximum = max(values)

#     squared_diffs =[(x - mean) **2 for x in values]
#     variance = sum(squared_diffs) / count
#     std = variance ** 0.5
#     std = round(std ,2)

#     return {
#         "count" : count,
#         "mean" : mean,
#         "min" : minimum,
#         "max" : maximum,
#         "std" : std
#     }

# def run_pipeline(steps):
#     for step in steps:
#         try:
#             step()
#         except Exception as e:
#             return {
#                 "status" : "failed",
#                 "step" : step.__name__,
#                 "error" : str(e)
#             }
#     return {"status" : "success"}

# def grouping(records, group):
#     groups = {}
#     for r in records:
#         key = tuple(r[col] for col in group)
#         groups[key] = groups.get(key, 0) +1
#     return groups

# def parse_query(query):
#     tokens = query.split()
#     result = {
#         "select" : None,
#         "from" : None,
#         "where" : None,
#         "order_by" : None
#     }

#     try :
#         select_idx = tokens.index("SELECT")
#         from_idx = tokens.index("FROM")
#     except ValueError:
#         return result

#     result["select"] = tokens[select_idx +1 : from_idx]
#     result["select"] = [col.strip(",") for col in result["select"]]

#     result["from"] = tokens[from_idx +1]

#     if "WHERE" in tokens :
#         where_idx = tokens.index("WHERE")
#         end = tokens.index("ORDER") if "ORDER" in tokens else len(tokens)
#         result["where"] = " ".join(tokens[where_idx +1 : end])
    
#     if "ORDER" in tokens:
#         order_idx = tokens.index("ORDER")
#         result["order_by"] = " ".join(tokens[order_idx +2 :])
    
#     return result
# def group_by_column(records, column):
#     result = {}

#     for r in records:
#         key = r[column]
#         if key not in result:
#           result[key] = []
#         result[key].append(r)
#     return result

# def list_files(fs, prefix=""):
#     paths = []

#     for name, value in fs.items():
#         full_path = f"{prefix}/{name}" if prefix else name

#         if isinstance(value, dict):
#             # Folder → go deeper
#             paths.extend(list_files(value, full_path))
#         else:
#             # File → add full path
#             paths.append(full_path)

#     return paths      

# def has_cycle(dag):
#     visited = set()
#     in_stack = set()   # nodes currently in recursion stack

#     def dfs(node):
#         if node in in_stack:
#             return True   # cycle found

#         if node in visited:
#             return False  # already processed safely

#         visited.add(node)
#         in_stack.add(node)

#         for dep in dag.get(node, []):
#             if dfs(dep):
#                 return True

#         in_stack.remove(node)
#         return False

#     # Check every node in case the graph is disconnected
#     for node in dag:
#         if dfs(node):
#             return True

#     return False

# def read_csv(filepath):
#     with open(filepath, "r") as f:
#         lines = f.read().splitlines()

#     header = lines[0].split(",")

#     data = []
#     for line in lines[1:]:
#         values = line.split(",")
#         row_dict = dict(zip(header, values))
#         data.append(row_dict)
    
#     return data

# def write_csv(filepath, data):
#     if not data:
#         return  # nothing to write

#     # Extract header from the keys of the first row
#     header = list(data[0].keys())

#     with open(filepath, "w") as f:
#         # Write header row
#         f.write(",".join(header) + "\n")

#         # Write each data row
#         for row in data:
#             values = [str(row[key]) for key in header]
#             f.write(",".join(values) + "\n")
# import json
# def save_json(filepath, data):
#     with open(filepath, "w") as f :
#         json.dump(data, f, indent=2)

# def load_json(filepath):
#     with open(filepath, "r") as f:
#        return json.load(f)

def extract_fields(data, fields):
    result = []
    for row in data:
        new_row = {}
        for field in fields :
            new_row[field] = row[field]
        result.append(new_row)
    return result
from datetime import datetime
def filter_by_date_range(records, start, end):
    result = []
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")
    for record in records:
        record_date = datetime.strptime(record["date"], "%Y-%m-%d")
        if start_date <= record_date<= end_date:
            result.append(record)
    return result
import json
def load_json(filepath):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("Invalid Json")
    except Exception as e :
        print(f"error :  {e}")

# def list_conprehension(matches):
#     result1 = [match["champion"] for match in matches]
#     result2 = [match["match_id"] for match in matches if match["win"] == True]
#     result3 = [match["kill"] * 2 for match in matches if match["kill"] > 3]

def process_matches(filepath):
    data = load_json(filepath)
    if data is None:
        return []
    new_data = [value for value in data if value["win"] == True]
    return [{"match_id" : val["match_id"], "champion" : val["champion"]} for val in new_data]

# with kda_calculated AS(
#     select champion, (kills + assists) / deaths AS KDA
#     from matches 
# ),
# KDA_positive AS(
#     select *
#     from kda_calculated 
#     where KDA > 3
# )

# select champion, avg(KDA) as AVG(KDA) from KDA_positive 
# group BY champion 
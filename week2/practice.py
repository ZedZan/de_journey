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


def count_by_category(records: list[dict]):
    results = {}
    for r in records:
        category = r["category"]
        if category in results:
            results[category] += 1
        else:
            results[category] = 1
    return results

records = [
    {"name": "iPhone", "category": "Electronics"},
    {"name": "Samsung", "category": "Electronics"},
    {"name": "Nike", "category": "Clothing"},
]
print(count_by_category(records))
# → {"Electronics": 2, "Clothing": 1}

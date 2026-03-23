def filter_by_country(dict_list, country_name ) -> list[dict] :
    list_country =[]
    for r in dict_list:
        if r["country"] == country_name :
            list_country.append(r)
    return list_country


data = [
    {"name": "Alice", "country": "France"},
    {"name": "Bob", "country": "UK"},
    {"name": "Carol", "country": "France"},
]

result = filter_by_country(data, "France")
print(result)
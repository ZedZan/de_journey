import json
import sys
def read_csv(filepath):
    with open(filepath, "r") as f:
        lines = f.read().splitlines()

    header = lines[0].split(",")

    data = []
    for line in lines[1:]:
        values = line.split(",")
        row_dict = dict(zip(header, values))
        data.append(row_dict)
    
    return data

def save_json(filepath, data):
    with open(filepath, "w") as f :
        json.dump(data, f, indent=2)

def match_processor(filepath):
    print(f"Starting with filepath: {filepath}")
    try:
        data = read_csv(filepath)
        print(f"Loaded {len(data)} records")
    except FileNotFoundError:
        return "File not found"
    filtered_matches = [value for value in data if (int(value["kills"]) > 3 and value["win"] == "True")]
    new_data = [{"match_id"  :val["match_id"] , "champion" :val["champion"] , "kills" : val["kills"]} for val in filtered_matches]
    try:
        save_json("data/output.json", new_data)
    except json.JSONDecodeError:
        return "invalid json"
    for match in new_data:
        print(f"current match id  passed the filter {match['match_id']}")
    
    print(f"Total processed: {len(data)}, Passed filter: {len(new_data)}")
    
  

if __name__ == "__main__":
    filepath = sys.argv[1]
    match_processor(filepath)



        
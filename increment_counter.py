import json

file_path = "counter.json"

with open(file_path, "r") as f:
    data = json.load(f)

# increment counter
data["message"] = str(int(data["message"]) + 1)

with open(file_path, "w") as f:
    json.dump(data, f)

import json

print(json.loads('{"name": "Subbu", "age": 25, "city": "Hyderabad"}'))
print(json.dumps({"name": "Subbu", "age": 25, "city": "Hyderabad"}))
print(json.dumps(["Subbu", "Hari", "Raju", "Ravi"]))

json_string = json.dumps(["Subbu", "Hari", "Raju", "Ravi"])
print(json.loads(json_string))

json_str = json.dumps({"name": "Arjun", "age": 25, "city": "Hyderabad"})
print(json.loads(json_str))

json_str = json.dump(["Subbu", "Hari", "Raju", "Ravi"], open("names.json", "w", encoding="utf-8" , errors="ignore", newline=None, closefd=True))
print(json.load(open("names.json")))
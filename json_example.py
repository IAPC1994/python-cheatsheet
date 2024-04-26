import json

# some JSON
x = '{ "name": "Ivan", "age": 30, "city": "Melbourne"}'

y = json.loads(x)

print(y["city"])

# a python object (dict)
z = { "name": "Ivan", "age": 30, "city": "Melbourne"}

u = json.dumps(z)
print(u)

obj = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# print(json.dumps(obj, indent=4, separators=(". ", " = ")))
print(json.dumps(obj, indent=4, sort_keys=True))
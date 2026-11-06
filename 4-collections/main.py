# Lists (ordered, mutable)

fruits = ["apple", "banana", "cherry"]

fruits[0]               # "apple"
fruits[-1]              # "cherry"
fruits.append("date")   # ["apple", "banana", "cherry", "date"]
fruits.remove("banana") # ["apple", "cherry", "date"]
len(fruits)             # 3
fruits[1:3]             # ["cherry", "date"]

# Tuples (ordered, immutable)
point = (3,4)
x,y = point # unpacking

# Dictionaries (key value pairs)

person = {"name": "Alice", "age": 30}

person["name"]              # Alice
person["city"] = "NYC"      # Add key
person.get("email", "N/A")  # Safe access with default

# Sets (unique items, unordered)

nums = {1,2,3,4,1,2}    # {1,2,3,4}
nums.add(5)             # {1,2,3,4,5}







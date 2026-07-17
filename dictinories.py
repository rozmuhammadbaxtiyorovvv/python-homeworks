capitals = {
    "Uzbekistan": "Tashkent",
    "USA": "Washington, D.C.",
    "South Korea": "Seoul",
    "Japan": "Tokyo",
    "Russia": "Moscow",
    "Germany": "Berlin"
}

print(f"Uzbekistan's capital is {capitals.get("Uzbekistan")}")  
print(f"USA's capital is {capitals.get("USA")}")  


capitals.update({"France": "Paris"})
capitals.update({"Uzbekistan": "Tashkent City"})

capitals.pop("Germany")

capitals.popitem()

keys = capitals.keys()
values = capitals.values()


print(f"Keys: {keys}")
print(f"Values: {values}")

print(capitals.get("Germany") or "Germany isnt in the dictionary")
print(capitals.get("France") or "France isnt in the dictionary")
print(capitals)
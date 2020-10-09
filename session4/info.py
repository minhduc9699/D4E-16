# person = ["Đức", 96, 175, "Sơn La", False, "dev"]

person = {
    "name": "Đức",
    "yob": 96, 
    "job": "dev",
    "bmi": {
        "weight": 70,
        "height": 175,
    },
}
print("name" in person) # CHECK KEY IN DICT
person["hair"] = "short" # CREATE
person["name"] = "cứĐ" # UPDATE
del person["bmi"] # DELETE
print(person)
# bmi = person["bmi"]
name = person["job"] # READ
for key in person:
    print(key, person[key])

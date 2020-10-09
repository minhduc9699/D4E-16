dictionary = {
    "hc": "học",
    "any": "anh người iu",
    "hk": "không",
}
while True:
    for key in dictionary:
        print(key, end="\t")
    print()
    input_key = input("your code?")
    if input_key in dictionary:
        print("it means:", dictionary[input_key])
    else:
        choice = input("Not found your word, wanna contrib? (Y/N) ").upper()
        if choice == "Y":
            dictionary[input_key] = input("Enter it meaning ")
        else:
            print("bye")
            break
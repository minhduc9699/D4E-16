mon_an1 = 'phở'
mon_an2 = 'cơm'
mon_an3 = 'bún'
mon_an3 = 'thịt chó'

# List
foods = ['phở', 'cơm', 'bún', 'thịt chó', 'bún đậu', 'phở']

# a = input('Enter new item')
foods.append('anything') # CREATE
foods[3] = 'thịt bò' # UPDATE
foods.remove('phở') # DELETE by value
foods.pop(3) # DELETE by index
removed_item = foods.pop(3)  # DELETE by index and save to variable
print(foods[0])# READ ONE
for i in range(len(foods)): # READ ALL
    print(i, foods[i])
# find index of item
index = foods.index('phở')
# check if item in list
result = 'phở' in foods
# print('_______')
# for food in foods:
#     print(i)

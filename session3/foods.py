mon_an1 = 'phở'
mon_an2 = 'cơm'
mon_an3 = 'bún'
mon_an3 = 'thịt chó'

# List
foods = ['phở', 'cơm', 'bún', 'thịt chó', 'bún đậu', 'phở']

# a = input('Enter new item')
# foods.append(a) # CREATE

mon_thit_cho = foods[3]

foods[3] = 'thịt bò' # UPDATE
print('->>',mon_thit_cho)
print(len(foods))
# foods.remove('phở') # DELETE by value
# foods.pop(3) # DELETE by index
# removed_item = foods.pop(3)  # DELETE by index and save to variable
# print('removed item', removed_item)
index = foods.index('bún đậu')
print(foods[index])
for i in range(len(foods)):
    print(i, foods[i])
# print('_______')
# for food in foods:
#     print(i)

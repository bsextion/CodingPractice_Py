# #Updating entries
# phone_book = {"Batman": 468426,
#               "Cersei": 237734,
#               "Ghostbusters": 44678}
# phone_book["Batman"] = 2

# #deleting
# del phone_book["Cersei"]
# print(phone_book)

# #Check existence
# print("Batman" in phone_book)


#update the contents
# phone_book = {"Batman": 468426,
#               "Cersei": 237734,
#               "Ghostbusters": 44678}

# second_phone_book = {"Catwoman": 67423, "Jaime": 237734, "Godzilla": 37623}

# # Add secondphone_book to phone_book
# phone_book.update(second_phone_book)
# print(phone_book)


houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
new_houses = {n**2: house + "!" for (n, house) in houses.items()}
# print(houses)
# print(new_houses)
popped = new_houses.popitem()
print(popped)
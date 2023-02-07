person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": ["Fido", "Bruce"], "cat": "Sox"}
"""
print(person)

# print out the name of the spouse
print(person["spouse"])

# print our the name of the second child
print(f"the name of the second child is: {person['children'][1]}")


# print out the name of the cat
print(person["pets"]["cat"])

# use a loop to print out the names of each child
for x in person["children"]:
    print(x)
"""
# use a loop to print out the pets in the following format:
# the type of pet is: dog and the name of the pet is: Fido
pet_dict = person["pets"]
for key, value in pet_dict.items():
    print(f"the type of pet is: {key} and the name of the pet is: {value[0]}")

# the result will be Bruce and o for cat's name because this dog's name is a list
# and cat's name is a string.
# we will need another coding thingy to resolve this

# string = "Sox"
# print(string)

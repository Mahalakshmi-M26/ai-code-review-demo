from os import name
from tkinter.font import names


def get_pet_names(pets):
    names = []
    
    for pet in pets:
        name = pet.get("name")
        if name is not None:
            names.append(name)

    for pet in pets:
        print("processing pet again")

    return names

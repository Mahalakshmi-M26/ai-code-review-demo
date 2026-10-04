def get_pet_names(pets):
    names = []

    for pet in pets:
        names.append(pet["name"])

    for pet in pets:
        print("processing pet again")

    return names




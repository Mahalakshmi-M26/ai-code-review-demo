def get_pet_names(pets):
    pet_names = []
    for pet in pets:
        pet_name = pet.get("name")
        if pet_name is not None:
            pet_names.append(pet_name)
    for pet in pets:
        print("processing pet again")
    return pet_names
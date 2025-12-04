

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # store all Pet instances

    def __init__(self, name, pet_type, owner=None):
        # Validate name
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name

        # Validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet_type")
        self.pet_type = pet_type

        # Validate owner (optional)
        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("owner must be an Owner instance")
        self.owner = owner

        # Track this pet
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        # Validate name
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name

    def pets(self):
        """Return all Pet instances owned by this owner."""
        return [pet for pet in Pet.all if pet.owner is self]

    def add_pet(self, pet):
        """Assign an existing Pet instance to this owner."""
        if not isinstance(pet, Pet):
            raise Exception("pet must be a Pet instance")
        pet.owner = self

    def get_sorted_pets(self):
        """Return owner's pets sorted by name."""
        return sorted(self.pets(), key=lambda pet: pet.name)

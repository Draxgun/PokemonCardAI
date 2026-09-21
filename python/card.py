VALID_TYPES = {
    "Colorless",
    "Darkness",
    "Dragon",
    "Fairy",
    "Fighting",
    "Fire",
    "Grass",
    "Lightning",
    "Metal",
    "Psychic",
    "Water"
    }

class Card:

    def __init__(self, id, name, set, number, rarity, hp, types):

        if not id or not isinstance(id, str):
            raise ValueError("Card ID cannot be empty and must be a string")
        

        if not set or not isinstance(set, str):
            raise ValueError("Card set cannot be empty and must be a string")

        if not name or not isinstance(name, str):
            raise ValueError("Card name cannot be empty and must be a string")

        if not number or not isinstance(number, str):
            raise ValueError("Card number cannot be empty and must be a string")

        if not rarity or not isinstance(rarity, str):
            raise ValueError("Card rarity cannot be empty and must be a string")
        
        if not isinstance(hp, int):
            raise ValueError("HP must be an integer")
        
        if hp <= 0:
            raise ValueError("HP must be greater than 0")

        if not isinstance(types, list):
            raise ValueError("Card types must be a list")

        if  len(types) == 0:
            raise ValueError("Card types cannot be empty")

        for t in types:
            if not isinstance(t, str):
                raise ValueError("Card type must be a string")
            if not t:
                raise ValueError("Card type cannot be empty")
            if t not in VALID_TYPES:
                raise ValueError(f"Card type '{t}' is not valid")
            if (types.count(t) > 1):
                raise ValueError(f"Card type '{t}' is duplicated")

        self.id = id
        self.name = name
        self.set = set
        self.number = number
        self.rarity = rarity
        self.hp = hp
        self.types = types
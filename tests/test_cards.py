import pytest
from python.card import Card;

def test_create_valid_card():
    card = Card(
        "base1-001",
        "Bulbasaur",
        "Base Set",
        "001",
        "Common",
        40,
        ["Grass"]
    )

    assert card.id == "base1-001"
    assert card.name == "Bulbasaur"
    assert card.set == "Base Set"
    assert card.number == "001"
    assert card.rarity == "Common"
    assert card.hp == 40
    assert card.types == ["Grass"]


def test_empty_card_id():
    with pytest.raises(ValueError):
        Card("", "Bulbasaur", "Base Set", "001", "Common", 40, ["Grass"])


def test_invalid_card_id_type():
    with pytest.raises(ValueError):
        Card(123, "Bulbasaur", "Base Set", "001", "Common", 40, ["Grass"])


def test_empty_card_name():
    with pytest.raises(ValueError):
        Card("base1-001", "", "Base Set", "001", "Common", 40, ["Grass"])


def test_invalid_card_name_type():
    with pytest.raises(ValueError):
        Card("base1-001", 123, "Base Set", "001", "Common", 40, ["Grass"])


def test_empty_card_set():
    with pytest.raises(ValueError):
        Card("base1-001", "Bulbasaur", "", "001", "Common", 40, ["Grass"])


def test_invalid_card_set_type():
    with pytest.raises(ValueError):
        Card("base1-001", "Bulbasaur", 123, "001", "Common", 40, ["Grass"])


def test_empty_card_number():
    with pytest.raises(ValueError):
        Card("base1-001", "Bulbasaur", "Base Set", "", "Common", 40, ["Grass"])


def test_invalid_card_number_type():
    with pytest.raises(ValueError):
        Card("base1-001", "Bulbasaur", "Base Set", 1, "Common", 40, ["Grass"])


def test_empty_card_rarity():
    with pytest.raises(ValueError):
        Card("base1-001", "Bulbasaur", "Base Set", "001", "", 40, ["Grass"])


def test_invalid_card_rarity_type():
    with pytest.raises(ValueError):
        Card("base1-001", "Bulbasaur", "Base Set", "001", 123, 40, ["Grass"])


def test_invalid_hp_type():
    with pytest.raises(ValueError):
        Card("base1-001", "Bulbasaur", "Base Set", "001", "Common", "40", ["Grass"])


def test_zero_hp():
    with pytest.raises(ValueError):
        Card("base1-001", "Bulbasaur", "Base Set", "001", "Common", 0, ["Grass"])


def test_negative_hp():
    with pytest.raises(ValueError):
        Card("base1-001", "Bulbasaur", "Base Set", "001", "Common", -10, ["Grass"])


def test_types_not_list():
    with pytest.raises(ValueError):
        Card("base1-001", "Bulbasaur", "Base Set", "001", "Common", 40, "Grass")


def test_empty_types():
    with pytest.raises(ValueError):
        Card("base1-001", "Bulbasaur", "Base Set", "001", "Common", 40, [])


def test_type_not_string():
    with pytest.raises(ValueError):
        Card("base1-001", "Bulbasaur", "Base Set", "001", "Common", 40, ["Grass", 123])


def test_empty_type():
    with pytest.raises(ValueError):
        Card("base1-001", "Bulbasaur", "Base Set", "001", "Common", 40, [""])


def test_invalid_type():
    with pytest.raises(ValueError):
        Card("base1-001", "Bulbasaur", "Base Set", "001", "Common", 40, ["Ice"])


def test_duplicate_type():
    with pytest.raises(ValueError):
        Card("base1-001", "Bulbasaur", "Base Set", "001", "Common", 40, ["Grass", "Grass"])


def test_multiple_valid_types():
    card = Card(
        "base1-004",
        "Charizard",
        "Base Set",
        "004",
        "Rare Holo",
        120,
        ["Fire", "Colorless"]
    )

    assert card.types == ["Fire", "Colorless"]
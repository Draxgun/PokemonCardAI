import json
from pathlib import Path


def load_cards(path):
    with path.open("r", encoding="utf-8") as f:
        cards = json.load(f)
    return cards

def validate_cards(cards):
    return 

def generate_report():
    return 

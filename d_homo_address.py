import re
import random
import csv

csv_file = "addresses.csv"
txt_file = "addresses_v.txt"


def Extract_file(csv_file, txt_file):
    """
    Extract value
    """
    with open(csv_file, "r", newline='', encoding="utf-8") as csv_infile:
        csv_reader = csv.reader(csv_infile)
        
        with open(txt_file, "w", encoding="utf-8") as txt_outfile:
            for row in csv_reader:
                if row:  
                    txt_outfile.write(row[0] + "\n") 

# Llama a la función para realizar la extracción
Extract_file(csv_file, txt_file)

homo_address = {
    "carrera": ["cra", "carr", "kra", "transversal", "calle", "carera", "crr"],
    "calle": ["kll", "Call", "Cal", "kalle", "cale", "tranversal", "carrera"],
    "carr": ["cra", "carrera", "kra", "transversal", "calle", "carera", "carr"],
    "#": ["Nro", "numero", "nùmero", "num", "numb"],
    "num": ["Nro", "numero", "nùmero", "#", "numb"],
}


def choose_homo(char):
    """
    Returns a list of homonyms for the guiven character,
    or the character itself if there are no homonyms.
    """
    return homo_address.get(char, [char])
   


def generate_combinations(address):
    """
    Finds the character in the address that should be replaced by homonyms.
    """
    pattern = re.compile(r"[ael357#]")
    matches = pattern.findall(address)
    combinations = [address]

    for match in matches:
        new_combinations = []
        for combination in combinations:
            for char in match:
                # Generate all possible homonyms for the current character.
                for homo in choose_homo(char):
                    new_combinations.append(combination.replace(char, homo))
            new_combinations =list(set(new_combinations))
        combinations = new_combinations

    return combinations


def generate_all_combinations(addresses):
    result = []
    for address in addresses:
        # Generate all possible combinations combinatios for each address in teh list.
        combinations = generate_combinations(address)
        result.extend(combinations)

    return result

addresses= [
    "calle 53 # 55 a 67",
    "calle 44 # 89 b 44",
    "carrera 50 # 38 a 39",
    "carrera 102 bb num 49 a 30",
    "carrera 99 a # 48 b 29",
    "1600 Amphitheatre Parkway",
]

all_combinations = generate_all_combinations(addresses)

# print all resulting combinations.
for combo in all_combinations:
    print(combo)

import re
import csv
from itertools import product

csv_file = "addresses.csv"
txt_file = "addresses_h.txt"

synonyms = {
    "Cr.": ["Carrera", "Crr", "kra"],
    "Cl..": ["Cda", "Cll.", "Cl.", "calle"],
    "Calle":["Cl.", "Cda", "Cll."],
    "Diag":["Diagonal", "Diag."],
    "#": ["Nro", "numero", "número", "num"],
    "num": ["Nro","numero", "nùmero", "#"],
}

def Extract_addresses(csv_file):
    """
    Extract value
    """
    h_addresses = []
    with open(csv_file, "r", newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if "address" in row:
                h_addresses.append(row["address"])
    return h_addresses
        
def choose_homo(char):
    """
    Returns a list of homonyms for the guiven character,
    or the character itself if there are no homonyms.
    """
    return synonyms.get(char, [char])
   
def generate_synonyms_combinations(address):
    """
    Finds the character in the address that should be replaced by homonyms.
    """
    homonym_combination= [address]

    for word, homonyms in synonyms.items():
        for homonym in homonyms:
            pattern = re.compile(rf"\b{word}\b", flags=re.IGNORECASE)
            synonym_address = re.sub(pattern, homonym, address)
            homonym_combination.append(synonym_address)   

    return homonym_combination       

def generate_all_combinations(addresses):
    result = []
    for address in addresses:
        # Generate all possible combinations combinatios for each address in teh list.
        combinations = generate_synonyms_combinations(address)
        result.extend(combinations)

    return result

def homo_address():
  addresses= Extract_addresses(csv_file)
  all_combinations = generate_all_combinations(addresses)

   # print all resulting combinations.
  with open(txt_file, "w", encoding="UTF-8") as addresses_v:
    for combo in all_combinations[1:]:
       addresses_v.write(combo + "\n")

print ("Process completed successfully")
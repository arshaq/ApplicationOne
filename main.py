import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def findMeaning(searchTerm):
    searchTerm = searchTerm.lower()
    if searchTerm in data:
        return data[searchTerm]
    elif searchTerm.capitalize() in data:           # For proper nouns
        return data[searchTerm.capitalize()]
    elif searchTerm.upper() in data:                # For acronyms and abbreviations
        return data[searchTerm.upper()]
    else:
        closest_match = get_close_matches(searchTerm, data.keys(), n=1)
        if closest_match:
            answer = input("No word like " + searchTerm + ". Did you mean " + closest_match[0] + "? (Type Y/N): ")
            if answer.upper() == "Y":
                return data[closest_match[0]]

        return "The word doesn't exist in the dictionary. Please check the spelling."

searchTerm = input("Enter the word you want to find the meaning for: ")

print(findMeaning(searchTerm))

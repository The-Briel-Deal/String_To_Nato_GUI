class NatoBrain:
    def __init__(self):
        alphabet = open("nato_phonetic_alphabet.csv").read()
        split_alphabet = alphabet.split("\n")
        list_alphabet = [item.split(",") for item in split_alphabet]
        del list_alphabet[0]
        self.check_alphabet = [letter[0] for letter in list_alphabet]
        self.dict_alphabet = {letter: word for (letter, word) in list_alphabet}

    def convert_to_nato(self, initial_text):
        converted_text = ""
        for letter in initial_text:
            if letter.upper() in self.check_alphabet:
                if letter.isupper():
                    temp_string = f"{letter} is Uppercase {self.dict_alphabet[letter.upper()]}"
                    temp_string = temp_string.ljust(60)
                    converted_text += f"{temp_string}\n"
                else:
                    temp_string = f"{letter} is Lowercase {self.dict_alphabet[letter.upper()]}"
                    temp_string = temp_string.ljust(60)
                    converted_text += f"{temp_string}\n"
            else:
                temp_string = f"{letter}"
                temp_string = temp_string.ljust(60)
                converted_text += f"{temp_string}\n"
        return converted_text

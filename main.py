import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")


phonetic = {row.letter: row.code for (column, row) in data.iterrows()}


user = input("Enter a letter: ").upper()

result = [phonetic[letter] for letter in user]
print(result)
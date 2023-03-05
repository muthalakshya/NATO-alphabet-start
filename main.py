import pandas
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dic = {}
for (index,row) in data.iterrows():
    alphabet = row[0]
    code = row[1]
    data_dic[alphabet] = code

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
enter_word = input("Enter Word : ").upper()
enter_list = list(enter_word)
final_list = [data_dic[n] for n in enter_list]
print(final_list)
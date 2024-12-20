# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data.to_dict())

# Create a dictionary from the data frame using iterrows
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Prompt the user to input a word
word = input("Enter a word: ").upper()

# Generate a list of phonetic code words
phonetic_code_words = [phonetic_dict[letter] for letter in word if letter in phonetic_dict]

# Print the resulting list
print(phonetic_code_words)



# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}



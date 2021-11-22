
import pandas
 

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict={row.letter:row.code for (index,row) in data.iterrows()}
#ask user for input and convert it into uppercase

word=input("Enter a word: \n" ).upper()
output_list=[phonetic_dict[letter] for letter in word]
print(output_list)
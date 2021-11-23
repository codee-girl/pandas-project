
import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict={row.letter:row.code for (index,row) in data.iterrows()}
#ask user for input and convert it into uppercase

def generate_phonetic():
    word=input("Enter a word: \n" ).upper()
    try:
        output_list=[phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only letters in the input are accepted.")
        generate_phonetic()
    else:        
        print(output_list)

generate_phonetic()      
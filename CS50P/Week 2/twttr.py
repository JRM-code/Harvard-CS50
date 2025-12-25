# --- GET STRING FROM THE USER --- #
string = input("Write a string: ")
vowel_list = ["a", "e", "i", "o", "u", 
              "A", "E", "I", "O", "U"]

# --- LOOP OVER THE STRING, FIND VOWELS AND REPLACE --- #
for i in string:
    if i in vowel_list:
        string = string.replace(i, '')

print(string)
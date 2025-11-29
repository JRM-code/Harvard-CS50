# --- GET GREETING FROM USER --- #
greeting = str(input("Enter your greeting: ")).lower().strip()

# --- SEPARATE GREETING TO LIST OF WORDS AND CHARS --- #
word_list = greeting.split(',')
char_list = list(greeting)

# --- EVALUATE GREETING AND PRINT RESULT --- #
if word_list[0] == "hello":
    print("$0")
elif word_list != "hello" and char_list[0] == "h":
    print("$20")
else:
    print("$100")
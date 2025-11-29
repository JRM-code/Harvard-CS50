# --- GET USER INPUT --- #
answer = str(input("What is the answer to the Great Question of Life, the Universe and Everything? ")).lower().strip()

# --- CHECK ANSWER WITH CONDITIONALS AND PRINT RESULT --- #
if answer == "forty two":
    print("Yes")
elif answer == "forty-two":
    print("Yes")
elif answer == "42":
    print("Yes")
else:
    print("No")
# --- GET GREETING FROM USER AND CALL VALUE FUNCTION, PRINT RESULT --- # 
def main():
    greeting = str(input("Enter your greeting: "))
    greet_value = value(greeting)
    print(f"${greet_value}")

# --- CHECK GREETING AND RETURN VALUE --- #
def value(greeting):
    greeting = greeting.lower().strip()

    for i in greeting:
        if greeting == "hello":
            return 0
        elif i[0] == "h":
            return 20
        else:
            return 100

if __name__ == "__main__":
    main()

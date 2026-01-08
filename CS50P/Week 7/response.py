from validator_collection import validators, errors

email = input("Enter email: ")

try:
    email = validators.email(email)
    if email:
        print("Valid")

except errors.EmptyValueError:
    print("Invalid")
except errors.InvalidEmailError:
    print("Invalid")
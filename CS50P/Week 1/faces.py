# --- GET USER GREETING AND CALL THE CONVERT FUNCTION --- #
def main():
    greeting = convert(str(input("Say Hello :) or Goodbye :( ")))  
    print(greeting)

def convert(smiley):    
    smiley = smiley.replace(':)', '🙂').replace(':(', '🙁')  
    return smiley

main()
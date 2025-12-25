# --- FUNCTION TO CONVERT KGS TO JOULES
def get_kgs(kgs):
    joules = kgs * (300000000 ** 2)
    print(joules)

# --- GET USER INPUT AND CALL THE CONVERSION FUNCTION--- #
kgs = get_kgs(int(input("Enter the mass in kgs: ")))

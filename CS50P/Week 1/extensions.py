# --- GET FILE NAME FROM USER --- #
filename = str(input("Enter your filename: ")).lower().strip()

# --- SPLIT THE FILE EXTENSION FROM THE FILE NAME --- #
ext_split = filename.split('.')
ext_name = ext_split[-1].lower()

# --- EVALUATE FILENAME AND PRINT RESULT --- #
if ext_name in ("gif", "jpeg", "png"):
    print("image/", ext_name, sep="")
elif ext_name == "jpg":
    print("image/jpeg")
elif ext_name == "pdf" or ext_name == "zip":
    print("application/", ext_name, sep="")
elif ext_name == "txt":
    print("text/plain")
elif ext_name == None:
    print("application/octet-stream")
else:
    print("application/octet-stream")

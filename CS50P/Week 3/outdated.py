# --- MONTH LIST --- #
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# --- GET USER DATE IN SPECIFIED FORMATS --- #
while True:
    user_date = input("Date: ").strip()
    try:
        # --- CONVERT DATE IN MM/DD/YYYY FORMAT --- #
        if '/' in user_date and user_date[0].isdigit():
            split_date = user_date.split("/")
            month = int(split_date[0])
            day = int(split_date[1])
            year = int(split_date[2])

        # --- CONVERT DATE IN MONTH D, YYYY FORMAT --- #
        elif ',' in user_date and not user_date[0].isdigit():
            month, day, year = user_date.split()
            if month in months: 
                month = months.index(month) + 1
                day = day.strip(',')
                day = int(day)

        else:
            continue
    except ValueError:
        continue

    try:
        if day > 31 or month > 12:
            continue
        else:
            break
    except ValueError:
        continue

print(f"{year}-{month:02}-{day:02}")

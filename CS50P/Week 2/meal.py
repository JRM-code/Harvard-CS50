# --- GET TIME FROM USER --- #
def main():
    day_time = input("What time is it? ")
    time = convert(day_time)

    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")
    else:
        return None

# --- CONVERT USER INPUT TO HOURS AND MINS DECIMAL --- #
def convert(time):
    hours, mins = time.split(":")
    hours = float(hours)
    mins = float(mins) / 60
    dec_time = round(hours + mins, 2)
    return dec_time

if __name__ == "__main__":
    main()
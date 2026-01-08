import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
        in_time = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s, re.IGNORECASE)

        # --- SPLIT GROUPS INTO A LIST --- #
        if in_time:
             split_time = list(in_time.groups())
        else:
             raise ValueError
        
        # --- FIX NONE VALUES --- #
        if split_time[1] == None:
             split_time[1] = 0
        if split_time[4] == None:
             split_time[4] = 0

        # --- CHECK HOUR AND MINUTE VALUES ARE VALID --- #
        if int(split_time[1]) > 59 or int(split_time[4]) > 59:
             raise ValueError
        if int(split_time[0]) > 12 or int(split_time[3]) > 12:
             raise ValueError
        
        # --- INT CONVERSION AND ASSIGNMENT --- #
        first_hour = int(split_time[0])
        first_mins = int(split_time[1])
        first_ap = split_time[2].lower()
        second_hour = int(split_time[3])
        second_mins = int(split_time[4])
        second_ap = split_time[5].lower()

        # --- CONVERT HOURS TO 24HR TIME --- #
        # --- IF AM --- #
        if first_hour == 12 and first_ap == "am":
            first_hour = 0
        if second_hour == 12 and second_ap == "am":
            second_hour = 0
        # --- IF PM --- #
        if first_hour != 12 and first_ap == "pm":
            first_hour = first_hour + 12
        if second_hour != 12 and second_ap == "pm":
            second_hour = second_hour + 12

        return f"{first_hour:02}" + ':' + f"{first_mins:02}" + ' to ' + f"{second_hour:02}" + ':' + f"{second_mins:02}"
             
if __name__ == "__main__":
    main()

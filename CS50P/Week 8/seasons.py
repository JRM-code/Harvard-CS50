from datetime import date, timedelta
import sys
import inflect

p = inflect.engine()

def main():
    birthday = input("Date of birth: ")
    minutes = calc_mins(birthday)
    print(p.number_to_words(minutes).capitalize().replace(" and", ""), "minutes")

def calc_mins(birthday):
    try:
        year, month, day = birthday.split("-")
        birthdate = date(int(year), int(month), int(day))
        min_diff = (date.today() - birthdate).total_seconds() / 60
        return round(min_diff)
    except ValueError:
        sys.exit(1)

if __name__ == "__main__":
    main()

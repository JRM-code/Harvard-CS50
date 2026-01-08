import re
import sys

def main():
    print(validate(input('IPv4 Address: ')))

def validate(ip):
    split_ip = ip.split(".")
    if re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        for i in split_ip:
            if i.startswith("0") and len(i) > 1:
                return False
            if int(i) < 0 or int(i) > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()


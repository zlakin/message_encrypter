import random

file_name = "secret_message"
file = open(file_name, "r")
encrypted_file = open("encrypted_message", "w+")
keys = []


def main(file1):
    shifter = get_rand_shifter()
    keys.append(shifter)
    line = file1.readline()
    encrypted_line = ""
    encrypt(line, encrypted_line, shifter)
    for line in file1:
        shifter = get_rand_shifter()
        keys.append(shifter)
        encrypted_line = ""
        encrypt(line, encrypted_line, shifter)
    print(keys)


def encrypt(line, encryption, shift):
    stripped = line.strip()
    lower_case_line = stripped.lower()
    for i in range(len(lower_case_line)):
        char = lower_case_line[i]
        encryption += chr((ord(char) + shift - 97) % 26 + 97)
    print(encryption)
    encrypted_file.write(encryption)
    encrypted_file.write("\n")


def get_rand_shifter():
    key = random.randint(1, 25)
    return key


def decrypt(line, list_of_keys):
    pass


main(file)

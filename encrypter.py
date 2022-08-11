import random

file_name = "secret_message"
file = open(file_name, "r")


def main(file1):
    shifter = get_rand_shifter()
    line = file1.readline()
    encrypted_line = ""
    encrypt(line, encrypted_line, shifter)
    for line in file1:
        shifter = get_rand_shifter()
        encrypted_line = ""
        encrypt(line, encrypted_line, shifter)


def encrypt(line, encryption, shift):
    stripped = line.strip()
    lower_case_line = stripped.lower()
    for i in range(len(lower_case_line)):
        char = lower_case_line[i]
        encryption += chr((ord(char) + shift - 97) % 26 + 97)
    print(encryption)


def get_rand_shifter():
    return random.randint(1, 25)


main(file)

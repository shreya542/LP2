import pyperclip as pc
import math

def main():
    my_message = "Toners raiCntisippoh"
    key = 6
    plaintext = decrypt(key, my_message)
    print("Plaintext is:", plaintext)

def decrypt(key, message):
    column = math.ceil(len(message) / key)
    rows = key
    numOfbox = (column * rows) - len(message)
    plaintext = [''] * column
    col = 0
    row = 0

    for c in message:
        plaintext[col] += c
        col += 1
        if col == column or (col == column - 1 and row >= rows - numOfbox):
            col = 0
            row += 1
    
    return ''.join(plaintext)

main()

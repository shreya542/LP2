import pyperclip

def decrypt_message(key, encrypted_message):
    num_columns = -(-len(encrypted_message) // key)
    num_rows = key
    num_unused_cells = (num_columns * num_rows) - len(encrypted_message)


    grid = [''] * num_columns
    column = 0
    row = 0
    for symbol in encrypted_message:
        grid[column] += symbol
        column += 1
        if (column == num_columns) or (column == num_columns - 1 and row >= num_rows - num_unused_cells):
            column = 0
            row += 1

    
    decrypted_message = ''.join(grid)

    return decrypted_message


key = 3
encrypted_message = "hello shreya"
decrypted_message = decrypt_message(key, encrypted_message)

print("Decrypted message:", decrypted_message)


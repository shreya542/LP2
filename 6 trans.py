import pyperclip as pc

def main():
	my_message="Transposition cipher"
	my_key=4
	ciphertext=encryptMessage(my_key,my_message)
	print("CipherText is")
	print(ciphertext+"|")
	pc.copy(ciphertext)

def encryptMessage(key,message):
	ciphertext=[""]*key
	for col in range(key):
		pos=col
		while pos<len(message):
			ciphertext[col]+=message[pos]
			pos+=key
		return "".join(ciphertext)

main()
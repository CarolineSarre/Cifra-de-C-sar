import sys

ALPHA ='abcdefghijklmnopqrstuvwxyz'
ROT = 3

def cipher(message, dir):
	m=''
	for c in message:
		if c in ALPHA:
			c_index = ALPHA.index(c)
			m+=ALPHA[(c_index + (dir * ROT))% len (ALPHA)]
		else:
			m+= c
	return m
def encrypt(message):
	return cipher(message, 1)

def decrypt(message):
	return cipher(message, -1)


def main():
	command = sys.argv[1].lower()
	message = sys.argv[2].lower()

	if command == 'encrypt':
		print (encrypt(message))

	elif command == 'decrypt':
		print (decrypt(message))

	else:
		print('command not found')

if __name__ == '__main__':
	main()
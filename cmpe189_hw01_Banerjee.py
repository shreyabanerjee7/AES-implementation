#Shreya Banerjee(012415845)

#S-BOX Table and Inverse S-box Table

box = [
        0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
        0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
        0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
        0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
        0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
        0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
        0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
        0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
        0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
        0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
        0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
        0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
        0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
        0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
        0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
        0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
       ]
    
boxinv = [
        0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
        0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
        0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
        0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
        0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
        0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
        0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
        0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
        0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
        0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
        0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
        0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
        0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
        0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
        0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
        0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
       ]

#The constant list that is used in Key Scheduling
rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]

#Taking the XOR of the Rotword, Rcon and w[i-4] columns to generate a Key Schedule
def KeyExpansion(key):
    w = []
    i = 0
    while (i < 4):
        w.append([key[4 * i], key[4 * i + 1], key[4 * i + 2], key[4 * i + 3]])
        i = i + 1
    i = 4
    while (i < 4 * 11):
        temp = w[i-1]
        if (i % 4 == 0):
            temp = AddLists(Subword(Rotword(temp, 1)), [rcon[int(i/4)-1], 0, 0, 0])
        w.append(AddLists(w[i-4],temp))
        i = i+1
    return w

#Rotates a word(4 bytes) by the input number of bytes 
def Rotword(word, a):
    return word[a:] + word[0:a]
 
#Performs the inverse of Rotword
def RotwordInv(word,a):
	return word[len(word)-a:] + word[0:len(word)-a]

#Takes a word and applies the S-box to each of the four bytes to give an output word	
def Subword(word):
    subw = []
    for i in range(len(word)):
        subw.append(box[word[i]])
    return subw
    
#Takes a word and applies the Inverse S-box to each of the four bytes to give an output word  
def SubwordInv(word):
	subw = []
	for i in range(len(word)):
		subw.append(boxinv[word[i]])
	return subw
	
#Does the XOR operation on the round key and the Mix columns functions which are taken as lists
def Add_Round_Key(state, w):
    return AddLists(state, w)
    
#Adds two lists of equal length    
def AddLists(a,b):
    l = [0 for i in range(len(a))]
    for i in range(len(a)):
        l[i] = a[i] ^ b[i]
    return l

#Bytes in the last three rows of the State(here taken as a single list) are shifted over different number of bytes
def ShiftRows(state):
    output_state = [0 for i in range(len(state))]
    for i in range(4):
        row = [state[0 + i], state[4 + i], state[8 + i], state[12 + i]]
        rotated_row = Rotword(row,i)
        for j in range(4):
            output_state[4 * j + i] = rotated_row[j]
    return output_state
    
#Performs the inverse of function ShiftRows()   
def InvShiftRows(state):
	output_state = [0 for i in range(len(state))]
	for i in range(4):
		row = [state[0 + i], state[4 + i], state[8 + i], state[12 + i]]
		rotated_row = RotwordInv(row,i)
		for j in range(4):
			output_state[4 * j + i] = rotated_row[j]
	return output_state

def into_one(va):
    return va

def into_two(va):
    op = 0x11b
    out = va << 1
    if (out >> 8 == 0):
        return out
    else:
        return (out ^ op)

def into_three(va):
    return into_one(va) ^ into_two(va)
    
def MixColumn(la):
    fr = into_two(la[0]) ^ into_three(la[1]) ^ into_one(la[2]) ^ into_one(la[3])
    se = into_one(la[0]) ^ into_two(la[1]) ^ into_three(la[2]) ^ into_one(la[3])
    th = into_one(la[0]) ^ into_one(la[1]) ^ into_two(la[2]) ^ into_three(la[3])
    fo = into_three(la[0]) ^ into_one(la[1]) ^ into_one(la[2]) ^ into_two(la[3])
    return [fr,se,th,fo]
    
#MixColumns() operates on the state column by column(here taken as a list) and does the matrix multiplication    
def MixColumns(state):
    return MixColumn(state[0:4]) + MixColumn(state[4:8]) + MixColumn(state[8:12]) + MixColumn(state[12:])

def into_fourteen(va):
	return into_two(into_two(into_two(va))) ^ into_two(into_two(va)) ^ into_two(va) 

def into_nine(va):
	return into_two(into_two(into_two(va))) ^ into_one(va)

def into_eleven(va):
	return into_two(into_two(into_two(va))) ^ into_two(va) ^ into_one(va)
	
def into_thirteen(va):
	return into_two(into_two(into_two(va))) ^ into_two(into_two(va)) ^ into_one(va)

#Performs the inverse of MixColumn()	
def InvMixColumn(la):
    fr = into_fourteen(la[0]) ^ into_eleven(la[1]) ^ into_thirteen(la[2]) ^ into_nine(la[3])
    se = into_nine(la[0]) ^ into_fourteen(la[1]) ^ into_eleven(la[2]) ^ into_thirteen(la[3])
    th = into_thirteen(la[0]) ^ into_nine(la[1]) ^ into_fourteen(la[2]) ^ into_eleven(la[3])
    fo = into_eleven(la[0]) ^ into_thirteen(la[1]) ^ into_nine(la[2]) ^ into_fourteen(la[3])
    return [fr,se,th,fo]

def InvMixColumns(state):
    return InvMixColumn(state[0:4]) + InvMixColumn(state[4:8]) + InvMixColumn(state[8:12]) + InvMixColumn(state[12:])

#This is the main encryption method. This runs the 10 rounds of the AES algorithm.
def Cipher(block, key):
	KeyEx = KeyExpansion(key)
	state = block
	
	state = Add_Round_Key(state, Key_list(KeyEx[0:4]))
	
	for round in range(1, 10):
		state = Subword(state)
		state = ShiftRows(state)
		state = MixColumns(state)
		state = Add_Round_Key(state, Key_list(KeyEx[4 * round:4 * (round + 1)]))
	
	state = Subword(state)
	state = ShiftRows(state)
	state = Add_Round_Key(state, Key_list(KeyEx[4 * 10:]))

	return state

#This is the main decryption method which performs the inverse of the Cipher function
def InvCipher(block, key):
	KeyEx = KeyExpansion(key)
	state = block
	
	state = Add_Round_Key(state, Key_list(KeyEx[4 * 10:]))
		
	for round in range(9, 0, -1):
		state = InvShiftRows(state)
		state = SubwordInv(state)
		state = Add_Round_Key(state, Key_list(KeyEx[4 * round:4 * (round + 1)]))
		state = InvMixColumns(state)
		
	state = InvShiftRows(state)
	state = SubwordInv(state)
	state = Add_Round_Key(state, Key_list(KeyEx[0:4]))
	
	return state

#Takes the 4 * 4 list and makes it into one single list to flatten the key	
def Key_list(inp):
	out = []
	for i in inp:
		out.extend(i)
	return out 

#Takes the ASCII value of the characters of a string s
def sttointlist(s):
	ints = []
	for i in range(len(s)):
		ints.append(ord(s[i]))
	return ints
	
#Converts an input of hexadecimal numbers and gives the output as integers represented by the hexadecimal numbers 
def sttohexlist(s):
	words = s.split()
	ls = []
	for i in range(len(words)):
		ls.append(int(words[i], 16))
	return ls
	
#Takes the input plaintext and a key, breaks plaintext into blocks of 16 bytes and then calls the Cipher function for each block 
def encrypt(s, keystring):
	key = sttointlist(keystring)
	plaintextint = sttointlist(s)
	l = len(s)
	ciphertext = []
	for i in range(int(l/16)):
		ciphertext.append(Cipher(plaintextint[i*16:(i+1)*16], key))
	if (l % 16 > 0):
		ciphertext.append(Cipher(plaintextint[int(l/16)*16:] + [0 for j in range(16 - l % 16)], key))
	return ciphertext

#Reads the plaintext_file, encryts and writes to the ciphertext_file
def EncryptFile(plaintext_file, ciphertext_file, key):
	read_file = open(plaintext_file, "r")
	s = read_file.read()
	read_file.close()
	ciphertext = encrypt(s, key)
	write_file = open(ciphertext_file, "w")
	for encrypted_block in ciphertext:
		block_list = ['{:02x}'.format(i) for i in encrypted_block]
		block_string = " ".join(block_list)
		write_file.write(block_string + "\n")
	write_file.close()
	
#Decrypts the ciphertext_file and writes to the decrypted_file 	
def DecryptFile(ciphertext_file, decrypted_file, key):
	keylist = sttointlist(key)
	read_file = open(ciphertext_file, "r")
	write_file = open(decrypted_file, "w")
	for line in read_file:
		encrypted_block = sttohexlist(line)
		plain_block = InvCipher(encrypted_block, keylist)
		for i in plain_block:
			if i != 0:
				write_file.write(chr(i))
	read_file.close()
	write_file.close()

EncryptFile("plaintext.txt", "encryptedtext.txt", "lukeimyourfather")
DecryptFile("encryptedtext.txt", "decryptedtext.txt", "lukeimyourfather")
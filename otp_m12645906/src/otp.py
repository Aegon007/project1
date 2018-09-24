## This is the code for project1 of class Data Security
##
## Author: Chenggang Wang
## UC ID: M12645906
## Date: Sept 17, 2018

import argparse
import random
import string
import binary

def str2Bits(str_input):
    """Converts string s to a string containing only 0s or 1s,
    representing the original string."""
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

	
def bits2Str(bits_input):
	"""Convert bin sequence to string, to show the cipher text or decrypt text"""
    chars = []
    for b in range(len(bits) / 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)


def KeyGen(n):
	'''
		Description: Generates a random key of bits (with 0s or 1s) of length n
		Input: key length n
		Output: binary key
	'''
	k = []
    for i in range(n):
        k.append(random.choice(["0", "1"]))
    return k

	
def Enc(msg, k):
	'''
		Description: using key to encode plaintext message to ciphertext
		Input: plaintext msg, binary key
		Output: ciphertext
	'''
	count = 0
	bMsg = str2Bits(msg)
	mLen = len(bMsg)
	for i in range(mLen):
		count = count % len(key)	
		elem = bMsg[i]
		tmp = elem ^ k[count]
		bMsg[i] = tmp
		count = count + 1
	
	cipher = bits2Str(bMsg)
	return cipher
		


def Dec(cipher, key):
	'''
		Description: using key to decode ciphertext to plaintext
		Input: ciphertext and key
		Output: plaintext
	'''
	count = 0
	bCipher = str2Bits(cipher)
	cLen = len(bCipher)
	for i in range(cLen):
		count = count % len(key)
		elem = bCipher[i]
		tmp = elem ^ k[count]
		bCipher[i] = tmp
		count = count + 1
	
	msg = bits2Str(bCipher)
	return msg


def saveData(fname, text):
	with open(fname, 'w') as f:
		f.write(text)
		
def readData(fname):
	with open(fname, 'r') as f:
		return f.read()

def main(opts, args):
	if 'genKey' == opts:
		KeyGen(args.length)
	elif '' == opts:
		Enc(msg, key)
	elif '' == opts:
		Dec(msg, key)
	else:
		print("input is not allowed.)
	

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Process input opts and args.')
	parser.add_argument('-f', '--function', dest='function',
						help='choose among encode/decode/genKey')
	parser.add_argument('-k', '--keyFile', dest='key',
						help='source input file/files, specify multipal time will enter multipal value')
	parser.add_argument('-p', '--plaintextFile', dest='source',
						help='source input file/files, specify multipal time will enter multipal value')
	parser.add_argument('-t', '--targetFile', dest='target',
						help='target output file')
	args = parser.parse_args()
	
	print(args.accumulate(args.integers))
	
	main(opts, args)
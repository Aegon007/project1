## This is the code for project1 of class Data Security
##
## Author: Chenggang Wang
## UC ID: M12645906
## Date: Sept 17, 2018

import argparse
import random


def charToNum(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    num = 1
    for letter in alphabet:
        if letter == char:
            break
        else:
            num+=1
    return num


def numToChar(num):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[num+1]


def str2Bin(str):


def bin2Str(bin):


def xor(m, k):
    """Given strings m and k of characters 0 or 1,
    it returns the string representing the XOR
    between each character in the same position.
    This means that m and k should be of the same length.

    Use this function both for encrypting and decrypting!"""
    r = []
    for i, j in zip(m, k):
        r.append(str(int(i) ^ int(j)))  # xor between bits i and j
    return "".join(r)


def KeyGen():
	'''
		Description: Generates a random key of bits (with 0s or 1s) of length n
		Input: 
		Output: 
	'''
	    k = []
    for i in range(n):
        k.append(random.choice(["0", "1"]))
    return "".join(k)

def Enc():
	'''
		Description: 
		Input: 
		Output: 	
	'''


def Dec():
	'''
		Description:
		Input: 
		Output: 
	'''


def main(opts, args):
	print("hello world")
	

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Process input opts and args.')
	parser.add_argument('function', dest='function',
						help='an integer for the accumulator')
	parser.add_argument('-s', '--sourceFile', dest='source',
						help='source input file/files, specify multipal time will enter multipal value')
	parser.add_argument('-t', '--targetFile', dest='target',
						help='target output file')
	args = parser.parse_args()
	print(args.accumulate(args.integers))
	
	main(opts, args)
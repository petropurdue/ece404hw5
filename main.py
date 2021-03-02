# Homework Number: 05
# Name: Ziro Petro
# ECN Login: petrop
# Due Date: March 02 2020
# Python Interpreter: Python 3.8

from BitVector import *
from Crypto.Cipher import AES

#Arguments:# v0: 128-bit BitVector object containing the seed value
# dt: 128-bit BitVector object symbolizing the date and time
# key_file: String of file name containing the encryption key (in ASCII) for AES
# totalNum: integer indicating the total number of random numbers to generate

#Function Description
# Uses the arguments with the X9.31 algorithm to generate totalNum randomnumbers as BitVector objects
# #Returns a list of BitVector objects, with each BitVector object representing arandom number generated from X9.31
def x931(v0, dt, totalNum, key_file):
    #file reading
    kptr = open(key_file,"r")
    key = kptr.readline()
    key = key.strip()

    #Initializations
    #print(len(key))
    key1 = key[0:16]
    key2 = key[16:32]
    #print(len(key1),len(key2))
    bkey1  = bytes(key1, 'utf-8') #bytekey 1
    bkey2  = bytes(key2, 'utf-8') #bytekey 2

    #Convert BV to byte vectors
    tv0 = v0.get_text_from_bitvector() #textv0
    print(tv0)
    bv0 = bytes(tv0, 'utf-8') #byte v0
    ddt = dt.int_val()
    bdt = ddt.to_bytes(2,'big')

    #begin EDE
    kak = AES.new(bkey1,AES.MODE_EAX)
    ede1 = kak.encrypt(bdt)
    ede3 = ede1 ^ bv0
    ede3 = kak.encrypt(ede3)
    ede2 = kak.encrypt(ede3 ^ ede1)
    v0 = ede2

    rj = ede3

    print("Aaa")
    #EDE - 2x DES- Encrypt, decrypt, encryptds
    #but where are the 2 keys it needs???

if __name__ == '__main__':
    v0 = BitVector(textstring='computersecurity')  # v0 will be 128 bits
    # As mentioned before, for testing purposes dt is set to a predetermined value
    dt = BitVector(intVal=99, size=128)
    listX931 = x931(v0,dt,3,'keyX931.txt')
    print("po")
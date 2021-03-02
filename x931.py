# Homework Number: 05
# Name: Ziro Petro
# ECN Login: petrop
# Due Date: March 02 2020
# Python Interpreter: Python 3.9

from BitVector import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.strxor import strxor

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
    bkey = bytes(key, 'utf-8')
    Randarr = []

    #Convert BV to byte vectors
    tv0 = v0.get_text_from_bitvector() #textv0
    bv0 = bytes(tv0, 'utf-8') #byte v0
    ddt = dt.int_val()
    #bdt = ddt.to_bytes(2,'little')
    bdt = bytes.fromhex(dt.get_bitvector_in_hex())

    #PRNG Initializations
    kak = AES.new(bkey,AES.MODE_ECB)

    #PRNG loop
    #ede1 = kak.encrypt(pad(bdt, 16))
    ede1 = kak.encrypt(bdt)
    for i in range(totalNum):
        ede3 = kak.encrypt(strxor(ede1,bv0))
        Randarr.append(int.from_bytes(ede3,'big'))
        ede2 = kak.encrypt(strxor(ede3,ede1))
        bv0 = ede2
        #print(len(ede1),len(ede2),len(ede3),len(bv0))
    #print(Randarr)
    #for i in Randarr :
    #    print(len(str(i)))
    return Randarr

def writetofile(datavals,filename):
    fptr = open(filename,"w")
    for i in datavals:
        if (type(i) == type(69)):
            fptr.write(str(i))
            if(datavals[len(datavals)-1]!= i):
                fptr.write('\n')
        if (type(i) == type('thephantompain')):
            fptr.write(i)

def part1test():
    v0 = BitVector(textstring='computersecurity')  # v0 will be 128 bits
    # As mentioned before, for testing purposes dt is set to a predetermined value
    dt = BitVector(intVal=501, size=128)
    listX931 = x931(v0, dt, 3, 'keyX931.txt')
    writetofile(listX931, 'output.txt')

if __name__ == '__main__':
    part1test()

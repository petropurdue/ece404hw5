from BitVector import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.strxor import strxor

def tempwritetofile(firsthree,datavals,filename):
    fptr = open(filename,"wb")
    for i in datavals:
        if (type(i) == type(69)):
            fptr.write(str(i))
            if(datavals[len(datavals)-1]!= i):
                fptr.write('\n')
        if (type(i) == type('thephantompain')):
            fptr.write(i)

#Arguments:
# iv: 128-bit initialization vector
# image_file: input .ppm image file name
# out_file: encrypted .ppm image file name
# key_file: String of file name containing encryption key (in ASCII)
#Function Descrption:
# Encrypts image_file using CTR mode AES and writes said file to out_file. No required return value.
def ctr_aes_image(iv,image_file='image.ppm',out_file='my_enc_image.ppm', key_file='key.txt'):
    #Read keyfile
    kptr = open(key_file, "r")
    key = kptr.readline()
    key = key.strip()

    #Open PPM File
    bptr = open(image_file,"rb")
    wholeassfile = bptr.readlines()

    #Initializations
    header = wholeassfile[0:3]
    ppm = wholeassfile[3:len(wholeassfile)]
    bkey = bytes(key, 'utf-8')
    encodedarr = []
    bvppm = []

    for i in ppm:
        bv = BitVector(rawbytes = i)
        bvppm.append(bv)

    #convert IV to int, add one, convert back to bitvector

    #Start encoding
    kak = AES.new(bkey,AES.MODE_ECB)


    for i in ppm:
        ede1 = kak.encrypt(bytes.fromhex(iv.get_bitvector_in_hex()))
        print((len(ede1), len(i)))
        encodedarr.append(strxor(ede1,i))

        #iv = BitVector(intVal= iv.int_val() + 1,size=128)
    
    tempwritetofile(header,encodedarr,'poo.ppm')
    readprint('poo.ppm')
    readprint('enc_image.ppm')


def readprint(image_file):
    #Open PPM File
    bptr = open(image_file,"rb")
    wholeassfile = bptr.readlines()
    print(wholeassfile)



def testpart2():
    iv = BitVector(textstring='computersecurity')  # iv will be 128 bits
    ctr_aes_image(iv,'image.ppm', 'enc_image.ppm', 'keyCTR.txt')

if __name__ == '__main__':
    testpart2()

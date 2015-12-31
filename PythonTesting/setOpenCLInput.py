import sys
#This code will fill the input text files with the current keys

##Absolute Locations of Folders
CARTER_PATH = "/home/sca-team/Andrew/RSA"
ALEX_PATH = "/home/sca-team/Andrew/rsa_optimizations"
PYTHON_PATH = "/home/sca-team/Andrew/PythonTesting"

##Input Files - These are the files we will ouput the key to
INPUT_OPENCL = "inputOpenCL.txt" #format: [p] [q] [e] [message]
INPUT_CPP = "inputCpp.txt" #format: [message] [e] [modulus] [p] [q]

##Read File - This is where we are reading the original keys from 
KEYS_FILE = "keys.csv" #format: [private exponent] [modulous] [public exponent] #Public Exponent remains constant

##DUMMY VALUES
MESSAGE = 'message'
P = 'p'
Q = 'q'

##Open an extract the set of keys that we want from the key file
KEY = open(KEYS_FILE)

runNum = sys.argv[1]

for i, line in enumerate(KEY): #Get the line corresponding to the key we want
	if i == (int(runNum)):
		currentKey = KEY.readline()
		print ("Run Num: " + runNum + " Current Line: " + currentKey)
	elif i > int(runNum):
        	break
KEY.close()

#Break string up into variables
keySplit = currentKey.split(",")
#print("Run Num: " + str(runNum))
#print("Current Key: " + str(currentKey))
#print("keySplit: " + str(keySplit))
#print("firstValue: " + str(keySplit[1]))
privateExponent = int(keySplit[0])
modulous = int(keySplit[1])
publicExponent = int(keySplit[2])
p = P
q = Q
message = MESSAGE

##Write the keys to designated input file
with open(INPUT_OPENCL, "a") as writeCL:
	writeCL.write(str(p) + " " + str(q) + " " + str(publicExponent) + " " + str(message) +  "\n")
with open(INPUT_CPP, "a") as writeCPP:
	writeCPP.write(str(message) + " " + str(publicExponent) + " " + str(modulous) + " " + str(p) + " " + str(q) + "\n")


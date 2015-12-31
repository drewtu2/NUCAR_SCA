import subprocess
import os

##Absolute Locations of Folders
CARTER_PATH = "/home/sca-team/Andrew/RSA"
ALEX_PATH = "/home/sca-team/Andrew/rsa_optimizations"
PYTHON_PATH = "/home/sca-team/Andrew/PythonTesting"

##Application Names
CasRSA_CL = "./CasRSA_CL"
Input = "example_conf.txt"
Output = "out.txt"
OpenCLResults = "OpenCLResults.txt"
RSA_CRT = "./RSA_CRT"
CppResults = "CppResults.txt"
	
subprocess.call("clear")

numRun = int(input("How many times would you like to check code? "))

for x in range(0,numRun):
	os.system("python3 setOpenCLInput.py " +  str(x))

	##Run and save open_CL code output
	os.chdir(CARTER_PATH) #Move to RSA Directory
	subprocess.call([CasRSA_CL, Input, Output]) #Run the OpenCL code. Input in format: [p] [q] [e] [message]
	f = open(Output) #Get the code ouput and append it to the end of the OpenCLResults
	latestResult = f.readline()
	f.close()

	os.chdir(PYTHON_PATH) #OpenCLResults file is in the Python Folder

	with open(OpenCLResults, "a") as myfile:
	    myfile.write(latestResult + "\n")


	##Run and Save RSA_CRT.cpp code output
	#os.chdir(ALEX_PATH) #Move to rsa_optimzations folder

	#subprocess.call([RSA_CRT, "mod", message, e, modulus, prime1, prime2]) #run the RSA_CRT encryption. Input format [message] [e] [modulus] [p] [q]
	#message can remain constant, exponent changes, modulus changes, [p] and [q] are dependent on modulus
	#os.chdir(PYTHON_PATH)

	#with open(CppResults, "a") as myfile:
	#    myfile.write(latestResult + "\n")


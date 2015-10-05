import os
import binascii

sign_list = ["ff d8", "ff d9", "4d 5a", "89 50 4e 47 0d 0a 1a 0a", "25 50 44 46", "ff fb", "49 44 33", "49 49 2a 00", "4d 4d 00 2a"]

#IDEAS FOR FOOTERS. STORE HEADERS/FOOTERS AS TUPLES, WHEN RUNNING THE CHECK, CHECK FIRST FOR HEADERS, IF HEADER IS FOUND, CHECK SECOND TUPLE INDEX.

file_list = [f for f in os.listdir(".") if os.path.isfile(f)]

for f in file_list:
	opened_file = open(f, "rb")
	unspaced_hex_data = binascii.hexlify(opened_file.read())
	hex_data = " ".join([unspaced_hex_data[i:i+2] for i in range(0, len(unspaced_hex_data), 2)])
	for sign in sign_list:
		if sign in hex_data:
			print "FOUND {} in {}".format(sign, f)
		
		
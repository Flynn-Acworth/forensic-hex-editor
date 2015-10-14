import os
import binascii

# sign_list = ["ff d8", "ff d9", "4d 5a", "89 50 4e 47 0d 0a 1a 0a", "25 50 44 46", "ff fb", "49 44 33", "49 49 2a 00", "4d 4d 00 2a"]

sig_list = [("ff d8", "ff d9")]

#IDEAS FOR FOOTERS. STORE HEADERS/FOOTERS AS TUPLES, WHEN RUNNING THE CHECK, CHECK FIRST FOR HEADERS, IF HEADER IS FOUND, CHECK SECOND TUPLE INDEX.

file_list = [f for f in os.listdir(".") if os.path.isfile(f)]

print file_list

for f in file_list:
	print "\n"
	print "OPENING {}".format(f)
	opened_file = open(f, "rb")
	
	#get hex data from the file
	unspaced_hex_data = binascii.hexlify(opened_file.read())

	#convert raw hex data into hex that is spaced properly so that the parser can match headers/footers
	hex_data = " ".join([unspaced_hex_data[i:i+2] for i in range(0, len(unspaced_hex_data), 2)])
	
	
	for sig in sig_list:

		if sig[0] in hex_data[0:6]: # this is looking for the header of the file.

			print "[+] Identified .jpeg header in file, finding footer for file: {}".format(f)

			last_index = len(hex_data)

			if sig[1] in hex_data[last_index - 5: last_index]: # checking to see if the footer is the last bytes in the file.
				print "[-] Identified .jpeg footer as last bytes. No appended data in file: {}".format(f)
			else:
				print "[!] Indentified potential appended data attached to file. Investigate file: {}".format(f)


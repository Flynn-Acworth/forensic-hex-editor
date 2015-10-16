import os
import binascii

listFoundHeader=[]
listFoundFooter=[]
listIssue=[]
listFile=[]
sig_list = [("ff d8", "ff d9"),("89 50 4e 47","49 45 4e 44")] # This list stores tuple values of headers/footers

file_list = [f for f in os.listdir(".") if os.path.isfile(f)] # creates a list of every file in the current directory
os.system("clear;")
print "|File List:"
for file in file_list:
                print "|   "+file # this for loop prints out every file in the current directory
print "\nNow Scanning..."


for f in file_list: # for every file

        opened_file = open(f, "rb") # open the file in read binary mode
        unspaced_hex_data = binascii.hexlify(opened_file.read()) # convert the binary into hexadecimal data.
        hex_data = " ".join([unspaced_hex_data[i:i+2] for i in range(0, len(unspaced_hex_data), 2)]) # add a space between every second character of the hex

        for sig in sig_list: # for every tuple pair of signatures

                if sig[0] in hex_data[0:11]: # if the first index of the tuple (the header) is found in the first 11 characters of hex
                        print " [+] {} | {} Header Found".format(f, sig[0]) # alert the user to the found header.
                        listFile.append(f)
                        listFoundHeader.append(sig[0])
                        last_index = len(hex_data) # last_index is a variable used to find the end of a file

                        if sig[1] in hex_data[last_index - 11: last_index]: # if the footer is in the last 11 characters of the hex
                                print " [-] {} | {} Footer Found".format(f, sig[1]) # alert the user to the found footer.
                                listFoundFooter.append(sig[1])
                                print "\n"
                        else:
                                print " [!] Potential Appended Data" # if footer is not found, it may indicate potential appended data in the file.
                                listIssue.append("Issue Found | "+str([hex_data[last_index - 11: last_index]]))
                                print "\n"

print "[+] {} File(s) found.".format(str(file_list.__len__()))
print "[+] {} File(s) scanned".format(str(listFile.__len__()))
print "[-] {} File(s) missed.\n".format(file_list.__len__()-listFile.__len__())
print "[+] {} Header(s) found.".format(str(listFoundHeader.__len__()))
print "[+] {} Footer(s) found.".format(str(listFoundFooter.__len__()))
print "[!] {} Issue(s) found.".format(str(listIssue.__len__()))


import os
import binascii

#sign_list = ["ff d8", "ff d9", "4d 5a", "89 50 4e 47 0d 0a 1a 0a", "25 50 44 46", "ff fb", "49 44 33", "49 49 2a 00", "4d 4d 00 2a"]
listFoundHeader=[]
listFoundFooter=[]
listIssue=[]
listFile=[]
sig_list = [("ff d8", "ff d9"),("ff d1","ff d3")]

file_list = [f for f in os.listdir(".") if os.path.isfile(f)]
os.system("clear;")
print "|File List:"
for file in file_list:
                print "|   "+file
print "\nNow Scanning..."
for f in file_list:

        opened_file = open(f, "rb")
        unspaced_hex_data = binascii.hexlify(opened_file.read())
        hex_data = " ".join([unspaced_hex_data[i:i+2] for i in range(0, len(unspaced_hex_data), 2)])

        for sig in sig_list:

                if sig[0] in hex_data[0:6]:
                        print " [+] {} | FF D8 Header Found".format(f)
                        listFile.append(f)
                        listFoundHeader.append("FF D8")
                        last_index = len(hex_data)

                        if sig[1] in hex_data[last_index - 5: last_index]:
                                print " [-] {} | FF D9 Footer Found".format(f)
                                listFoundFooter.append("FF D9")
                                print "\n"
                        else:
                                print " [!] {} | Potential Appended Data".format(f)+"|"+str([hex_data[last_index - 5: last_index]])
                                listIssue.append("Issue Found | "+str([hex_data[last_index - 5: last_index]]))
                                print "\n"

print "[+] {} File(s) found.".format(str(file_list.__len__()))
print "[+] {} File(s) scanned".format(str(listFile.__len__()))
print "[-] {} File(s) missed.\n".format(file_list.__len__()-listFile.__len__())
print "[+] {} Header(s) found.".format(str(listFoundHeader.__len__()))
print "[+] {} Footer(s) found.".format(str(listFoundFooter.__len__()))
print "[!] {} Issue(s) found.".format(str(listIssue.__len__()))


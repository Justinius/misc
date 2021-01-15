import sys
import os.path

fname = sys.argv[1]
inFile = open(fname,"r")
head,tail = os.path.splitext(fname)
oname = head+"_output"+tail
outFile = open(oname,"w")


for line in inFile:
    outFile.write(line.rstrip()+"\n")
    outFile.write(line.rstrip()+"\n")
    outFile.write("\n")

inFile.close()
outFile.close()
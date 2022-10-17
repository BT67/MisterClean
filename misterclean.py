#misterclean.py
#Created by JGallo 2022/7/12
#Removes duplicate lines from .txt files
import string, sys, getopt, os, argparse

inputfile = ''
outputfile = ''

parser = argparse.ArgumentParser(description='Removes duplicate lines from .txt files')
parser.add_argument('-i', '--input')
args = parser.parse_args()

try:
    opts, args = getopt.getopt(sys.argv[1:],'hi:o',['ifile='])
except getopt.GetoptError:
    print('usage: misterclean.py -i <inputfile>')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print('usage: misterclean.py -i <inputfile>')
        sys.exit()
    elif opt in ('-i', '--input'):
       inputfiles = arg
       
if(len(inputfiles) == 0):
    print('usage: misterclean.py -i <inputfile>')
else:
    inputfiles = inputfiles.split(",")
    print("Cleaning files:")
    for inputfile in inputfiles:
        print(inputfile)
        outputfile = inputfile.replace(".","_clean.")
        lines_seen = set() # holds lines already seen
        outfile = open(outputfile, "w")
        for line in open(inputfile, "r"):
            line = line.strip()
            line = line + "\n"
            if line not in lines_seen: # not a duplicate
                outfile.write(line)
                lines_seen.add(line)
        outfile.close()
        os.remove(inputfile)
        os.rename(outputfile,outputfile.replace("_clean",""))

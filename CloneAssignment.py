# Python 3
# Requires SSH key paired with GitHub Account
import os
import sys

if(len(sys.argv) == 5):
    classroomName = sys.argv[1]
    assignmentName = sys.argv[2]
    rosterPath = sys.argv[3]
    outpath = sys.argv[4]
else:
    print ("Invalid command line arguments, please run CloneAssignment.py [name of classroom][name of assignment] [path to roster] [absolute path for out dir]")
    sys.exit(0)

with open(rosterPath) as f:
    names = f.read().splitlines()

for name in names:
    print(name)
    cloneCmd = "git clone git@github.com:{}/{}-{}".format(classroomName, assignmentName, name) + " " + outpath+ "{}-{}".format(assignmentName, name)
    os.system(cloneCmd)


#!/usr/bin/env python

import re

shakes = open("TEXT DOC HERE", "r")

for line in shakes:
    if re.match("(.*)PID(.*)", line): 
        print line,

#The first line is a "shebang" that, on execution of the file, instructs the computer to process the script using the python interpreter. 
#The "import re" pulls in Python's standard regular expression module so we can use it later to search the text. 
#The open() command grabs the file we've just downloaded and opens it up. The "r" is for read mode.


#script will print lines that contain the word PID

#"(.*)(P|p)ID(.*)"
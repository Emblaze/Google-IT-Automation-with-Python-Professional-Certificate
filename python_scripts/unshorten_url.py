#!/usr/bin/env python3
import re
import urlexpander

sourcefile = open("Youtube_DevOps_Learning.txt")
outputfile = open("Youtube_DevOps_Learning_expanded.txt", "w")

def unshorten_url(sourcefile):
    """Searches for a shortned URL pattern in each line of the input file,
     expands and replaces it before saving it into a new file
    """
    pattern = r"https\:\/\/lnkd\.in\/[a-zA-Z0-9-_]+"
    for line in sourcefile:
        result = re.search(pattern, line)
        if result == None:
            outputfile.write(line)
        else:
            expandedurl = urlexpander.expand(result[0])
            print('About to replace: ', line, 'with: ', expandedurl)
            outputfile.write(expandedurl + "\n")
    sourcefile.close()
    outputfile.close()

unshorten_url(sourcefile)
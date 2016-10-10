## MIT License
## Copyright (c) 2016 Exequor Studios Inc.
##
## Permission is hereby granted, free of charge, to any person obtaining a
## copy of this software and associated documentation files (the
## "Software"), to deal in the Software without restriction, including
## without limitation the rights to use, copy, modify, merge, publish,
## distribute, sublicense, and/or sell copies of the Software, and to
## permit persons to whom the Software is furnished to do so, subject to
## the following conditions:
##
## The above copyright notice and this permission notice shall be included
## in all copies or substantial portions of the Software.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
## OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
## MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
## IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
## CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
## TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
## SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
from operator import itemgetter
folder_size = [];

# Change the root directory and maximum results below
rootDir = "C:/"
max_results = 50

def scanFolder(directory):
    global folder_size
    size = 0
    try:
        i = 0
        for file in os.listdir(path=directory):
            if (os.path.isdir(directory+file)):
                size += scanFolder(directory+file+"/")
            else:
                try:
                    size += os.path.getsize(directory+file)
                    i+=1
                    if (i%500 == 0):
                        print(".",end="")
                except FileNotFoundError:
                    print("*********************************************************************")
                    print(directory+" : File Not Found Error")
                    print("*********************************************************************")
                    return 0

        folder_size += [[directory,size]]
        return size
    except PermissionError:
        print("*********************************************************************")
        print(directory+" : Access Error")
        print("*********************************************************************")
        folder_size+= [[directory, -1000]]
        return 0

print ("Total Size: %d"%scanFolder(rootDir))
sorted_folders = sorted(folder_size, key=itemgetter(1), reverse=True)

i = max_results
for i in range(0,max_results):
    print (sorted_folders[i][0]+": {:,}k".format(int(sorted_folders[i][1]/1024)))
    

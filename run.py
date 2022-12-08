import os
import time
import sys

cwd = os.getcwd()
year = sys.argv[1]

start_time = time.time()
for (root, dirs, files) in os.walk('./%s' %(year)):

    for file in files:
        if file[-3:] == ".py":
            ind_start = time.time()
            print("##### %s #####" %(root.split("/")[-1]))
            os.chdir(root)
            os.system("python3 %s" %(file))
            os.chdir(cwd)
            print("Time taken: %s seconds\n" %(round(time.time()-ind_start, 3)))

print("Total time: %s seconds" %(round(time.time()-start_time, 3)))

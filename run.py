import os
import time
import sys

cwd = os.getcwd()
years = []
days = []

def handle_flags(_flag):
    if _flag.isnumeric():
        return [int(_flag)]
    elif "-" in _flag:
        _flag = _flag.split("-")
        return list(range(int(_flag[0]), int(_flag[1])+1))
    else:
        return [int(item) for item in _flag.split(",")]

for i in range(1, len(sys.argv)):
    if sys.argv[i] == "year":
        years = handle_flags(sys.argv[i+1])
        i += 1
    elif sys.argv[i] == "days":
        days = handle_flags(sys.argv[i+1])
        days = [("Day %s" %(item)) for item in days]
        i += 1

start_time = time.time()
for year in years:
    print("###### Year %s ######" %(year))
    year_start_time = time.time()
    for (root, dirs, files) in os.walk('./%s' %(year)):

        if root.split("/")[-1] in days:
            for file in files:
                if file[-3:] == ".py":
                    ind_start = time.time()
                    print("##### %s #####" %(root.split("/")[-1]))
                    os.chdir(root)
                    os.system("python3 %s >/dev/null" %(file))
                    os.chdir(cwd)
                    print("Time taken: %s seconds\n" %(round(time.time()-ind_start, 3)))
    print("Total time for year: %s seconds\n\n" %(round(time.time()-year_start_time, 3)))

print("Total time: %s seconds" %(round(time.time()-start_time, 3)))

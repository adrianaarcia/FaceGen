import os
import itertools
cwd = os.getcwd()
dir = cwd+'/assets/'

for subdir, dirs, files in os.walk(dir):
    for file in files:
        #remove info for teeth and tongue
        filepath = os.path.join(subdir, file)
        if file.lower().endswith(('2.png', '3.png')):
            os.remove(filepath)
        if file.lower().endswith(('.obj')): # line 23685 is the last relevant line
            line_num = 0
            #temp = file+'.bak'
            temppath = filepath+'.bak'
            with open(filepath, 'r') as original, open(temppath, 'w') as new:
                for line in original:
                    if line_num < 23685:
                        # Get parts (skip first)
                        if line.startswith('f '):
                            indexSets = [num for num in line.split(' ') if num][1:5]
                            combs = list(itertools.combinations(indexSets, 3))
                            for comb in combs:
                                new.write('f '+ ' '.join(comb) + '\n')
                        else: 
                            new.write(line)
                        line_num+=1
            os.remove(filepath)
            os.rename(temppath, filepath)
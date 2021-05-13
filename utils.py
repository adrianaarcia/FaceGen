import os
import itertools

def clear_results():
    cwd = os.getcwd()
    dir = cwd+'/results/'

    for subdir, dirs, files in os.walk(dir):
        for file in files:
            #remove previous results
            filepath = os.path.join(subdir, file)
            os.remove(filepath)
            
def preprocess():
    cwd = os.getcwd()
    dir = cwd+'/assets/'

    for subdir, dirs, files in os.walk(dir):
        for file in files:
            #remove info for teeth and tongue
            filepath = os.path.join(subdir, file)
            if file.lower().endswith(('2.png', '3.png')):
                os.remove(filepath)
            if file.lower().endswith(('.obj')): # line 23685 is the last relevant line
                count = 0
                temppath = filepath+'.bak'
                with open(filepath, 'r') as original, open(temppath, 'w') as new:
                    for line in original:
                        if line.startswith('o '):
                            if count != 0:
                                break
                            count += 1
                        if line.startswith('f '):
                            indexSets = [num for num in line.split(' ') if num][1:]
                            if len(indexSets) > 4:
                                indexSets = indexSets[:4]
                                combs = list(itertools.combinations(indexSets, 3))
                                for comb in combs:
                                    new.write('f '+ ' '.join(comb) + '\n')
                            else:
                                new.write(line)
                        else: 
                            new.write(line)
                os.remove(filepath)
                os.rename(temppath, filepath)
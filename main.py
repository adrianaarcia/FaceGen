import numpy as np
from vispy import app, io, scene
import vispy
from calc import norms, normalize, normalize_multi
from show import get_scatter, get_mesh, assign_colors
from utils import clear_results, preprocess

races = ['anyrace', 'african', 'eastasian', 'european', 'southasian']
sexes = ['anysex', 'male', 'female']

def comp_avg(sex, mcmap='viridis', scmap='viridis'):
    
    n = len(races)
    # make paths to files
    paths = ['/average/' + grp + '/'  + sex + '/' +  'avg_'+ grp + '_' + sex for grp in races]

    #initialize arrays 
    verts = []
    faces = []
    for i in range(n): #store vertices and faces for each face
        path = 'assets' + paths[i] + '.obj'
        vertices, facess, normals, nothing = io.read_mesh(path)
        verts.append(vertices)
        faces.append(facess)

    #calculate the norm of each face with respect to 'anyrace'
    nrms = [norms(verts[0], vert) for vert in verts]
    normalized_single = [normalize(x) for x in nrms] #normalize magnitude across self
    normalized_all = normalize_multi(nrms) #normalize magnitude across all faces

    for i in range(1, n): #skip 'anyrace' as we don't care to compare it to itself
        #get colors
        nall_arr = np.array(normalized_all[i])
        nrms_arr = np.array(nrms[i])
        
        sc = assign_colors(nall_arr, nrms_arr, scmap)
        mc = assign_colors(nall_arr, nrms_arr, mcmap)

        #display results
        vs = verts[i]
        fs = faces[i]

        path = 'results' + paths[i]

        #get_scatter(vs, sc, path)
        get_mesh(vs, fs, mc, path)

preprocess()
clear_results()
for sex in sexes:
    comp_avg(sex)

if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1:
        app.run()
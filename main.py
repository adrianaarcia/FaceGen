import numpy as np
from vispy import app, io, scene
import vispy
from calc import norms, normalize, normalize_multi
from show import get_scatter, get_mesh, assign_colors

racial_groups = ['anyrace', 'african', 'eastasian', 'european', 'southasian']

def comp_avg(sex, mcmap='blues', scmap='viridis'):
    
    n = len(racial_groups)
    # make paths to files
    # filenames = ['avg_'+ grp + '_' + sex  for grp in racial_groups]
    paths = ['/average/' + grp + '/'  + sex + '/' +  'avg_'+ grp + '_' + sex for grp in racial_groups]

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
        nall_arr = np.array(normalized_single[i])
        nrms_arr = np.array(nrms[i])
        
        sc = assign_colors(nall_arr, nrms_arr, scmap)
        mc = assign_colors(nall_arr, nrms_arr, mcmap)

        #display results
        vs = verts[i]
        fs = faces[i]

        rg = racial_groups[i]
        path = 'results' + paths[i]

        get_scatter(vs, sc, path)
        get_mesh(vs, fs, mc, path)


#comp_avg('anysex')
comp_avg('female')
comp_avg('male')

if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1:
        app.run()
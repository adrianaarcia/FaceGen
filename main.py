import numpy as np
from vispy import app, io
from calc import norms, normalize, normalize_multi
from show import show_scatter, show_mesh, assign_colors

racial_groups = ['anyrace', 'african', 'eastasian', 'european', 'southasian']

def comp_avg(sex, mcmap='hsl', scmap='viridis'):
    #get path to file
    path_head = 'assets/average/'
    path_end = '/' + sex + '/'

    filename_head = 'avg_'
    filename_end = '_' + sex + '.obj'

    #initialize arrays 
    verts = []
    faces = []
    for grp in racial_groups: #store vertices and faces for each face
        path = path_head+grp+path_end+filename_head+grp+filename_end
        vertices, facess, normals, nothing = io.read_mesh(path)
        verts.append(vertices)
        faces.append(facess)

    #calculate the norm of each face with respect to 'anyrace'
    nrms = [norms(verts[0], vert) for vert in verts]
    normalized_single = [normalize(x) for x in nrms] #normalize magnitude across self
    normalized_all = normalize_multi(nrms) #normalize magnitude across all faces

    for i in range(1, 4): #skip 'anyrace' as we don't care to compare it to itself
        #get colors
        nall_arr = np.array(normalized_single[i])
        nrms_arr = np.array(nrms[i])
        
        sc = assign_colors(nall_arr, nrms_arr, scmap)
        mc = assign_colors(nall_arr, nrms_arr, mcmap)

        #display results
        vs = verts[i]
        fs = faces[i]

        #show_scatter(vs, sc)
        show_mesh(vs, fs, mc)

comp_avg('anysex')
if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1:
        app.run()
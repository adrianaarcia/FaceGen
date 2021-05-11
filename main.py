import numpy as np
from vispy import app, io
from calc import norms, normalize, normalize_multi
from show import show_scatter, show_mesh, assign_colors

#get path to file
path_head = 'assets/average/'
path_end = '/anysex/'

filename_head = 'avg_'
filename_end = '_anysex.obj'

#choose face to compare
cmp_index = 2
dirs = ['anyrace', 'african', 'eastasian', 'european', 'southasian']

verts = []
faces = []
for dir in dirs:
    path = path_head+dir+path_end+filename_head+dir+filename_end
    vertices, facess, normals, nothing = io.read_mesh(path)
    verts.append(vertices)
    faces.append(facess)

nrms = [norms(verts[0], vert) for vert in verts]
normalized_single = [normalize(x) for x in nrms]
normalized_all = normalize_multi(nrms)

#get colors
nall_arr = np.array(normalized_all[cmp_index])
nrms_arr = np.array(nrms[cmp_index])
vs = verts[cmp_index]
fs = faces[cmp_index]

sc = assign_colors(nall_arr, nrms_arr)
mc = assign_colors(nall_arr, nrms_arr)

#display results
show_scatter(vs, sc)
show_mesh(vs, fs, mc)

if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1:
        app.run()
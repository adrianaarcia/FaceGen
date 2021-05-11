import numpy as np
from vispy import app, scene, io, visuals, color
from vispy.visuals import transforms
import vispy.plot as vp
from vispy.util.filter import gaussian_filter
from calc import norms, normalize, normalize_multi

#get face vertices from files
path_head = 'assets/average/'
path_end = '/anysex/'

filename_head = 'avg_'
filename_end = '_anysex.obj'

cmp_index = 1
dirs = ['anyrace', 'african', 'eastasian', 'european', 'southasian']
vertices = []

for dir in dirs:
    path = path_head+dir+path_end+filename_head+dir+filename_end
    verts, faces, normals, nothing = io.read_mesh(path)
    vertices.append(verts)

# A = vertices[0]
# B = vertices[1]
nrms = [norms(vertices[0], vert) for vert in vertices]
normalized_single = [normalize(x) for x in nrms]
normalized_all = normalize_multi(nrms)

#set up view box
canvas = scene.SceneCanvas(keys='interactive', show=True)
view = canvas.central_widget.add_view()
view.camera = scene.TurntableCamera(up='+y', distance=500)
view.camera.rect = (-10, -10, 20, 20)

# #get colors
# cm = color.get_colormap('viridis')
# colors = cm.map(normalized_all[cmp_index])

# # build visuals
# Scatter3D = scene.visuals.create_visual_node(visuals.MarkersVisual)
# p1 = Scatter3D(parent=view.scene)
# p1.set_gl_state('translucent', blend=True, depth_test=True)

# p1.set_data(vertices[cmp_index], symbol='o', size=5, edge_width=0.2, face_color=colors)

z = np.random.normal(size=(250, 250), scale=200)
z[100, 100] += 50000
z = gaussian_filter(z, (10, 10))

fig = vp.Fig(show=False)
cnorm = z / abs(np.amax(z))
c = color.get_colormap("hsl").map(cnorm).reshape(z.shape + (-1,))
c = c.flatten().tolist()
c=list(map(lambda x,y,z,w:(x,y,z,w), c[0::4],c[1::4],c[2::4],c[3::4]))

#p1 = fig[0, 0].surface(z, vertex_colors=c) # why doesn't vertex_colors=c work?
p1 = fig[0, 0].surface(z)
p1.mesh_data.set_vertex_colors(c) # but explicitly setting vertex colors does work?

fig.show()

if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1:
        app.run()
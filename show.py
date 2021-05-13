import numpy as np
from vispy import scene, visuals, color, io

def assign_colors(normalized_arr, nrms_arr, cmap='husl'):      
    colors = color.get_colormap(cmap).map(normalized_arr).reshape(nrms_arr.shape + (-1,))
    colors = colors.flatten().tolist()
    colors =list(map(lambda x,y,z,w:(x,y,z,w), colors[0::4], colors[1::4], colors[2::4], colors[3::4]))

    return colors

def viewbox(canvas):
    vb = canvas.central_widget.add_view()
    vb.camera = scene.TurntableCamera(up='+y', distance=500)
    vb.camera.rect = (-10, -10, 20, 20)

    return vb

def get_scatter(verts, colors, path):
    s = scene.canvas.SceneCanvas(keys='interactive', show=True)
    view = viewbox(s)
   
    Scatter3D = scene.visuals.create_visual_node(visuals.MarkersVisual)
    p1 = Scatter3D(parent=view.scene)
    p1.set_gl_state('translucent', blend=True, depth_test=True)
    p1.set_data(verts, symbol='o', size=5, edge_width=0.2, face_color=colors)
    
    img = s.render()
    io.write_png(path + "_verts.png", img)


def get_mesh(vs, fs, colors, path):
    s = scene.canvas.SceneCanvas(keys='interactive', show=True)
    view = viewbox(s)

    mesh = scene.visuals.Mesh(vertices=vs, faces=fs, shading='smooth', vertex_colors=colors)
    mesh.set_gl_state('translucent', depth_test=True, cull_face=True)

    view.add(mesh)

    img = s.render()
    io.write_png(path  + "_mesh.png",img)

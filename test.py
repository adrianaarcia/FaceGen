import pywavefront
import numpy as np
import json

avg_anyrace_anysex = pywavefront.Wavefront('assets/average/anyrace/anysex/avg_anyrace_anysex.obj')
avg_african_anysex = pywavefront.Wavefront('assets/average/african/anysex/avg_african_anysex.obj')
avg_eastasian_anysex = pywavefront.Wavefront('assets/average/eastasian/anysex/avg_eastasian_anysex.obj')
avg_european_anysex = pywavefront.Wavefront('assets/average/european/anysex/avg_european_anysex.obj')
avg_southasian_anysex = pywavefront.Wavefront('assets/average/southasian/anysex/avg_southasian_anysex.obj')

geometries = [avg_anyrace_anysex, avg_african_anysex, avg_eastasian_anysex, avg_european_anysex, avg_southasian_anysex]


defined_race_verts = [avg_african_anysex.vertices, avg_eastasian_anysex.vertices,  avg_southasian_anysex.vertices, avg_european_anysex.vertices]
anyrace_verts = avg_anyrace_anysex.vertices

nrms = [norms(anyrace_verts, vert) for vert in defined_race_verts]

normalized_single = [normalize(x) for x in nrms]
normalized_across = normalize_multi(nrms)

# with open("verts.json", "w") as f:
#     json_str = json.dumps({'anyrace_verts': anyrace_verts})
#     f.write(json_str)
    
# with open("norms.json", "w") as f:
#     json.dump(nrms, f)

# with open("single.json", "w") as f:    
#     json.dump(normalized_single, f)

# with open("across.json", "w") as f:
#     json.dump(normalized_across, f)

# for i in range(len(defined_race_verts)):
#     print("--------------------")
#     print("Norms")
#     x = nrms[i]

#     sm = sum(x)
#     avg = np.mean(x)
    
#     print(f"{sm}, {avg}")
#     print("")

#     print("Norms, normalized (single)")
#     x = normalized_single[i]

#     sm = sum(x)
#     avg = np.mean(x)

#     print(f"{sm}, {avg}")
#     print("")

#     print("Norms, normalized (all)")
#     x = normalized_accross[i]
    
#     sm = sum(x)
#     avg = np.mean(x)
    
#     print(f"{sm}, {avg}")
#     print("--------------------")



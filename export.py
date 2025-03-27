import trimesh
import os

# path = "/Users/bytedance/Desktop/CVPR'25/complete mesh/kitchen/kitchen_our/heatmap_0.6"
# files = os.listdir(path)
# # Load the .ply file
# for file in files:
#     if file.startswith("langsurf") is True:
#         input_file = os.path.join(path, file)
#         mesh = trimesh.load(input_file)
#         # Export as .glb
#         output_file = os.path.join('static/images/kitchen', file.split('.')[0] + '.glb')
#         mesh.export(output_file)

# langsurf_kitchen_mesh = trimesh.load("/Users/bytedance/Desktop/CVPR'25/complete mesh/kitchen/kitchen_our/langsurf_language.ply")
# output_file = os.path.join('static/images/', 'langsurf_kitchen.glb')
# langsurf_kitchen_mesh.export(output_file, file_type="glb")
 
# files = os.listdir("static/images/0085")
# # Load the .ply file
# for file in files:
#     input_file = os.path.join('static/images/0085', file)
#     mesh = trimesh.load(input_file)
#     # Export as .glb
#     output_file = os.path.join('static/images/0085', file.split('.')[0] + '.glb')
#     mesh.export(output_file)

# langsurf_085_gt_mesh = trimesh.load("/Users/bytedance/Desktop/CVPR'25/complete mesh/0085/scene0085_00_vh_clean_2.ply")
# output_file = os.path.join('static/images/0085', 'scene0085_00_vh_clean_2.glb')
# langsurf_085_gt_mesh.export(output_file, file_type="glb")

langsurf_085_gt_mesh = trimesh.load("/Users/bytedance/Desktop/CVPR'25/complete mesh/0617/scene0617_00_vh_clean_2.ply")
output_file = os.path.join('static/images/0617', 'scene0617_00_vh_clean_2.glb')
langsurf_085_gt_mesh.export(output_file, file_type="glb")


path = "/Users/bytedance/Desktop/CVPR'25/complete mesh/0617/0617_our/heatmap_0.53"
files = os.listdir(path)
# Load the .ply file
for file in files:
    if file.startswith("langsurf") is True:
        input_file = os.path.join(path, file)
        mesh = trimesh.load(input_file)
        # Export as .glb
        output_file = os.path.join('static/images/0617', file.split('.')[0] + '.glb')
        mesh.export(output_file)
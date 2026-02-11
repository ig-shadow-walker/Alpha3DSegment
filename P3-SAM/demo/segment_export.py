"""
Export segmented mesh to GLB with one material per part.
"""
import numpy as np
import trimesh
from trimesh.visual import TextureVisuals
from trimesh.visual.material import PBRMaterial


def export_segmented_mesh_with_materials(mesh, face_ids, color_map, filepath):
    """
    Export a segmented mesh as a GLB with one mesh per part and one material per part.

    Args:
        mesh: trimesh.Trimesh
        face_ids: (n_faces,) int array of part id per face; -1/-2 are skipped
        color_map: dict part_id -> (R, G, B) uint8
        filepath: output path (e.g. .glb)
    """
    unique_ids = np.unique(face_ids)
    face_index_arrays = []
    part_ids = []
    for part_id in unique_ids:
        if part_id in (-1, -2):
            continue
        mask = face_ids == part_id
        n = np.sum(mask)
        if n == 0:
            continue
        face_index_arrays.append(np.where(mask)[0])
        part_ids.append(part_id)

    if not face_index_arrays:
        # Fallback: export single mesh with face colors (no valid parts)
        mesh_save = mesh.copy()
        face_colors = np.zeros((len(mesh.faces), 3), dtype=np.uint8)
        for i in range(len(mesh.faces)):
            pid = face_ids[i]
            if pid in color_map:
                face_colors[i] = color_map[pid]
        mesh_save.visual.face_colors = face_colors
        mesh_save.export(filepath)
        return

    submeshes = mesh.submesh(face_index_arrays, append=False)
    scene = trimesh.Scene()
    for part_mesh, part_id in zip(submeshes, part_ids):
        color = np.asarray(color_map[part_id], dtype=np.float64) / 255.0
        material = PBRMaterial(
            baseColorFactor=(float(color[0]), float(color[1]), float(color[2]), 1.0)
        )
        part_mesh.visual = TextureVisuals(material=material)
        scene.add_geometry(part_mesh, geom_name=f"part_{part_id}")
    scene.export(filepath)

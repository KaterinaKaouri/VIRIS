from topologicpy.Vertex import Vertex
from topologicpy.Edge import Edge
from topologicpy.Wire import Wire
from topologicpy.Face import Face
from topologicpy.Shell import Shell
from topologicpy.Cell import Cell
from topologicpy.CellComplex import CellComplex
from topologicpy.Cluster import Cluster
from topologicpy.Topology import Topology
from topologicpy.Graph import Graph
from topologicpy.Dictionary import Dictionary
from topologicpy.Vector import Vector
from topologicpy.Helper import Helper
from topologicpy.Plotly import Plotly
import numpy as np
from tqdm.auto import tqdm
import math
from math import nan



def convert_seconds_to_hms(seconds):
    # Calculate hours, minutes, and remaining seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60

    # Return the result as a tuple (hours, minutes, seconds)
    return hours, minutes, remaining_seconds

def ByMeshFace(face, meshSize = None, meshName = None, tolerance = 0.0001):
    """
    Creates a shell of triangular meshes from the input face.

    Parameters
    ----------
    face : topologic.Face
        The input face.
    meshSize : float , optional
        The desired mesh size.
    tolerance : float , optional
        The desired tolerance. The default is 0.0001.
    
    Returns
    ----------
    topologic.Shell
        The shell of triangular meshes.

    """

    import gmsh
    import numpy as np
    from topologicpy.Vertex import Vertex
    from topologicpy.Wire import Wire
    from topologicpy.Face import Face
    from topologicpy.Shell import Shell
    import topologic_core as topologic

    if not isinstance(face, topologic.Face):
        print("Shell.ByMeshFace - Error: The input face parameter is not a valid face. Returning None.")
        return None
    if not meshSize:
        bounding_face = Face.BoundingRectangle(face)
        bounding_face_vertices = Face.Vertices(bounding_face)
        bounding_face_vertices_x = [Vertex.X(i) for i in bounding_face_vertices]
        bounding_face_vertices_y = [Vertex.Y(i) for i in bounding_face_vertices]
        width = max(bounding_face_vertices_x)-min(bounding_face_vertices_x)
        length = max(bounding_face_vertices_y)-min(bounding_face_vertices_y)
        meshSize = max([width,length])//10
    if not meshName:
        meshName = "mesh.msh"
    
    gmsh.initialize()
    face_external_boundary = Face.ExternalBoundary(face)
    external_vertices = Wire.Vertices(face_external_boundary)
    external_vertex_number = len(external_vertices)
    for i in range(external_vertex_number):
        gmsh.model.geo.addPoint(Vertex.X(external_vertices[i]), Vertex.Y(external_vertices[i]), Vertex.Z(external_vertices[i]), meshSize, i+1)
    for i in range(external_vertex_number):
        if i < external_vertex_number-1:
            gmsh.model.geo.addLine(i+1, i+2, i+1)
        else:
            gmsh.model.geo.addLine(i+1, 1, i+1)
    gmsh.model.geo.addCurveLoop([i+1 for i in range(external_vertex_number)], 1)
    current_vertex_number = external_vertex_number
    current_edge_number = external_vertex_number
    current_wire_number = 1

    face_internal_boundaries = Face.InternalBoundaries(face)
    if face_internal_boundaries:
        internal_face_number = len(face_internal_boundaries)
        for i in range(internal_face_number):
            face_internal_boundary = face_internal_boundaries[i]
            internal_vertices = Wire.Vertices(face_internal_boundary)
            internal_vertex_number = len(internal_vertices)
            for j in range(internal_vertex_number):
                gmsh.model.geo.addPoint(Vertex.X(internal_vertices[j]), Vertex.Y(internal_vertices[j]), Vertex.Z(internal_vertices[j]), meshSize, current_vertex_number+j+1)
            for j in range(internal_vertex_number):
                if j < internal_vertex_number-1:
                    gmsh.model.geo.addLine(current_vertex_number+j+1, current_vertex_number+j+2, current_edge_number+j+1)
                else:
                    gmsh.model.geo.addLine(current_vertex_number+j+1, current_vertex_number+1, current_edge_number+j+1)
            gmsh.model.geo.addCurveLoop([current_edge_number+i+1 for i in range(internal_vertex_number)], current_wire_number+1)
            current_vertex_number = current_vertex_number+internal_vertex_number
            current_edge_number = current_edge_number+internal_vertex_number
            current_wire_number = current_wire_number+1

    gmsh.model.geo.addPlaneSurface([i+1 for i in range(current_wire_number)])
    gmsh.model.geo.synchronize()
    
    gmsh.model.mesh.generate(2)         # For a 2D mesh
    gmsh.write(meshName)
    nodeTags, nodeCoords, nodeParams = gmsh.model.mesh.getNodes(-1, -1)
    elemTypes, elemTags, elemNodeTags = gmsh.model.mesh.getElements(-1, -1)
    gmsh.finalize()
    
    vertex_number = len(nodeTags)
    vertices = []
    for i in range(vertex_number):
        vertices.append(Vertex.ByCoordinates(nodeCoords[3*i],nodeCoords[3*i+1],nodeCoords[3*i+2]))

    faces = []
    for n in range(len(elemTypes)):
        vn = elemTypes[n]+1
        et = elemTags[n]
        ent = elemNodeTags[n]
        if vn==3:
            for i in range(len(et)):
                face_vertices = []
                for j in range(vn):
                    face_vertices.append(vertices[np.where(nodeTags==ent[i*vn+j])[0][0]])
                faces.append(Face.ByVertices(face_vertices))
    shell = Shell.ByFaces(faces, tolerance=tolerance)
    return shell
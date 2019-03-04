import pandas as pd
import igraph as ig

import sys

vertices_path = sys.argv[1]
edges_path = sys.argv[2]
graph_storage_path = sys.argv[3]
country_code = vertices_path[:3].lower()

vdf = pd.read_csv(vertices_path)
edf = pd.read_csv(edges_path)

def get_index_by_id(id):
	for row in range(vdf.shape[0]): # df is the DataFrame
	    if vdf['id'][row] == name:
	    	return row
	    	break

edge_list = []
for i in range(len(edf['src'])):
	edge_list.append([get_index_by_name(edf['src'][i]), get_index_by_name(edf['dst'][i])])

G = ig.Graph(directed=True)
G.add_vertices(vdf['name'])
G.vs['x'] = vdf['lat']
G.vs['y'] = vdf['lon']
G.add_edges(edge_list)
G.es['length'] = edf['length']
G.es['oneway'] = edf['oneway']
G.es['highway'] = edf['highway']
G.es[weight] = edf['length']

print("Serializing igraph")
pickle.dump(G_ig, open(graph_storage_path + "/" + country_code + "_roads_igraph.p", "wb"))




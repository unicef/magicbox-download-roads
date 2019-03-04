import pandas as pd
import igraph as ig

vertices_path = sys.argv[1]
edges_path = sys.argv[2]
graph_storage_path = sys.argv[3]

vdf = pd.read_csv(vertices_path)
edf = pd.read_csv(edges_path)

def get_index_by_name(name):
	for row in range(vdf.shape[0]): # df is the DataFrame
	         for col in range(vdf.shape[1]):
	             if df.get_value(row,col) == name:
	                 return(row)
	                 break

for i in range(len(edf['src'])):
	edf.set_value(i, 'src', get_index_by_name(edf['src'][i]))

for i in range(len(edf['dst'])):
	edf.set_value(i, 'dst', get_index_by_name(edf['dst'][i]))

G = ig.Graph(directed=True)
G.add_vertices(vdf['name'])
G.vs['x'] = vdf['lat']
G.vs['y'] = vdf['lon']



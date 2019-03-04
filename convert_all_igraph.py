import pandas as pd
import igraph as ig
import pickle
import sys, os
import pathos.multiprocessing as mp

from iso_country_codes import CC

csv_storage_dir = sys.argv[1]
igraph_storage_dir = sys.argv[2]

country_codes = [v.upper() for k,v in list(CC.items())]
num_cores = mp.cpu_count()
csv_dir_list = os.listdir(csv_storage_path)

def csv_to_igraph(country_code):
	vertices_path = csv_storage_dir + "/" + country_code + "_roads_vertices.csv"
	edges_path = csv_storage_dir + "/" + country_code + "_roads_edges.csv"

	if (country_code + "_roads_vertices.csv") and (country_code + "_roads_edges.csv") not in csv_dir_list:
		print("Unable to find graph csv for " + country_code)
	else:
		vdf = pd.read_csv(vertices_path)
		edf = pd.read_csv(edges_path)

		def get_index_by_id(id):
			for row in range(vdf.shape[0]): # df is the DataFrame
			    if vdf['id'][row] == id:
			    	return row
			    	break

		edge_list = []
		for i in range(len(edf['src'])):
			edge_list.append([get_index_by_id(edf['src'][i]), get_index_by_id(edf['dst'][i])])

		G = ig.Graph(directed=True)
		G.add_vertices(vdf['id'])
		G.vs['osmid'] = vdf['id']
		G.vs['x'] = vdf['lat']
		G.vs['y'] = vdf['lon']

		G.add_edges(edge_list)
		G.es['length'] = edf['length']
		G.es['oneway'] = edf['oneway']
		G.es['highway'] = edf['highway']
		G.es[weight] = edf['length']

		print("Serializing igraph")
		pickle.dump(G_ig, open(graph_storage_path + "/" + country_code.lower()+ "_roads_igraph.p", "wb"))

def main():
    pool = mp.Pool(processes=num_cores)
    pool.map(makeIGraph, countries)   

if __name__ == "__main__":
    main()


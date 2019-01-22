import csv
import multiprocessing
import sys, os
import osmnx as ox 

from unicef_programme_countries import countries

graph_path = sys.argv[1]

def makeGraph(country, path):
    """ Given a country's name and a path to store graphs, 
    retrieves its road network writes edgelist and vertices list
    .csv's to path
    """

    edges_file = country + "_roads_edges.csv"
    vertices_file = country + "_roads_vertices.csv"
    
    if edges_file in os.listdir(path) or vertices_file in os.listdir(path):
        print("Graph for " + country + " already stored."
        return False

    else:

        try:
            print("Starting process for" + country)
            G = ox.graph_from_place(country, simplify=True, clean_periphery=True)

            print("Retrieved graph for " + country + ", starting vertices storage")
            with open(path + vertices_file, 'w') as roads_vertices:
                verticesWriter = csv.writer(roads_vertices, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                verticesWriter.writerow(['id', 'lat', 'lon'])
                for node in G:
                    verticesWriter.writerow([node, G.node[node]['y'], G.node[node]['x']])
                
            print("Completed storing vertices, starting edges storage")
            with open(path + edges_file, 'w') as roads_edges:
                edgesWriter = csv.writer(roads_edges, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                edgesWriter.writerow(['src', 'dst', 'len', 'lat0', 'lon0', 'lat1', 'lon1', 'oneway', 'highway'])
                for (u,v) in list(G.edges()):
                    edgesWriter.writerow([u, v, G[u][v][0]['length'], G.node[u]['y'], G.node[u]['x'], G.node[v]['y'], G.node[v]['x'],  G[u][v][0]['oneway'], G[u][v][0]['highway']])

            with open("retrieval_log.txt", 'w') as logfile:
                logfile.write("Graph storage success for " + country)
            print('Completed graph storage for ' + country)
            
            return True

        except:

            with open("retrieval_log.txt", 'w') as logfile:
                logfile.write("Retrieval failed for " + country)

            return False

def main():
    with multiprocessing.Pool() as pool:
        pool.map(lambda c : makeGraph(c, graph_path), countries)        

if __name__ == "__main__":
    main()

import igraph as ig
import networkx as nx
import numpy as np
import operator
import osmnx as ox
import sys, os, pickle
import multiprocessing

# imports only a dictionary of UNICEF programme countries mapped to country codes
from iso_country_codes import CC
from unicef_programme_countries import countries

ox.config(use_cache=True, log_console=True)
weight = 'length'

graph_storage_path = sys.argv[1]

def makeIGraph(country_name):

    try:
        country_code = CC[country_name]
    except:
        print("Country name must be a valid UNICEF programme country, moving on ... ")
        return False

    graph_filename = graph_storage_path + "/" + country_code +  "_roads_igraph.p" 
    if graph_filename in os.listdir(graph_storage_path):
        print("Graph for " + country_name + " already stored.")
        return False

    # create networkx graph
    G_nx = ox.graph_from_place(country_name, network_type='all', simplify=True)
    G_nx = nx.relabel.convert_node_labels_to_integers(G_nx)

    print("Converting downloaded roads graph to igraph")
    # convert networkx graph to igraph
    G_ig = ig.Graph(directed=True)

    G_ig.add_vertices(list(G_nx.nodes()))
    G_ig.add_edges(list(G_nx.edges()))

    G_ig.vs['osmid'] = list(nx.get_node_attributes(G_nx, 'osmid').values())
    G_ig.vs['x'] = list(nx.get_node_attributes(G_nx, 'x').values())
    G_ig.vs['y'] = list(nx.get_node_attributes(G_nx, 'y').values())

    G_ig.es['length'] = list(nx.get_edge_attributes(G_nx, 'length').values())
    G_ig.es['weight'] = list(nx.get_edge_attributes(G_nx, 'length').values())
    G_ig.es['oneway'] = list(nx.get_edge_attributes(G_nx, 'oneway').values())
    G_ig.es['highway'] = list(nx.get_edge_attributes(G_nx, 'highway').values())

    # Verify conversion by comparing vertex and edge count 
    # of networkx graph and newly created igraph
    G_ig_num_v = G_ig.vcount()
    G_ig_num_e = G_ig.ecount()
    assert len(G_nx.nodes()) == G_ig.vcount()
    assert len(G_nx.edges()) == G_ig.ecount()

    print("Serializing igraph")
    pickle.dump(G_ig, open(graph_filename, "wb"))

    print("igraph storage for " + country_name + " roads completed")
    print(str(G_ig_num_v) + " vertices, " + str(G_ig_num_e) + " edges stored")

def main():
    with multiprocessing.Pool() as pool:
        pool.map(makeIGraph, countries)   

if __name__ == "__main__":
    main()
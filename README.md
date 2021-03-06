Scripts to download, store, analyze, and visualize road network graphs of UNICEF Programme Countries, used to preprocess MagicBox data. 

*Prerequisite:
Pull the docker image (which contains osmnx and igraph) from the Docker hub:
```
sudo docker pull msradam/magicbox-tools
```
Then run bash:
```
sudo docker run --rm -it -u 0 --name osmnx -v "$PWD":/home/jovyan/work msradam/magicbox-tools /bin/bash
```

*Usage (with fast graph library)*:

To download graphs for all UNICEF programme countries (listed in the repo):
```
python get_roads_ig.py <path to graph storage>
```
To download graph for a single country:
```
python store_igraph.py <name of country> <path to graph storage>
```
A pickled Python iGraph object is stored, labeled by alpha-2 country code. 

*Usage (to generate .csvs for other graph network tools)*:
```
python get_roads.py <path to graph storage>
```
For each country, the script will store two separate lists - a list of *edges*, and a list of *vertices*. 

An example layout for a list of Belize's road vertices (first two nodes shown):

| Node ID | Latitude | Longitude |
|------------|--------------|--------------|
| 261980179 | -14.3455195 | -170.7243363 |
| 4329701403 | -14.3368641  | -170.7830434 |

And for a list of Belize's road eges (first two edges shown):

| Source Node ID | Destination Node ID | Road Length (meters) | Source Node Latitude | Source Node Longitude | Destination Node Latitude | Destination Node Longitude | Oneway? (True/False) | Classificatio |
|----------------|---------------------|----------------------|----------------------|-----------------------|---------------------------|----------------------------|----------------------|---------------|
| 4326686740     | 4326686716          | 95.05000000000001    | 18.4626269           | -88.3022409           | 18.4624143                | -88.3030744                | False                | residential   |
| 4326686740     | 4326686711          | 112.534              | 18.4626269           | -88.3022409           | 18.4623914                | -88.3012395                | False                | unclassified  |

(Note: Column names are truncated in the .csv files)
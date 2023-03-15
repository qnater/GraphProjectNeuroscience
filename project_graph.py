import matplotlib as mpl
import networkx as nx

from explore.exploration_graph import explore_graph as eg
from visualization.visualization_graph import visualization_graph as vg

# QUENTIN NATER - 01.03.2023 - ASS 1 - EX 2
if __name__ == '__main__':
    print("\n==================================================")
    print("====Quentin=Nater=====UNI-FR======================")
    print("==================================================\n")

    mpl.use('TkAgg')  # without it, cannot run my plots (maybe personal)

    tag = "prod"  # prod or test

    if tag == "test":
        myGraph = nx.Graph()
        myGraph.add_nodes_from([1, 2, 3, 4, 5, 6, 7])
        myGraph.add_edges_from([(1, 2), (1, 4), (1, 7), (2, 5), (2, 6), (3, 5), (3, 6)])
        vg.display_simple_graph(myGraph)
    elif tag == "prod":
        graph = eg.construct_simple_file("./dataset/amazon-meta.txt", 100000)
        vg.display_simple_graph(graph)
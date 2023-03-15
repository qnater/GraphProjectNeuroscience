import networkx as nx
import random
import matplotlib.pyplot as plt
import matplotlib as mpl
import networkx as nx

class visualization_graph:

    # Quentin Nater
    # Display a simple graph sample with a file
    def display_simple_graph(myGraph):

        nx.draw(myGraph, with_labels=True)
        plt.show()

        return myGraph

    # Quentin Nater
    # Display a simple graph sample with a file - test
    def display_simple_file(file_name):
        myGraph = nx.read_edgelist(file_name, create_using=nx.DiGraph(), nodetype=int)

        # number of nodes to sample
        num_nodes = 1000

        # randomly sample nodes
        nodes_list = list(myGraph.nodes())
        sampled_nodes = random.sample(nodes_list, num_nodes)

        # create a subgraph with the sampled nodes and all their edges
        sampled_graph = myGraph.subgraph(sampled_nodes)

        # draw the sampled graph
        nx.draw(sampled_graph, with_labels=True)
        plt.show()




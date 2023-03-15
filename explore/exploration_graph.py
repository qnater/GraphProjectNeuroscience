import networkx as nx
import random
import matplotlib.pyplot as plt
import matplotlib as mpl
import re

class explore_graph:

    # Quentin Nater
    # Display a complex graph sample with a file - test
    def construct_complex_file(file_name):

        # create a new graph
        graph = nx.Graph()

        # read and extract every nodes and edges
        with open(file_name, "r", encoding='utf-8') as f:
            for line in f:

                # read nodes ===============================================
                asin = ""
                match = re.search(r'ASIN:\s*(\w+)', line)
                if match:
                    asin = match.group(1)
                    #print(str(asin))
                    # add a node to the graph for the ASIN value
                    graph.add_node(asin)

                # read edges ===============================================
                # use regular expressions to extract the ASIN value
                match = re.search(r'similar:\s*(\w+)', line)
                if match:
                    similars = line.split(sep="  ")

                    for similar in similars:
                        graph.add_edge(*(asin, similar))
                        #print("("+str(asin) + ", " + str(similar) + ")")

        print("The graph has been successfully constructed !")

        return graph




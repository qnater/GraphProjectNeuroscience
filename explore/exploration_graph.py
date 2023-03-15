import string

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


    def convert_asin_to_int(asin):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if any(char.isalpha() for char in asin):
            for char in asin:
                if char.isalpha():
                    asin = asin.replace(char, str(alphabet.index(char.upper()) + 10))

        return int(asin)

    # Quentin Nater
    # Display a complex graph sample with a file - test
    def construct_simple_file(file_name, limit):

        # create a new graph
        graph = nx.DiGraph()

        i, asin_int = 0, 0

        # read and extract every nodes and edges
        with open(file_name, "r", encoding='utf-8') as f:
            for line in f:
                i += 1
                # read nodes ===============================================

                match = re.search(r'ASIN:\s*(\w+)', line)
                if match:
                    asin = match.group(1)
                    # add a node to the graph for the ASIN value
                    asin_int = explore_graph.convert_asin_to_int(asin)
                    graph.add_node(asin_int)

                # read edges ===============================================
                # use regular expressions to extract the ASIN value
                match = re.search(r'similar:\s*(\w+)', line)
                if match:
                    similars = line.split(sep="  ")
                    inc = 0
                    for similar in similars:
                        inc += 1
                        if inc > 2:
                            similar_int = explore_graph.convert_asin_to_int(similar)
                            graph.add_edge(*(asin_int, similar_int))
                            print("("+str(asin_int) + ", " + str(similar_int) + ")")

                if i == limit:
                    break

        print("The graph has been successfully constructed !")

        return graph






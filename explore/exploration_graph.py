import math

import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt

class explore_graph:

    def explore_simple_graph(myGraph):

        nx.draw(myGraph, with_labels=True)
        plt.show()

        return myGraph
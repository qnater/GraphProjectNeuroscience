import networkx as nx


class AnalyticsGraph:

    # Creator : Quentin Nater
    # reviewed by :
    #
    # myGraph       : networkX - graph of the dataset
    #
    # Calculate the centrality betweenness of a graph with a library
    def centrality_betweenness_library(graph):
        print(">> You have called the centrality betweenness library for your graph")

        nodes = nx.betweenness_centrality(graph)

        for node in nodes.keys():
            if nodes[node] > 0:
                print("\t\t\t\t" + str(node) + " : " + str(nodes[node]))

        return nodes
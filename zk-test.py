#!/usr/bin/env python3

import sys
import networkx as nx
import matplotlib.pyplot as plt   # ass python3-matplotlib

g = nx.MultiDiGraph()
g.add_node('fred')
g.add_node('bill')
g.add_node('mary')
g.add_nodes_from(["julie","arthur"])

g.add_edge('fred', 'mary')
g.add_edge('arthur', 'fred')
g.add_edge('fred', 'bill')
g.add_edge('mary', 'julie')
g.add_edge('mary', 'arthur')
g.add_edge('bill', 'arthur')
g.add_edge('wendy', 'fred')
g.add_edge('julie', 'bill')

#g = nx.relabel_nodes(g,{'fred':'f r e d'}, copy=False)

print("=======")
print('Directed:', nx.is_directed(g))
print('Nodes:', g.nodes())
print('Edges:', g.edges())
print("=======")
print('Fred ->', g.successors('fred'))
print('Fred <-', g.predecessors('fred'))
print("=======", flush=True)

sys.stderr = None  # suppress matlibplot messages

nx.draw(g, with_labels=True)
plt.savefig("path_graph1.png")
plt.show()



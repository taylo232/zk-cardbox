#!/usr/bin/env python3

import sys
import networkx as nx                  # dep python3-networkx
import matplotlib.pyplot as plt        # dep python3-matplotlib

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
g.add_edge('julie', 'arthur')
g.add_edge('mary', 'bill')
g.add_edge('wendy', 'arthur')
g.add_edge('fred', 'julie')

#g = nx.relabel_nodes(g,{'fred':'f r e d'}, copy=False)

print("=======")
print('Directed Graph:', nx.is_directed(g))
print("=======")
foo = g.nodes()
print('Nodes:',type(foo), foo)
print("=======")
foo = g.edges()
print('Edges:', type(foo), foo)
print("=======")
print('Fred ->', g.successors('fred'))
print('Fred <-', g.predecessors('fred'))
print("=======", flush=True)

sys.stderr = None                      # suppress matlibplot messages

nx.draw(g, with_labels=True)
plt.savefig("zk.png")
plt.show()

sys.stderr = sys.__stderr__            # suppress matlibplot messages

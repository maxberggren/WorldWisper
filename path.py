#!/usr/bin/python
# -*- coding: utf-8 -*-

from config import *
from gengo import Gengo
import json
import networkx as nx
import matplotlib.pyplot as plt
from sets import Set

def pretty(fromgengo):
    return json.dumps(fromgengo,
                      sort_keys=True,
                      indent=4, 
                      separators=(',', ': '))

gengo = Gengo(
    public_key=PUBLIC_KEY,
    private_key=PRIVATE_KEY,
    sandbox=True,
)

G = nx.Graph()
languages = Set()

for row in gengo.getServiceLanguagePairs()['response']:
    # Wierdly enough we start by adding the edges
    G.add_edge(row['lc_src'], row['lc_tgt'], time=1)

# Make all languages nodes
for language in languages:
    G.add_node(language)

#pos = nx.spring_layout(G)
pos = nx.shell_layout(G)

nx.draw_networkx_edges(G, pos, width=2.0, alpha=0.5)
nx.draw_networkx_nodes(G, pos, node_color='w', node_size=500, alpha=1)

labels={}
for item in nx.nodes(G):
    labels[item] = item

nx.draw_networkx_labels(G, pos, labels, font_size=10)

plt.axis('off')
plt.show()

print pretty(nx.all_pairs_shortest_path(G, cutoff=30))
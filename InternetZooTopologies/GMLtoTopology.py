import os
import os.path as op
from inspect import stack
import networkx as nx
import sys

def InitFileTopo(name):
    file_topo = open("Topologies/" + name + ".py", "w")
    file_topo.write("""#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink""" + "\n\n")
    file_topo.write("class " + name + "(Topo):\n" )
    file_topo.write("""    def __init__(self):
        Topo.__init__(self)\n\n""")
    file_topo.close()


def format_string(s):
    tmp = s.lower().replace(" ", "")[:8]

    if len(s) > 8 and s[-1].isdigit():
        tmp += s[-1]
    
    return tmp

#for file in os.listdir('DatasetGML'):
nameTopo="Aarnet"
graph = nx.read_gml(op.join('DatasetGML', nameTopo + '.gml'))
InitFileTopo("Aarnet")
file_topo = open("Topologies/Aarnet.py", "a")

file_topo.write("       #Adding Switches\n")
i=0
for name, properties in graph.nodes.items():
    i=i+1
    name = format_string(name)
    dpid = ("%016x" % (i + 1))
    file_topo.write("        " + name + ' = self.addSwitch(\'' + name + '\', dpid=\'' + dpid + '\')\n')

file_topo.write("\n           #Adding Links\n")
i=0
for links in graph.edges():
    file_topo.write('        self.addLink(' + format_string(str(links[0])) + ' , ' + format_string(str(links[1])) + ')\n' )

file_topo.write("\ntopos = { \'" + nameTopo + "\': ( lambda: "+nameTopo+"() ) }")

file_topo.close()



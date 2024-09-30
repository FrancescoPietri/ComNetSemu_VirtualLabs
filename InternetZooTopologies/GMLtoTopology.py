import os
import os.path as op
from inspect import stack
import networkx as nx
import sys
import black
import re
from mininet.link import TCLink
import random

LINK0_CONF = dict(delay='20ms', use_tbf=True, bw=20, max_queue_size=10, burst=1000000)
LINK1_CONF = dict(delay='25ms', use_tbf=True, bw=50, max_queue_size=10,  burst=1000000)
DEF_DICT_LINKS_CONF = {
    0: LINK0_CONF,
    1: LINK1_CONF
}

class GMLtoTopology:
    def __init__(self):
        pass

    def init_topo(self, name, topologyDirPath):
        file_topo = open(op.join(topologyDirPath, name + ".py"), "w")
        file_topo.write("""#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink\n\n""")
        file_topo.write(f"class {name}(Topo):\n")
        file_topo.write(" def __init__(self):\n")
        file_topo.write("  Topo.__init__(self)\n")
        file_topo.close()

    def refactor_file(self, file_path):
        with open(file_path, 'r') as file:
            code = file.read()

        formatted_code = black.format_str(code, mode=black.FileMode())

        with open(file_path, 'w') as file:
            file.write(formatted_code)


    def convert_gml_topo(self, name, datasetDirPath, topologyDirPath, flagLK=False, dictLinkConf=DEF_DICT_LINKS_CONF):
        random.seed()

        name = os.path.splitext(name)[0]

        graph = nx.read_gml(op.join(datasetDirPath, name + '.gml'), "id")

        self.init_topo(name, topologyDirPath)

        with open(op.join(topologyDirPath, name + ".py"), "a") as file_topo:
            file_topo.write("  # Adding Switches\n")
            i = 0
            for node_name, properties in graph.nodes.items():
                i += 1
                node_name = "s" + str(node_name)
                dpid = f"{i + 1:016x}"
                file_topo.write(f"  s{i-1} = self.addSwitch('{node_name}', dpid='{dpid}')\n")

            file_topo.write("\n  # Adding Links\n")
            if flagLK:
                i=0
                for linkCONF in dictLinkConf:
                    file_topo.write(f"  link{i}_conf = {str(dictLinkConf[linkCONF])}\n")
                    i=i+1


            for link in graph.edges():
                if not flagLK:
                    file_topo.write(f"  self.addLink(s{str(link[0])}, s{str(link[1])})\n")
                else:
                    randLinkConf = random.randint(0,len(dictLinkConf)-1)
                    file_topo.write(f"  self.addLink(s{str(link[0])}, s{str(link[1])}, **link{randLinkConf}_conf)\n")
                
                    

            file_topo.write(f"\ntopos = {{ '{name}': (lambda: {name}()) }}")

        self.refactor_file(op.join(topologyDirPath, name + ".py"))







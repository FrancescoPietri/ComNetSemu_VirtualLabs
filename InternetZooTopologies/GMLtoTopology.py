import os
import os.path as op
from inspect import stack
import networkx as nx
import sys
import black
import re

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

    def format_string(self, s):
        tmp = s.lower().replace(" ", "")[:8]

        tmp = re.sub(r'[^a-zA-Z0-9]', '', tmp)

        if len(s) > 8 and s[-1].isdigit():
            tmp += s[-1]
        
        return tmp

    def refactor_file(self, file_path):
        with open(file_path, 'r') as file:
            code = file.read()

        formatted_code = black.format_str(code, mode=black.FileMode())

        with open(file_path, 'w') as file:
            file.write(formatted_code)

    """def standardize_gml(name):
        file_gml = open"""

    def convert_gml_topo(self, name, datasetDirPath, topologyDirPath):

        name = os.path.splitext(name)[0]

        graph = nx.read_gml(op.join(datasetDirPath, name + '.gml'), "id")

        self.init_topo(name, topologyDirPath)

        with open(op.join(topologyDirPath, name + ".py"), "a") as file_topo:
            file_topo.write("  # Adding Switches\n")
            i = 0
            for node_name, properties in graph.nodes.items():
                i += 1
                node_name = properties['label'] + str(node_name)
                node_name = self.format_string(node_name)
                dpid = f"{i + 1:016x}"
                file_topo.write(f"  s{i-1} = self.addSwitch('{node_name}', dpid='{dpid}')\n")

            file_topo.write("\n  # Adding Links\n")
            for link in graph.edges():
                file_topo.write(f"  self.addLink(s{self.format_string(str(link[0]))}, s{self.format_string(str(link[1]))})\n")

            file_topo.write(f"\ntopos = {{ '{name}': (lambda: {name}()) }}")

        self.refactor_file(op.join(topologyDirPath, name + ".py"))







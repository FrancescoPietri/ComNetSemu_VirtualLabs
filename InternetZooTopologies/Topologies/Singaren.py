#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Singaren(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        nictqgpo = self.addSwitch("nictqgpo", dpid="0000000000000002")
        aarnet = self.addSwitch("aarnet", dpid="0000000000000003")
        academia = self.addSwitch("academia", dpid="0000000000000004")
        ntu = self.addSwitch("ntu", dpid="0000000000000005")
        biopolis = self.addSwitch("biopolis", dpid="0000000000000006")
        fusionop = self.addSwitch("fusionop", dpid="0000000000000007")
        nus = self.addSwitch("nus", dpid="0000000000000008")
        schools = self.addSwitch("schools", dpid="0000000000000009")
        singaren = self.addSwitch("singaren", dpid="000000000000000a")
        singaren = self.addSwitch("singaren", dpid="000000000000000b")
        tein3 = self.addSwitch("tein3", dpid="000000000000000c")

        # Adding Links
        self.addLink(nictqgpo, singaren)
        self.addLink(aarnet, singaren)
        self.addLink(academia, singaren)
        self.addLink(ntu, singaren)
        self.addLink(biopolis, singaren)
        self.addLink(fusionop, singaren)
        self.addLink(nus, singaren)
        self.addLink(schools, singaren)
        self.addLink(singaren, singaren)
        self.addLink(singaren, tein3)


topos = {"Singaren": (lambda: Singaren())}

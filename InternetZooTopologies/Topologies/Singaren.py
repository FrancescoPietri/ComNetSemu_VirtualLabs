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
        s0 = self.addSwitch("nictqgpo0", dpid="0000000000000002")
        s1 = self.addSwitch("aarnet1", dpid="0000000000000003")
        s2 = self.addSwitch("academia2", dpid="0000000000000004")
        s3 = self.addSwitch("ntu3", dpid="0000000000000005")
        s4 = self.addSwitch("biopolis4", dpid="0000000000000006")
        s5 = self.addSwitch("fusionop5", dpid="0000000000000007")
        s6 = self.addSwitch("nus6", dpid="0000000000000008")
        s7 = self.addSwitch("schools7", dpid="0000000000000009")
        s8 = self.addSwitch("singaren8", dpid="000000000000000a")
        s9 = self.addSwitch("singaren9", dpid="000000000000000b")
        s10 = self.addSwitch("tein310", dpid="000000000000000c")

        # Adding Links
        self.addLink(s0, s9)
        self.addLink(s1, s9)
        self.addLink(s2, s9)
        self.addLink(s3, s9)
        self.addLink(s4, s9)
        self.addLink(s5, s9)
        self.addLink(s6, s9)
        self.addLink(s7, s9)
        self.addLink(s8, s9)
        self.addLink(s9, s10)


topos = {"Singaren": (lambda: Singaren())}

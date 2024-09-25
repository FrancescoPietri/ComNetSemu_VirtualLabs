#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class HiberniaUk(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("london0", dpid="0000000000000002")
        s1 = self.addSwitch("southpor1", dpid="0000000000000003")
        s2 = self.addSwitch("none2", dpid="0000000000000004")
        s3 = self.addSwitch("none3", dpid="0000000000000005")
        s4 = self.addSwitch("manchest4", dpid="0000000000000006")
        s5 = self.addSwitch("peterbor5", dpid="0000000000000007")
        s6 = self.addSwitch("cambridg6", dpid="0000000000000008")
        s7 = self.addSwitch("sheffiel7", dpid="0000000000000009")
        s8 = self.addSwitch("leiceste8", dpid="000000000000000a")
        s9 = self.addSwitch("bracewel9", dpid="000000000000000b")
        s10 = self.addSwitch("leeds10", dpid="000000000000000c")
        s11 = self.addSwitch("birmingh1", dpid="000000000000000d")
        s12 = self.addSwitch("liverpoo2", dpid="000000000000000e")
        s13 = self.addSwitch("reading13", dpid="000000000000000f")
        s14 = self.addSwitch("bristol14", dpid="0000000000000010")

        # Adding Links
        self.addLink(s0, s3)
        self.addLink(s0, s13)
        self.addLink(s0, s6)
        self.addLink(s1, s9)
        self.addLink(s1, s12)
        self.addLink(s2, s13)
        self.addLink(s4, s11)
        self.addLink(s4, s12)
        self.addLink(s5, s8)
        self.addLink(s5, s6)
        self.addLink(s7, s8)
        self.addLink(s7, s10)
        self.addLink(s9, s10)
        self.addLink(s11, s14)
        self.addLink(s13, s14)


topos = {"HiberniaUk": (lambda: HiberniaUk())}

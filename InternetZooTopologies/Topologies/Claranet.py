#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Claranet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("faro0", dpid="0000000000000002")
        s1 = self.addSwitch("madrid1", dpid="0000000000000003")
        s2 = self.addSwitch("porto2", dpid="0000000000000004")
        s3 = self.addSwitch("lisbon3", dpid="0000000000000005")
        s4 = self.addSwitch("barcelon4", dpid="0000000000000006")
        s5 = self.addSwitch("manchest5", dpid="0000000000000007")
        s6 = self.addSwitch("newyork66", dpid="0000000000000008")
        s7 = self.addSwitch("amsterda7", dpid="0000000000000009")
        s8 = self.addSwitch("eindhove8", dpid="000000000000000a")
        s9 = self.addSwitch("berlin9", dpid="000000000000000b")
        s10 = self.addSwitch("frankfur0", dpid="000000000000000c")
        s11 = self.addSwitch("munich11", dpid="000000000000000d")
        s12 = self.addSwitch("paris12", dpid="000000000000000e")
        s13 = self.addSwitch("rennes13", dpid="000000000000000f")
        s14 = self.addSwitch("london14", dpid="0000000000000010")

        # Adding Links
        self.addLink(s0, s3)
        self.addLink(s1, s3)
        self.addLink(s1, s4)
        self.addLink(s2, s3)
        self.addLink(s3, s14)
        self.addLink(s4, s12)
        self.addLink(s5, s14)
        self.addLink(s6, s14)
        self.addLink(s7, s8)
        self.addLink(s7, s10)
        self.addLink(s7, s14)
        self.addLink(s9, s10)
        self.addLink(s9, s11)
        self.addLink(s10, s11)
        self.addLink(s10, s12)
        self.addLink(s10, s14)
        self.addLink(s12, s13)
        self.addLink(s12, s14)


topos = {"Claranet": (lambda: Claranet())}

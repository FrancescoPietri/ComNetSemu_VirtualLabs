#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Globalcenter(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("minneapo0", dpid="0000000000000002")
        s1 = self.addSwitch("seattle1", dpid="0000000000000003")
        s2 = self.addSwitch("sanjose22", dpid="0000000000000004")
        s3 = self.addSwitch("phoenix3", dpid="0000000000000005")
        s4 = self.addSwitch("dallas4", dpid="0000000000000006")
        s5 = self.addSwitch("atlanta5", dpid="0000000000000007")
        s6 = self.addSwitch("vienna6", dpid="0000000000000008")
        s7 = self.addSwitch("whippany7", dpid="0000000000000009")
        s8 = self.addSwitch("chicago8", dpid="000000000000000a")

        # Adding Links
        self.addLink(s0, s1)
        self.addLink(s0, s2)
        self.addLink(s0, s3)
        self.addLink(s0, s4)
        self.addLink(s0, s5)
        self.addLink(s0, s6)
        self.addLink(s0, s7)
        self.addLink(s0, s8)
        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s1, s4)
        self.addLink(s1, s5)
        self.addLink(s1, s6)
        self.addLink(s1, s7)
        self.addLink(s1, s8)
        self.addLink(s2, s3)
        self.addLink(s2, s4)
        self.addLink(s2, s5)
        self.addLink(s2, s6)
        self.addLink(s2, s7)
        self.addLink(s2, s8)
        self.addLink(s3, s4)
        self.addLink(s3, s5)
        self.addLink(s3, s6)
        self.addLink(s3, s7)
        self.addLink(s3, s8)
        self.addLink(s4, s5)
        self.addLink(s4, s6)
        self.addLink(s4, s7)
        self.addLink(s4, s8)
        self.addLink(s5, s6)
        self.addLink(s5, s7)
        self.addLink(s5, s8)
        self.addLink(s6, s7)
        self.addLink(s6, s8)
        self.addLink(s7, s8)


topos = {"Globalcenter": (lambda: Globalcenter())}

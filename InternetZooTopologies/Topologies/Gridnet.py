#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Gridnet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("houston0", dpid="0000000000000002")
        s1 = self.addSwitch("sanfranc1", dpid="0000000000000003")
        s2 = self.addSwitch("losangel2", dpid="0000000000000004")
        s3 = self.addSwitch("newyork33", dpid="0000000000000005")
        s4 = self.addSwitch("newark4", dpid="0000000000000006")
        s5 = self.addSwitch("washingt5", dpid="0000000000000007")
        s6 = self.addSwitch("atlanta6", dpid="0000000000000008")
        s7 = self.addSwitch("dallas7", dpid="0000000000000009")
        s8 = self.addSwitch("miami8", dpid="000000000000000a")

        # Adding Links
        self.addLink(s0, s8)
        self.addLink(s0, s2)
        self.addLink(s0, s3)
        self.addLink(s0, s7)
        self.addLink(s1, s2)
        self.addLink(s1, s4)
        self.addLink(s1, s5)
        self.addLink(s1, s6)
        self.addLink(s1, s7)
        self.addLink(s2, s3)
        self.addLink(s2, s8)
        self.addLink(s3, s8)
        self.addLink(s3, s4)
        self.addLink(s4, s5)
        self.addLink(s4, s6)
        self.addLink(s4, s7)
        self.addLink(s5, s6)
        self.addLink(s5, s7)
        self.addLink(s6, s8)
        self.addLink(s6, s7)


topos = {"Gridnet": (lambda: Gridnet())}

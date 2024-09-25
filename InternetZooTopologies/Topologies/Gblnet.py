#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Gblnet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("newyork00", dpid="0000000000000002")
        s1 = self.addSwitch("london1", dpid="0000000000000003")
        s2 = self.addSwitch("stockhol2", dpid="0000000000000004")
        s3 = self.addSwitch("stpeters3", dpid="0000000000000005")
        s4 = self.addSwitch("moscow4", dpid="0000000000000006")
        s5 = self.addSwitch("amsterda5", dpid="0000000000000007")
        s6 = self.addSwitch("frankfur6", dpid="0000000000000008")
        s7 = self.addSwitch("paris7", dpid="0000000000000009")

        # Adding Links
        self.addLink(s0, s5)
        self.addLink(s1, s5)
        self.addLink(s2, s3)
        self.addLink(s2, s5)
        self.addLink(s3, s4)
        self.addLink(s5, s6)
        self.addLink(s5, s7)


topos = {"Gblnet": (lambda: Gblnet())}

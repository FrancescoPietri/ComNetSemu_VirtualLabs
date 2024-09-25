#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Nsfcnet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("pekingun0", dpid="0000000000000002")
        s1 = self.addSwitch("cernet1", dpid="0000000000000003")
        s2 = self.addSwitch("apansta2", dpid="0000000000000004")
        s3 = self.addSwitch("cernet3", dpid="0000000000000005")
        s4 = self.addSwitch("tsinghua4", dpid="0000000000000006")
        s5 = self.addSwitch("naturals5", dpid="0000000000000007")
        s6 = self.addSwitch("beijingu6", dpid="0000000000000008")
        s7 = self.addSwitch("beijingu7", dpid="0000000000000009")
        s8 = self.addSwitch("chinaaca8", dpid="000000000000000a")
        s9 = self.addSwitch("cstnet9", dpid="000000000000000b")

        # Adding Links
        self.addLink(s0, s8)
        self.addLink(s0, s4)
        self.addLink(s2, s4)
        self.addLink(s3, s4)
        self.addLink(s4, s5)
        self.addLink(s4, s7)
        self.addLink(s4, s8)
        self.addLink(s5, s6)
        self.addLink(s6, s7)
        self.addLink(s8, s9)


topos = {"Nsfcnet": (lambda: Nsfcnet())}

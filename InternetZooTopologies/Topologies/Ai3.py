#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Ai3(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("unibraw0", dpid="0000000000000002")
        s1 = self.addSwitch("naist1", dpid="0000000000000003")
        s2 = self.addSwitch("keio2", dpid="0000000000000004")
        s3 = self.addSwitch("ioit3", dpid="0000000000000005")
        s4 = self.addSwitch("asti4", dpid="0000000000000006")
        s5 = self.addSwitch("tu5", dpid="0000000000000007")
        s6 = self.addSwitch("ait6", dpid="0000000000000008")
        s7 = self.addSwitch("itb7", dpid="0000000000000009")
        s8 = self.addSwitch("tp8", dpid="000000000000000a")
        s9 = self.addSwitch("usm9", dpid="000000000000000b")

        # Adding Links
        self.addLink(s0, s7)
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s2, s4)
        self.addLink(s2, s6)
        self.addLink(s2, s7)
        self.addLink(s2, s8)
        self.addLink(s2, s9)
        self.addLink(s5, s6)


topos = {"Ai3": (lambda: Ai3())}

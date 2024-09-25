#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Abilene(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("newyork00", dpid="0000000000000002")
        s1 = self.addSwitch("chicago1", dpid="0000000000000003")
        s2 = self.addSwitch("washingt2", dpid="0000000000000004")
        s3 = self.addSwitch("seattle3", dpid="0000000000000005")
        s4 = self.addSwitch("sunnyval4", dpid="0000000000000006")
        s5 = self.addSwitch("losangel5", dpid="0000000000000007")
        s6 = self.addSwitch("denver6", dpid="0000000000000008")
        s7 = self.addSwitch("kansasci7", dpid="0000000000000009")
        s8 = self.addSwitch("houston8", dpid="000000000000000a")
        s9 = self.addSwitch("atlanta9", dpid="000000000000000b")
        s10 = self.addSwitch("indianap0", dpid="000000000000000c")

        # Adding Links
        self.addLink(s0, s1)
        self.addLink(s0, s2)
        self.addLink(s1, s10)
        self.addLink(s2, s9)
        self.addLink(s3, s4)
        self.addLink(s3, s6)
        self.addLink(s4, s5)
        self.addLink(s4, s6)
        self.addLink(s5, s8)
        self.addLink(s6, s7)
        self.addLink(s7, s8)
        self.addLink(s7, s10)
        self.addLink(s8, s9)
        self.addLink(s9, s10)


topos = {"Abilene": (lambda: Abilene())}

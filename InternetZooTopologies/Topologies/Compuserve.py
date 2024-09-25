#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Compuserve(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("10", dpid="0000000000000002")
        s1 = self.addSwitch("11", dpid="0000000000000003")
        s2 = self.addSwitch("washingt2", dpid="0000000000000004")
        s3 = self.addSwitch("13", dpid="0000000000000005")
        s4 = self.addSwitch("boston4", dpid="0000000000000006")
        s5 = self.addSwitch("newyork55", dpid="0000000000000007")
        s6 = self.addSwitch("seattle6", dpid="0000000000000008")
        s7 = self.addSwitch("sanfranc7", dpid="0000000000000009")
        s8 = self.addSwitch("losangel8", dpid="000000000000000a")
        s9 = self.addSwitch("dallas9", dpid="000000000000000b")
        s10 = self.addSwitch("houston10", dpid="000000000000000c")
        s11 = self.addSwitch("atlanta11", dpid="000000000000000d")
        s12 = self.addSwitch("columbus2", dpid="000000000000000e")
        s13 = self.addSwitch("chicago13", dpid="000000000000000f")

        # Adding Links
        self.addLink(s0, s12)
        self.addLink(s1, s12)
        self.addLink(s2, s11)
        self.addLink(s2, s12)
        self.addLink(s2, s5)
        self.addLink(s3, s12)
        self.addLink(s4, s5)
        self.addLink(s4, s13)
        self.addLink(s6, s13)
        self.addLink(s6, s7)
        self.addLink(s7, s8)
        self.addLink(s7, s12)
        self.addLink(s8, s9)
        self.addLink(s9, s10)
        self.addLink(s9, s12)
        self.addLink(s10, s11)
        self.addLink(s12, s13)


topos = {"Compuserve": (lambda: Compuserve())}

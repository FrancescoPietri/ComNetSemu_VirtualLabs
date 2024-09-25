#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Ans(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("hartford0", dpid="0000000000000002")
        s1 = self.addSwitch("newyork11", dpid="0000000000000003")
        s2 = self.addSwitch("chicago2", dpid="0000000000000004")
        s3 = self.addSwitch("clevelan3", dpid="0000000000000005")
        s4 = self.addSwitch("greensbo4", dpid="0000000000000006")
        s5 = self.addSwitch("atlanta5", dpid="0000000000000007")
        s6 = self.addSwitch("washingt6", dpid="0000000000000008")
        s7 = self.addSwitch("reston7", dpid="0000000000000009")
        s8 = self.addSwitch("dallas8", dpid="000000000000000a")
        s9 = self.addSwitch("stlouis99", dpid="000000000000000b")
        s10 = self.addSwitch("seattle10", dpid="000000000000000c")
        s11 = self.addSwitch("denver11", dpid="000000000000000d")
        s12 = self.addSwitch("sanfranc2", dpid="000000000000000e")
        s13 = self.addSwitch("sanjose13", dpid="000000000000000f")
        s14 = self.addSwitch("losangel4", dpid="0000000000000010")
        s15 = self.addSwitch("albuquer5", dpid="0000000000000011")
        s16 = self.addSwitch("hawaii16", dpid="0000000000000012")
        s17 = self.addSwitch("houston17", dpid="0000000000000013")

        # Adding Links
        self.addLink(s0, s1)
        self.addLink(s0, s3)
        self.addLink(s1, s3)
        self.addLink(s1, s6)
        self.addLink(s1, s7)
        self.addLink(s2, s3)
        self.addLink(s2, s9)
        self.addLink(s2, s11)
        self.addLink(s4, s5)
        self.addLink(s4, s6)
        self.addLink(s5, s17)
        self.addLink(s6, s7)
        self.addLink(s7, s8)
        self.addLink(s7, s9)
        self.addLink(s8, s9)
        self.addLink(s8, s13)
        self.addLink(s8, s17)
        self.addLink(s10, s11)
        self.addLink(s10, s12)
        self.addLink(s11, s12)
        self.addLink(s12, s13)
        self.addLink(s12, s14)
        self.addLink(s14, s15)
        self.addLink(s15, s16)
        self.addLink(s15, s17)


topos = {"Ans": (lambda: Ans())}

#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Atmnet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("saltlake0", dpid="0000000000000002")
        s1 = self.addSwitch("minneapo1", dpid="0000000000000003")
        s2 = self.addSwitch("kansasci2", dpid="0000000000000004")
        s3 = self.addSwitch("denver3", dpid="0000000000000005")
        s4 = self.addSwitch("pittsbur4", dpid="0000000000000006")
        s5 = self.addSwitch("philadel5", dpid="0000000000000007")
        s6 = self.addSwitch("chicago6", dpid="0000000000000008")
        s7 = self.addSwitch("detroit7", dpid="0000000000000009")
        s8 = self.addSwitch("newyork88", dpid="000000000000000a")
        s9 = self.addSwitch("washingt9", dpid="000000000000000b")
        s10 = self.addSwitch("losangel0", dpid="000000000000000c")
        s11 = self.addSwitch("houston11", dpid="000000000000000d")
        s12 = self.addSwitch("stlouis12", dpid="000000000000000e")
        s13 = self.addSwitch("seattle13", dpid="000000000000000f")
        s14 = self.addSwitch("oakland14", dpid="0000000000000010")
        s15 = self.addSwitch("santacla5", dpid="0000000000000011")
        s16 = self.addSwitch("atlanta16", dpid="0000000000000012")
        s17 = self.addSwitch("sandiego7", dpid="0000000000000013")
        s18 = self.addSwitch("phoenix18", dpid="0000000000000014")
        s19 = self.addSwitch("tucson19", dpid="0000000000000015")
        s20 = self.addSwitch("dallas20", dpid="0000000000000016")

        # Adding Links
        self.addLink(s0, s3)
        self.addLink(s0, s14)
        self.addLink(s1, s6)
        self.addLink(s2, s3)
        self.addLink(s2, s12)
        self.addLink(s4, s5)
        self.addLink(s4, s7)
        self.addLink(s5, s8)
        self.addLink(s6, s12)
        self.addLink(s6, s7)
        self.addLink(s8, s9)
        self.addLink(s9, s16)
        self.addLink(s10, s17)
        self.addLink(s10, s15)
        self.addLink(s11, s16)
        self.addLink(s11, s12)
        self.addLink(s11, s20)
        self.addLink(s13, s14)
        self.addLink(s14, s15)
        self.addLink(s17, s18)
        self.addLink(s18, s19)
        self.addLink(s19, s20)


topos = {"Atmnet": (lambda: Atmnet())}

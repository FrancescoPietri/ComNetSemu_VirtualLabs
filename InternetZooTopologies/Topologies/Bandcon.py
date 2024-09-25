#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Bandcon(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("paris0", dpid="0000000000000002")
        s1 = self.addSwitch("atlanta1", dpid="0000000000000003")
        s2 = self.addSwitch("brussels2", dpid="0000000000000004")
        s3 = self.addSwitch("frankfur3", dpid="0000000000000005")
        s4 = self.addSwitch("phoenix4", dpid="0000000000000006")
        s5 = self.addSwitch("lasvegas5", dpid="0000000000000007")
        s6 = self.addSwitch("miami6", dpid="0000000000000008")
        s7 = self.addSwitch("dallas7", dpid="0000000000000009")
        s8 = self.addSwitch("losangel8", dpid="000000000000000a")
        s9 = self.addSwitch("houston9", dpid="000000000000000b")
        s10 = self.addSwitch("philadel0", dpid="000000000000000c")
        s11 = self.addSwitch("boston11", dpid="000000000000000d")
        s12 = self.addSwitch("london12", dpid="000000000000000e")
        s13 = self.addSwitch("amsterda3", dpid="000000000000000f")
        s14 = self.addSwitch("sanjose14", dpid="0000000000000010")
        s15 = self.addSwitch("sanfranc5", dpid="0000000000000011")
        s16 = self.addSwitch("seattle16", dpid="0000000000000012")
        s17 = self.addSwitch("chicago17", dpid="0000000000000013")
        s18 = self.addSwitch("toronto18", dpid="0000000000000014")
        s19 = self.addSwitch("ashburn19", dpid="0000000000000015")
        s20 = self.addSwitch("newjerse0", dpid="0000000000000016")
        s21 = self.addSwitch("newyork21", dpid="0000000000000017")

        # Adding Links
        self.addLink(s0, s3)
        self.addLink(s0, s12)
        self.addLink(s1, s19)
        self.addLink(s1, s6)
        self.addLink(s2, s3)
        self.addLink(s2, s13)
        self.addLink(s4, s8)
        self.addLink(s4, s7)
        self.addLink(s5, s8)
        self.addLink(s5, s14)
        self.addLink(s6, s7)
        self.addLink(s7, s9)
        self.addLink(s7, s19)
        self.addLink(s7, s17)
        self.addLink(s8, s14)
        self.addLink(s10, s18)
        self.addLink(s10, s19)
        self.addLink(s11, s18)
        self.addLink(s11, s21)
        self.addLink(s12, s13)
        self.addLink(s12, s21)
        self.addLink(s13, s19)
        self.addLink(s14, s17)
        self.addLink(s14, s15)
        self.addLink(s15, s16)
        self.addLink(s16, s17)
        self.addLink(s17, s18)
        self.addLink(s17, s19)


topos = {"Bandcon": (lambda: Bandcon())}

#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Xeex(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("denver0", dpid="0000000000000002")
        s1 = self.addSwitch("lasvegas1", dpid="0000000000000003")
        s2 = self.addSwitch("indianap2", dpid="0000000000000004")
        s3 = self.addSwitch("nashvill3", dpid="0000000000000005")
        s4 = self.addSwitch("phoenix4", dpid="0000000000000006")
        s5 = self.addSwitch("hongkong5", dpid="0000000000000007")
        s6 = self.addSwitch("sanfranc6", dpid="0000000000000008")
        s7 = self.addSwitch("sandiego7", dpid="0000000000000009")
        s8 = self.addSwitch("tokyo8", dpid="000000000000000a")
        s9 = self.addSwitch("chennai9", dpid="000000000000000b")
        s10 = self.addSwitch("london10", dpid="000000000000000c")
        s11 = self.addSwitch("pittsbur1", dpid="000000000000000d")
        s12 = self.addSwitch("columbus2", dpid="000000000000000e")
        s13 = self.addSwitch("amsterda3", dpid="000000000000000f")
        s14 = self.addSwitch("miami14", dpid="0000000000000010")
        s15 = self.addSwitch("cincinna5", dpid="0000000000000011")
        s16 = self.addSwitch("seattle16", dpid="0000000000000012")
        s17 = self.addSwitch("sanjose17", dpid="0000000000000013")
        s18 = self.addSwitch("losangel8", dpid="0000000000000014")
        s19 = self.addSwitch("chicago19", dpid="0000000000000015")
        s20 = self.addSwitch("ashburn20", dpid="0000000000000016")
        s21 = self.addSwitch("newyork21", dpid="0000000000000017")
        s22 = self.addSwitch("atlanta22", dpid="0000000000000018")
        s23 = self.addSwitch("dallas23", dpid="0000000000000019")

        # Adding Links
        self.addLink(s0, s1)
        self.addLink(s0, s19)
        self.addLink(s1, s18)
        self.addLink(s2, s19)
        self.addLink(s2, s12)
        self.addLink(s3, s15)
        self.addLink(s3, s22)
        self.addLink(s3, s23)
        self.addLink(s4, s18)
        self.addLink(s4, s7)
        self.addLink(s4, s23)
        self.addLink(s5, s8)
        self.addLink(s5, s9)
        self.addLink(s5, s18)
        self.addLink(s6, s16)
        self.addLink(s6, s17)
        self.addLink(s7, s18)
        self.addLink(s8, s17)
        self.addLink(s8, s9)
        self.addLink(s10, s21)
        self.addLink(s11, s12)
        self.addLink(s11, s20)
        self.addLink(s13, s20)
        self.addLink(s14, s20)
        self.addLink(s14, s22)
        self.addLink(s15, s19)
        self.addLink(s16, s19)
        self.addLink(s17, s18)
        self.addLink(s17, s19)
        self.addLink(s19, s21)
        self.addLink(s19, s23)
        self.addLink(s20, s22)
        self.addLink(s20, s21)
        self.addLink(s22, s23)


topos = {"Xeex": (lambda: Xeex())}

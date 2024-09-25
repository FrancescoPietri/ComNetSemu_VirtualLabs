#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Abvt(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("washingt0", dpid="0000000000000002")
        s1 = self.addSwitch("newyork11", dpid="0000000000000003")
        s2 = self.addSwitch("atlanta2", dpid="0000000000000004")
        s3 = self.addSwitch("miami3", dpid="0000000000000005")
        s4 = self.addSwitch("boston4", dpid="0000000000000006")
        s5 = self.addSwitch("london5", dpid="0000000000000007")
        s6 = self.addSwitch("philadel6", dpid="0000000000000008")
        s7 = self.addSwitch("baltimor7", dpid="0000000000000009")
        s8 = self.addSwitch("amsterda8", dpid="000000000000000a")
        s9 = self.addSwitch("frankfur9", dpid="000000000000000b")
        s10 = self.addSwitch("houston10", dpid="000000000000000c")
        s11 = self.addSwitch("none11", dpid="000000000000000d")
        s12 = self.addSwitch("paris12", dpid="000000000000000e")
        s13 = self.addSwitch("dallas13", dpid="000000000000000f")
        s14 = self.addSwitch("austin14", dpid="0000000000000010")
        s15 = self.addSwitch("seattle15", dpid="0000000000000011")
        s16 = self.addSwitch("portland6", dpid="0000000000000012")
        s17 = self.addSwitch("tokyo17", dpid="0000000000000013")
        s18 = self.addSwitch("sanfranc8", dpid="0000000000000014")
        s19 = self.addSwitch("losangel9", dpid="0000000000000015")
        s20 = self.addSwitch("phoenix20", dpid="0000000000000016")
        s21 = self.addSwitch("denver21", dpid="0000000000000017")
        s22 = self.addSwitch("chicago22", dpid="0000000000000018")

        # Adding Links
        self.addLink(s0, s2)
        self.addLink(s0, s4)
        self.addLink(s0, s5)
        self.addLink(s0, s7)
        self.addLink(s1, s8)
        self.addLink(s1, s6)
        self.addLink(s1, s4)
        self.addLink(s1, s5)
        self.addLink(s1, s22)
        self.addLink(s2, s10)
        self.addLink(s2, s3)
        self.addLink(s3, s10)
        self.addLink(s5, s12)
        self.addLink(s5, s8)
        self.addLink(s6, s7)
        self.addLink(s8, s9)
        self.addLink(s9, s12)
        self.addLink(s10, s20)
        self.addLink(s10, s13)
        self.addLink(s10, s14)
        self.addLink(s11, s13)
        self.addLink(s11, s22)
        self.addLink(s11, s21)
        self.addLink(s13, s14)
        self.addLink(s15, s16)
        self.addLink(s15, s22)
        self.addLink(s16, s18)
        self.addLink(s17, s18)
        self.addLink(s18, s19)
        self.addLink(s18, s21)
        self.addLink(s19, s20)


topos = {"Abvt": (lambda: Abvt())}

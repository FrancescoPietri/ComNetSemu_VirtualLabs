#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class BtEurope(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("budapest0", dpid="0000000000000002")
        s1 = self.addSwitch("munich1", dpid="0000000000000003")
        s2 = self.addSwitch("prague2", dpid="0000000000000004")
        s3 = self.addSwitch("vienna3", dpid="0000000000000005")
        s4 = self.addSwitch("dusseldo4", dpid="0000000000000006")
        s5 = self.addSwitch("frankfur5", dpid="0000000000000007")
        s6 = self.addSwitch("zurich6", dpid="0000000000000008")
        s7 = self.addSwitch("paris7", dpid="0000000000000009")
        s8 = self.addSwitch("milan8", dpid="000000000000000a")
        s9 = self.addSwitch("barcelon9", dpid="000000000000000b")
        s10 = self.addSwitch("goonhill0", dpid="000000000000000c")
        s11 = self.addSwitch("newyork11", dpid="000000000000000d")
        s12 = self.addSwitch("washingt2", dpid="000000000000000e")
        s13 = self.addSwitch("madrid13", dpid="000000000000000f")
        s14 = self.addSwitch("helsinki4", dpid="0000000000000010")
        s15 = self.addSwitch("copenhag5", dpid="0000000000000011")
        s16 = self.addSwitch("london16", dpid="0000000000000012")
        s17 = self.addSwitch("london17", dpid="0000000000000013")
        s18 = self.addSwitch("madley18", dpid="0000000000000014")
        s19 = self.addSwitch("dublin19", dpid="0000000000000015")
        s20 = self.addSwitch("brussels0", dpid="0000000000000016")
        s21 = self.addSwitch("amsterda1", dpid="0000000000000017")
        s22 = self.addSwitch("gothenbu2", dpid="0000000000000018")
        s23 = self.addSwitch("stockhol3", dpid="0000000000000019")

        # Adding Links
        self.addLink(s0, s17)
        self.addLink(s0, s5)
        self.addLink(s1, s4)
        self.addLink(s1, s5)
        self.addLink(s2, s16)
        self.addLink(s2, s5)
        self.addLink(s3, s5)
        self.addLink(s3, s21)
        self.addLink(s4, s5)
        self.addLink(s4, s21)
        self.addLink(s5, s6)
        self.addLink(s5, s8)
        self.addLink(s5, s17)
        self.addLink(s5, s21)
        self.addLink(s6, s17)
        self.addLink(s7, s17)
        self.addLink(s7, s21)
        self.addLink(s8, s17)
        self.addLink(s9, s13)
        self.addLink(s9, s21)
        self.addLink(s10, s17)
        self.addLink(s11, s17)
        self.addLink(s12, s16)
        self.addLink(s13, s17)
        self.addLink(s14, s23)
        self.addLink(s15, s23)
        self.addLink(s16, s17)
        self.addLink(s16, s21)
        self.addLink(s16, s23)
        self.addLink(s17, s18)
        self.addLink(s17, s19)
        self.addLink(s17, s20)
        self.addLink(s17, s21)
        self.addLink(s19, s21)
        self.addLink(s21, s22)
        self.addLink(s21, s23)
        self.addLink(s22, s23)


topos = {"BtEurope": (lambda: BtEurope())}

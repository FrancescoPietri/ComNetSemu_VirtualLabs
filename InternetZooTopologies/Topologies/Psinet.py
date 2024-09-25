#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Psinet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("detroit0", dpid="0000000000000002")
        s1 = self.addSwitch("dublin1", dpid="0000000000000003")
        s2 = self.addSwitch("chicago2", dpid="0000000000000004")
        s3 = self.addSwitch("toledo3", dpid="0000000000000005")
        s4 = self.addSwitch("washingt4", dpid="0000000000000006")
        s5 = self.addSwitch("baltimor5", dpid="0000000000000007")
        s6 = self.addSwitch("herndon6", dpid="0000000000000008")
        s7 = self.addSwitch("atlanta7", dpid="0000000000000009")
        s8 = self.addSwitch("wilmingt8", dpid="000000000000000a")
        s9 = self.addSwitch("philadel9", dpid="000000000000000b")
        s10 = self.addSwitch("boston10", dpid="000000000000000c")
        s11 = self.addSwitch("troy11", dpid="000000000000000d")
        s12 = self.addSwitch("newyork12", dpid="000000000000000e")
        s13 = self.addSwitch("newark13", dpid="000000000000000f")
        s14 = self.addSwitch("kansasci4", dpid="0000000000000010")
        s15 = self.addSwitch("stlouis15", dpid="0000000000000011")
        s16 = self.addSwitch("sanfranc6", dpid="0000000000000012")
        s17 = self.addSwitch("santacla7", dpid="0000000000000013")
        s18 = self.addSwitch("losangel8", dpid="0000000000000014")
        s19 = self.addSwitch("phoenix19", dpid="0000000000000015")
        s20 = self.addSwitch("austin20", dpid="0000000000000016")
        s21 = self.addSwitch("fortwort1", dpid="0000000000000017")
        s22 = self.addSwitch("dallas22", dpid="0000000000000018")
        s23 = self.addSwitch("houston23", dpid="0000000000000019")

        # Adding Links
        self.addLink(s0, s3)
        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s1, s4)
        self.addLink(s2, s3)
        self.addLink(s2, s15)
        self.addLink(s4, s5)
        self.addLink(s5, s8)
        self.addLink(s6, s12)
        self.addLink(s6, s7)
        self.addLink(s7, s23)
        self.addLink(s8, s9)
        self.addLink(s9, s13)
        self.addLink(s10, s12)
        self.addLink(s11, s12)
        self.addLink(s12, s13)
        self.addLink(s14, s19)
        self.addLink(s14, s22)
        self.addLink(s14, s15)
        self.addLink(s16, s17)
        self.addLink(s16, s18)
        self.addLink(s18, s19)
        self.addLink(s20, s23)
        self.addLink(s21, s22)
        self.addLink(s22, s23)


topos = {"Psinet": (lambda: Psinet())}

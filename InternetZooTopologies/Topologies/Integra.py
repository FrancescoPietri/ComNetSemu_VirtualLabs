#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Integra(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("chicago0", dpid="0000000000000002")
        s1 = self.addSwitch("dallas1", dpid="0000000000000003")
        s2 = self.addSwitch("stcloud22", dpid="0000000000000004")
        s3 = self.addSwitch("minneapo3", dpid="0000000000000005")
        s4 = self.addSwitch("losangel4", dpid="0000000000000006")
        s5 = self.addSwitch("santacla5", dpid="0000000000000007")
        s6 = self.addSwitch("lasvegas6", dpid="0000000000000008")
        s7 = self.addSwitch("phoenix7", dpid="0000000000000009")
        s8 = self.addSwitch("sacramen8", dpid="000000000000000a")
        s9 = self.addSwitch("santaros9", dpid="000000000000000b")
        s10 = self.addSwitch("salem10", dpid="000000000000000c")
        s11 = self.addSwitch("bend11", dpid="000000000000000d")
        s12 = self.addSwitch("eugene12", dpid="000000000000000e")
        s13 = self.addSwitch("reno13", dpid="000000000000000f")
        s14 = self.addSwitch("ranchoco4", dpid="0000000000000010")
        s15 = self.addSwitch("newyork15", dpid="0000000000000011")
        s16 = self.addSwitch("ashburn16", dpid="0000000000000012")
        s17 = self.addSwitch("spokane17", dpid="0000000000000013")
        s18 = self.addSwitch("fargo18", dpid="0000000000000014")
        s19 = self.addSwitch("billings9", dpid="0000000000000015")
        s20 = self.addSwitch("denver20", dpid="0000000000000016")
        s21 = self.addSwitch("ogden21", dpid="0000000000000017")
        s22 = self.addSwitch("orem22", dpid="0000000000000018")
        s23 = self.addSwitch("saltlake3", dpid="0000000000000019")
        s24 = self.addSwitch("boise24", dpid="000000000000001a")
        s25 = self.addSwitch("portland5", dpid="000000000000001b")
        s26 = self.addSwitch("seattle26", dpid="000000000000001c")

        # Adding Links
        self.addLink(s0, s16)
        self.addLink(s0, s3)
        self.addLink(s0, s20)
        self.addLink(s1, s20)
        self.addLink(s1, s7)
        self.addLink(s2, s18)
        self.addLink(s2, s3)
        self.addLink(s3, s18)
        self.addLink(s3, s26)
        self.addLink(s3, s15)
        self.addLink(s4, s5)
        self.addLink(s4, s6)
        self.addLink(s4, s7)
        self.addLink(s5, s8)
        self.addLink(s6, s23)
        self.addLink(s6, s7)
        self.addLink(s8, s9)
        self.addLink(s8, s13)
        self.addLink(s8, s14)
        self.addLink(s8, s25)
        self.addLink(s10, s25)
        self.addLink(s10, s12)
        self.addLink(s11, s25)
        self.addLink(s11, s26)
        self.addLink(s13, s23)
        self.addLink(s15, s16)
        self.addLink(s17, s26)
        self.addLink(s17, s19)
        self.addLink(s19, s20)
        self.addLink(s20, s21)
        self.addLink(s21, s22)
        self.addLink(s21, s23)
        self.addLink(s22, s23)
        self.addLink(s23, s24)
        self.addLink(s24, s25)
        self.addLink(s25, s26)


topos = {"Integra": (lambda: Integra())}

#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Bbnplanet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("jackson0", dpid="0000000000000002")
        s1 = self.addSwitch("atlanta1", dpid="0000000000000003")
        s2 = self.addSwitch("austin2", dpid="0000000000000004")
        s3 = self.addSwitch("houston3", dpid="0000000000000005")
        s4 = self.addSwitch("detroit4", dpid="0000000000000006")
        s5 = self.addSwitch("columbus5", dpid="0000000000000007")
        s6 = self.addSwitch("cincinna6", dpid="0000000000000008")
        s7 = self.addSwitch("clevelan7", dpid="0000000000000009")
        s8 = self.addSwitch("chicago8", dpid="000000000000000a")
        s9 = self.addSwitch("minneapo9", dpid="000000000000000b")
        s10 = self.addSwitch("philadel0", dpid="000000000000000c")
        s11 = self.addSwitch("newyork11", dpid="000000000000000d")
        s12 = self.addSwitch("cambridg2", dpid="000000000000000e")
        s13 = self.addSwitch("boston13", dpid="000000000000000f")
        s14 = self.addSwitch("richmond4", dpid="0000000000000010")
        s15 = self.addSwitch("washingt5", dpid="0000000000000011")
        s16 = self.addSwitch("baltimor6", dpid="0000000000000012")
        s17 = self.addSwitch("denver17", dpid="0000000000000013")
        s18 = self.addSwitch("dallas18", dpid="0000000000000014")
        s19 = self.addSwitch("sacramen9", dpid="0000000000000015")
        s20 = self.addSwitch("oakland20", dpid="0000000000000016")
        s21 = self.addSwitch("sanfranc1", dpid="0000000000000017")
        s22 = self.addSwitch("paloalto2", dpid="0000000000000018")
        s23 = self.addSwitch("sanjose23", dpid="0000000000000019")
        s24 = self.addSwitch("losangel4", dpid="000000000000001a")
        s25 = self.addSwitch("sandiego5", dpid="000000000000001b")
        s26 = self.addSwitch("orange26", dpid="000000000000001c")

        # Adding Links
        self.addLink(s0, s1)
        self.addLink(s1, s18)
        self.addLink(s1, s15)
        self.addLink(s2, s18)
        self.addLink(s3, s18)
        self.addLink(s4, s7)
        self.addLink(s5, s7)
        self.addLink(s6, s7)
        self.addLink(s7, s8)
        self.addLink(s7, s11)
        self.addLink(s8, s17)
        self.addLink(s8, s13)
        self.addLink(s8, s9)
        self.addLink(s10, s11)
        self.addLink(s11, s12)
        self.addLink(s11, s15)
        self.addLink(s14, s15)
        self.addLink(s15, s16)
        self.addLink(s15, s23)
        self.addLink(s17, s20)
        self.addLink(s18, s24)
        self.addLink(s19, s20)
        self.addLink(s20, s21)
        self.addLink(s20, s23)
        self.addLink(s22, s23)
        self.addLink(s23, s24)
        self.addLink(s24, s25)
        self.addLink(s24, s26)


topos = {"Bbnplanet": (lambda: Bbnplanet())}

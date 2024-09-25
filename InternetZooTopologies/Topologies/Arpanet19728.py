#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Arpanet19728(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("illinois0", dpid="0000000000000002")
        s1 = self.addSwitch("mitre1", dpid="0000000000000003")
        s2 = self.addSwitch("carnegie2", dpid="0000000000000004")
        s3 = self.addSwitch("case3", dpid="0000000000000005")
        s4 = self.addSwitch("etac4", dpid="0000000000000006")
        s5 = self.addSwitch("afgwc5", dpid="0000000000000007")
        s6 = self.addSwitch("bbn6", dpid="0000000000000008")
        s7 = self.addSwitch("nbs7", dpid="0000000000000009")
        s8 = self.addSwitch("tinker8", dpid="000000000000000a")
        s9 = self.addSwitch("ames9", dpid="000000000000000b")
        s10 = self.addSwitch("arpa10", dpid="000000000000000c")
        s11 = self.addSwitch("radc11", dpid="000000000000000d")
        s12 = self.addSwitch("mcclella2", dpid="000000000000000e")
        s13 = self.addSwitch("rand13", dpid="000000000000000f")
        s14 = self.addSwitch("ames14", dpid="0000000000000010")
        s15 = self.addSwitch("noaabo5", dpid="0000000000000011")
        s16 = self.addSwitch("saac16", dpid="0000000000000012")
        s17 = self.addSwitch("belvoir17", dpid="0000000000000013")
        s18 = self.addSwitch("sdc18", dpid="0000000000000014")
        s19 = self.addSwitch("bbn19", dpid="0000000000000015")
        s20 = self.addSwitch("harvard20", dpid="0000000000000016")
        s21 = self.addSwitch("sri21", dpid="0000000000000017")
        s22 = self.addSwitch("ucsb22", dpid="0000000000000018")
        s23 = self.addSwitch("ucla23", dpid="0000000000000019")
        s24 = self.addSwitch("stanford4", dpid="000000000000001a")
        s25 = self.addSwitch("usc25", dpid="000000000000001b")
        s26 = self.addSwitch("utah26", dpid="000000000000001c")
        s27 = self.addSwitch("lincoln27", dpid="000000000000001d")
        s28 = self.addSwitch("mit28", dpid="000000000000001e")

        # Adding Links
        self.addLink(s0, s26)
        self.addLink(s0, s28)
        self.addLink(s1, s16)
        self.addLink(s1, s10)
        self.addLink(s2, s17)
        self.addLink(s2, s3)
        self.addLink(s3, s11)
        self.addLink(s3, s5)
        self.addLink(s4, s8)
        self.addLink(s4, s10)
        self.addLink(s4, s7)
        self.addLink(s5, s15)
        self.addLink(s6, s19)
        self.addLink(s6, s28)
        self.addLink(s7, s20)
        self.addLink(s8, s13)
        self.addLink(s9, s21)
        self.addLink(s9, s14)
        self.addLink(s11, s27)
        self.addLink(s12, s26)
        self.addLink(s12, s21)
        self.addLink(s13, s24)
        self.addLink(s13, s23)
        self.addLink(s14, s24)
        self.addLink(s15, s25)
        self.addLink(s16, s17)
        self.addLink(s18, s25)
        self.addLink(s18, s23)
        self.addLink(s19, s20)
        self.addLink(s21, s22)
        self.addLink(s22, s23)
        self.addLink(s27, s28)


topos = {"Arpanet19728": (lambda: Arpanet19728())}

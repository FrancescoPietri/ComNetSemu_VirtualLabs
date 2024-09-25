#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class HiberniaUs(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("pittsbur0", dpid="0000000000000002")
        s1 = self.addSwitch("philadel1", dpid="0000000000000003")
        s2 = self.addSwitch("newark2", dpid="0000000000000004")
        s3 = self.addSwitch("ashburn3", dpid="0000000000000005")
        s4 = self.addSwitch("raleigh4", dpid="0000000000000006")
        s5 = self.addSwitch("charlott5", dpid="0000000000000007")
        s6 = self.addSwitch("mclean6", dpid="0000000000000008")
        s7 = self.addSwitch("richmond7", dpid="0000000000000009")
        s8 = self.addSwitch("atlanta8", dpid="000000000000000a")
        s9 = self.addSwitch("newyork99", dpid="000000000000000b")
        s10 = self.addSwitch("none10", dpid="000000000000000c")
        s11 = self.addSwitch("none11", dpid="000000000000000d")
        s12 = self.addSwitch("whitepla2", dpid="000000000000000e")
        s13 = self.addSwitch("stamford3", dpid="000000000000000f")
        s14 = self.addSwitch("chicago14", dpid="0000000000000010")
        s15 = self.addSwitch("clevelan5", dpid="0000000000000011")
        s16 = self.addSwitch("buffalo16", dpid="0000000000000012")
        s17 = self.addSwitch("toronto17", dpid="0000000000000013")
        s18 = self.addSwitch("montreal8", dpid="0000000000000014")
        s19 = self.addSwitch("albany19", dpid="0000000000000015")
        s20 = self.addSwitch("boston20", dpid="0000000000000016")
        s21 = self.addSwitch("halifax21", dpid="0000000000000017")

        # Adding Links
        self.addLink(s0, s3)
        self.addLink(s0, s14)
        self.addLink(s0, s15)
        self.addLink(s1, s9)
        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s2, s3)
        self.addLink(s2, s12)
        self.addLink(s2, s9)
        self.addLink(s3, s6)
        self.addLink(s4, s5)
        self.addLink(s4, s7)
        self.addLink(s5, s8)
        self.addLink(s6, s7)
        self.addLink(s9, s19)
        self.addLink(s9, s13)
        self.addLink(s10, s21)
        self.addLink(s11, s21)
        self.addLink(s12, s13)
        self.addLink(s13, s20)
        self.addLink(s14, s15)
        self.addLink(s15, s16)
        self.addLink(s16, s17)
        self.addLink(s16, s19)
        self.addLink(s17, s18)
        self.addLink(s18, s19)
        self.addLink(s18, s21)
        self.addLink(s19, s20)
        self.addLink(s20, s21)


topos = {"HiberniaUs": (lambda: HiberniaUs())}

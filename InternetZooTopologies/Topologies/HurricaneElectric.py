#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class HurricaneElectric(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("amsterda0", dpid="0000000000000002")
        s1 = self.addSwitch("frankfur1", dpid="0000000000000003")
        s2 = self.addSwitch("london2", dpid="0000000000000004")
        s3 = self.addSwitch("paris3", dpid="0000000000000005")
        s4 = self.addSwitch("paloalto4", dpid="0000000000000006")
        s5 = self.addSwitch("fremont15", dpid="0000000000000007")
        s6 = self.addSwitch("zurich6", dpid="0000000000000008")
        s7 = self.addSwitch("stockhol7", dpid="0000000000000009")
        s8 = self.addSwitch("fremont28", dpid="000000000000000a")
        s9 = self.addSwitch("sanjose29", dpid="000000000000000b")
        s10 = self.addSwitch("newyork30", dpid="000000000000000c")
        s11 = self.addSwitch("newyork21", dpid="000000000000000d")
        s12 = self.addSwitch("newyork12", dpid="000000000000000e")
        s13 = self.addSwitch("sanjose13", dpid="000000000000000f")
        s14 = self.addSwitch("atlanta14", dpid="0000000000000010")
        s15 = self.addSwitch("miami15", dpid="0000000000000011")
        s16 = self.addSwitch("hongkong6", dpid="0000000000000012")
        s17 = self.addSwitch("tokyo17", dpid="0000000000000013")
        s18 = self.addSwitch("seattle18", dpid="0000000000000014")
        s19 = self.addSwitch("losangel9", dpid="0000000000000015")
        s20 = self.addSwitch("dallas20", dpid="0000000000000016")
        s21 = self.addSwitch("chicago21", dpid="0000000000000017")
        s22 = self.addSwitch("toronto22", dpid="0000000000000018")
        s23 = self.addSwitch("ashburn23", dpid="0000000000000019")

        # Adding Links
        self.addLink(s0, s1)
        self.addLink(s0, s2)
        self.addLink(s0, s3)
        self.addLink(s0, s12)
        self.addLink(s1, s3)
        self.addLink(s1, s6)
        self.addLink(s1, s7)
        self.addLink(s2, s12)
        self.addLink(s2, s23)
        self.addLink(s3, s23)
        self.addLink(s4, s5)
        self.addLink(s4, s8)
        self.addLink(s4, s9)
        self.addLink(s4, s13)
        self.addLink(s4, s19)
        self.addLink(s4, s23)
        self.addLink(s5, s9)
        self.addLink(s8, s9)
        self.addLink(s9, s12)
        self.addLink(s9, s13)
        self.addLink(s9, s18)
        self.addLink(s9, s21)
        self.addLink(s10, s11)
        self.addLink(s10, s12)
        self.addLink(s11, s12)
        self.addLink(s11, s22)
        self.addLink(s12, s19)
        self.addLink(s12, s21)
        self.addLink(s12, s23)
        self.addLink(s13, s16)
        self.addLink(s13, s17)
        self.addLink(s14, s20)
        self.addLink(s14, s23)
        self.addLink(s15, s23)
        self.addLink(s19, s20)
        self.addLink(s20, s21)
        self.addLink(s20, s23)


topos = {"HurricaneElectric": (lambda: HurricaneElectric())}

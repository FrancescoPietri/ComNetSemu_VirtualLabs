#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Amres(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("bor0", dpid="0000000000000002")
        s1 = self.addSwitch("kosovska1", dpid="0000000000000003")
        s2 = self.addSwitch("novipaza2", dpid="0000000000000004")
        s3 = self.addSwitch("krusteva3", dpid="0000000000000005")
        s4 = self.addSwitch("vranje4", dpid="0000000000000006")
        s5 = self.addSwitch("nis5", dpid="0000000000000007")
        s6 = self.addSwitch("pirot6", dpid="0000000000000008")
        s7 = self.addSwitch("leskovac7", dpid="0000000000000009")
        s8 = self.addSwitch("kragujev8", dpid="000000000000000a")
        s9 = self.addSwitch("novisad99", dpid="000000000000000b")
        s10 = self.addSwitch("bosniaan0", dpid="000000000000000c")
        s11 = self.addSwitch("hungarne1", dpid="000000000000000d")
        s12 = self.addSwitch("beograd12", dpid="000000000000000e")
        s13 = self.addSwitch("pancevo13", dpid="000000000000000f")
        s14 = self.addSwitch("telekoms4", dpid="0000000000000010")
        s15 = self.addSwitch("kraljevo5", dpid="0000000000000011")
        s16 = self.addSwitch("raska16", dpid="0000000000000012")
        s17 = self.addSwitch("subotica7", dpid="0000000000000013")
        s18 = self.addSwitch("sombor18", dpid="0000000000000014")
        s19 = self.addSwitch("zrenjani9", dpid="0000000000000015")
        s20 = self.addSwitch("sabac20", dpid="0000000000000016")
        s21 = self.addSwitch("valjevo21", dpid="0000000000000017")
        s22 = self.addSwitch("uzice22", dpid="0000000000000018")
        s23 = self.addSwitch("cacak23", dpid="0000000000000019")
        s24 = self.addSwitch("velikapl4", dpid="000000000000001a")

        # Adding Links
        self.addLink(s0, s5)
        self.addLink(s1, s12)
        self.addLink(s2, s16)
        self.addLink(s3, s5)
        self.addLink(s3, s15)
        self.addLink(s4, s7)
        self.addLink(s5, s6)
        self.addLink(s5, s7)
        self.addLink(s8, s24)
        self.addLink(s8, s15)
        self.addLink(s9, s17)
        self.addLink(s9, s18)
        self.addLink(s9, s19)
        self.addLink(s9, s12)
        self.addLink(s10, s20)
        self.addLink(s11, s17)
        self.addLink(s12, s13)
        self.addLink(s12, s14)
        self.addLink(s12, s20)
        self.addLink(s12, s21)
        self.addLink(s12, s24)
        self.addLink(s15, s16)
        self.addLink(s21, s22)
        self.addLink(s22, s23)


topos = {"Amres": (lambda: Amres())}

#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Uran(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("kherson0", dpid="0000000000000002")
        s1 = self.addSwitch("mykolaiv1", dpid="0000000000000003")
        s2 = self.addSwitch("sevastop2", dpid="0000000000000004")
        s3 = self.addSwitch("simferop3", dpid="0000000000000005")
        s4 = self.addSwitch("vinnitsa4", dpid="0000000000000006")
        s5 = self.addSwitch("khmelnit5", dpid="0000000000000007")
        s6 = self.addSwitch("odessa6", dpid="0000000000000008")
        s7 = self.addSwitch("kamianet7", dpid="0000000000000009")
        s8 = self.addSwitch("frankfur8", dpid="000000000000000a")
        s9 = self.addSwitch("poznang9", dpid="000000000000000b")
        s10 = self.addSwitch("cherkass0", dpid="000000000000000c")
        s11 = self.addSwitch("odessai1", dpid="000000000000000d")
        s12 = self.addSwitch("kharkiv2", dpid="000000000000000e")
        s13 = self.addSwitch("uaix13", dpid="000000000000000f")
        s14 = self.addSwitch("zaporizh4", dpid="0000000000000010")
        s15 = self.addSwitch("dniprope5", dpid="0000000000000011")
        s16 = self.addSwitch("lviv16", dpid="0000000000000012")
        s17 = self.addSwitch("lutsk17", dpid="0000000000000013")
        s18 = self.addSwitch("zhitomir8", dpid="0000000000000014")
        s19 = self.addSwitch("kiev19", dpid="0000000000000015")
        s20 = self.addSwitch("pereyasl0", dpid="0000000000000016")
        s21 = self.addSwitch("poltava21", dpid="0000000000000017")
        s22 = self.addSwitch("kharkiv22", dpid="0000000000000018")
        s23 = self.addSwitch("donetsk23", dpid="0000000000000019")

        # Adding Links
        self.addLink(s0, s1)
        self.addLink(s0, s3)
        self.addLink(s1, s10)
        self.addLink(s1, s6)
        self.addLink(s2, s3)
        self.addLink(s4, s19)
        self.addLink(s4, s5)
        self.addLink(s5, s16)
        self.addLink(s6, s11)
        self.addLink(s7, s19)
        self.addLink(s8, s19)
        self.addLink(s9, s16)
        self.addLink(s10, s19)
        self.addLink(s12, s22)
        self.addLink(s13, s19)
        self.addLink(s14, s15)
        self.addLink(s15, s21)
        self.addLink(s15, s23)
        self.addLink(s16, s19)
        self.addLink(s17, s18)
        self.addLink(s18, s19)
        self.addLink(s19, s20)
        self.addLink(s19, s21)
        self.addLink(s21, s22)


topos = {"Uran": (lambda: Uran())}

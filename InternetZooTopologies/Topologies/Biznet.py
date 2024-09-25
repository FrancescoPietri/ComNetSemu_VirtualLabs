#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Biznet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("cilacap0", dpid="0000000000000002")
        s1 = self.addSwitch("purwoker1", dpid="0000000000000003")
        s2 = self.addSwitch("sukabumi2", dpid="0000000000000004")
        s3 = self.addSwitch("tasikmal3", dpid="0000000000000005")
        s4 = self.addSwitch("pekalong4", dpid="0000000000000006")
        s5 = self.addSwitch("semarang5", dpid="0000000000000007")
        s6 = self.addSwitch("magelang6", dpid="0000000000000008")
        s7 = self.addSwitch("yogyakar7", dpid="0000000000000009")
        s8 = self.addSwitch("kudus8", dpid="000000000000000a")
        s9 = self.addSwitch("surakart9", dpid="000000000000000b")
        s10 = self.addSwitch("nusadua10", dpid="000000000000000c")
        s11 = self.addSwitch("surabaya1", dpid="000000000000000d")
        s12 = self.addSwitch("kediri12", dpid="000000000000000e")
        s13 = self.addSwitch("madium13", dpid="000000000000000f")
        s14 = self.addSwitch("tuban14", dpid="0000000000000010")
        s15 = self.addSwitch("banyunwa5", dpid="0000000000000011")
        s16 = self.addSwitch("jember16", dpid="0000000000000012")
        s17 = self.addSwitch("probolin7", dpid="0000000000000013")
        s18 = self.addSwitch("malang18", dpid="0000000000000014")
        s19 = self.addSwitch("bakauhun9", dpid="0000000000000015")
        s20 = self.addSwitch("cibaliun0", dpid="0000000000000016")
        s21 = self.addSwitch("tegal21", dpid="0000000000000017")
        s22 = self.addSwitch("cirebon22", dpid="0000000000000018")
        s23 = self.addSwitch("bandung23", dpid="0000000000000019")
        s24 = self.addSwitch("karawang4", dpid="000000000000001a")
        s25 = self.addSwitch("jakarta25", dpid="000000000000001b")
        s26 = self.addSwitch("bogor26", dpid="000000000000001c")
        s27 = self.addSwitch("serang27", dpid="000000000000001d")
        s28 = self.addSwitch("anyer28", dpid="000000000000001e")

        # Adding Links
        self.addLink(s0, s1)
        self.addLink(s0, s3)
        self.addLink(s1, s6)
        self.addLink(s2, s26)
        self.addLink(s2, s23)
        self.addLink(s3, s23)
        self.addLink(s4, s21)
        self.addLink(s4, s5)
        self.addLink(s5, s8)
        self.addLink(s5, s9)
        self.addLink(s6, s7)
        self.addLink(s7, s9)
        self.addLink(s8, s14)
        self.addLink(s9, s13)
        self.addLink(s10, s15)
        self.addLink(s11, s17)
        self.addLink(s11, s12)
        self.addLink(s11, s14)
        self.addLink(s12, s18)
        self.addLink(s12, s13)
        self.addLink(s15, s16)
        self.addLink(s16, s17)
        self.addLink(s16, s18)
        self.addLink(s19, s28)
        self.addLink(s20, s26)
        self.addLink(s20, s28)
        self.addLink(s21, s22)
        self.addLink(s22, s23)
        self.addLink(s23, s24)
        self.addLink(s24, s25)
        self.addLink(s25, s26)
        self.addLink(s25, s27)
        self.addLink(s27, s28)


topos = {"Biznet": (lambda: Biznet())}

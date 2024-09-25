#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Rnp(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("revife0", dpid="0000000000000002")
        s1 = self.addSwitch("maceio1", dpid="0000000000000003")
        s2 = self.addSwitch("campinag2", dpid="0000000000000004")
        s3 = self.addSwitch("jobopass3", dpid="0000000000000005")
        s4 = self.addSwitch("brasilia4", dpid="0000000000000006")
        s5 = self.addSwitch("belohori5", dpid="0000000000000007")
        s6 = self.addSwitch("aracaju6", dpid="0000000000000008")
        s7 = self.addSwitch("salvador7", dpid="0000000000000009")
        s8 = self.addSwitch("vitoria8", dpid="000000000000000a")
        s9 = self.addSwitch("riodejan9", dpid="000000000000000b")
        s10 = self.addSwitch("manaus10", dpid="000000000000000c")
        s11 = self.addSwitch("goiania11", dpid="000000000000000d")
        s12 = self.addSwitch("cuiaba12", dpid="000000000000000e")
        s13 = self.addSwitch("curitiba3", dpid="000000000000000f")
        s14 = self.addSwitch("portoale4", dpid="0000000000000010")
        s15 = self.addSwitch("floriano5", dpid="0000000000000011")
        s16 = self.addSwitch("saopaulo6", dpid="0000000000000012")
        s17 = self.addSwitch("portovel7", dpid="0000000000000013")
        s18 = self.addSwitch("riobranc8", dpid="0000000000000014")
        s19 = self.addSwitch("palmas19", dpid="0000000000000015")
        s20 = self.addSwitch("campogra0", dpid="0000000000000016")
        s21 = self.addSwitch("teresina1", dpid="0000000000000017")
        s22 = self.addSwitch("natal22", dpid="0000000000000018")
        s23 = self.addSwitch("redclara3", dpid="0000000000000019")
        s24 = self.addSwitch("inetnetc4", dpid="000000000000001a")
        s25 = self.addSwitch("americas5", dpid="000000000000001b")
        s26 = self.addSwitch("boavista6", dpid="000000000000001c")
        s27 = self.addSwitch("macapa27", dpid="000000000000001d")
        s28 = self.addSwitch("belem28", dpid="000000000000001e")
        s29 = self.addSwitch("saoluis29", dpid="000000000000001f")
        s30 = self.addSwitch("fortalez0", dpid="0000000000000020")

        # Adding Links
        self.addLink(s0, s2)
        self.addLink(s0, s21)
        self.addLink(s1, s6)
        self.addLink(s2, s3)
        self.addLink(s3, s22)
        self.addLink(s4, s9)
        self.addLink(s4, s26)
        self.addLink(s4, s27)
        self.addLink(s4, s10)
        self.addLink(s4, s5)
        self.addLink(s5, s16)
        self.addLink(s5, s30)
        self.addLink(s5, s7)
        self.addLink(s6, s7)
        self.addLink(s7, s8)
        self.addLink(s8, s9)
        self.addLink(s9, s16)
        self.addLink(s11, s19)
        self.addLink(s11, s12)
        self.addLink(s12, s17)
        self.addLink(s12, s20)
        self.addLink(s13, s16)
        self.addLink(s13, s20)
        self.addLink(s13, s14)
        self.addLink(s14, s15)
        self.addLink(s15, s16)
        self.addLink(s16, s23)
        self.addLink(s16, s24)
        self.addLink(s16, s25)
        self.addLink(s17, s18)
        self.addLink(s21, s28)
        self.addLink(s22, s30)
        self.addLink(s28, s29)
        self.addLink(s29, s30)


topos = {"Rnp": (lambda: Rnp())}

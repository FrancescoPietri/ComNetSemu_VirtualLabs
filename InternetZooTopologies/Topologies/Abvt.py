#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Abvt(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("00", dpid="0000000000000002")
        s1 = self.addSwitch("11", dpid="0000000000000003")
        s2 = self.addSwitch("22", dpid="0000000000000004")
        s3 = self.addSwitch("33", dpid="0000000000000005")
        s4 = self.addSwitch("44", dpid="0000000000000006")
        s5 = self.addSwitch("55", dpid="0000000000000007")
        s6 = self.addSwitch("66", dpid="0000000000000008")
        s7 = self.addSwitch("77", dpid="0000000000000009")
        s8 = self.addSwitch("88", dpid="000000000000000a")
        s9 = self.addSwitch("99", dpid="000000000000000b")
        s10 = self.addSwitch("1010", dpid="000000000000000c")
        s11 = self.addSwitch("1111", dpid="000000000000000d")
        s12 = self.addSwitch("1212", dpid="000000000000000e")
        s13 = self.addSwitch("1313", dpid="000000000000000f")
        s14 = self.addSwitch("1414", dpid="0000000000000010")
        s15 = self.addSwitch("1515", dpid="0000000000000011")
        s16 = self.addSwitch("1616", dpid="0000000000000012")
        s17 = self.addSwitch("1717", dpid="0000000000000013")
        s18 = self.addSwitch("1818", dpid="0000000000000014")
        s19 = self.addSwitch("1919", dpid="0000000000000015")
        s20 = self.addSwitch("2020", dpid="0000000000000016")
        s21 = self.addSwitch("2121", dpid="0000000000000017")
        s22 = self.addSwitch("2222", dpid="0000000000000018")

        # Adding Links
        self.addLink(s0, s2)
        self.addLink(s0, s4)
        self.addLink(s0, s5)
        self.addLink(s0, s7)
        self.addLink(s1, s8)
        self.addLink(s1, s6)
        self.addLink(s1, s4)
        self.addLink(s1, s5)
        self.addLink(s1, s22)
        self.addLink(s2, s10)
        self.addLink(s2, s3)
        self.addLink(s3, s10)
        self.addLink(s5, s12)
        self.addLink(s5, s8)
        self.addLink(s6, s7)
        self.addLink(s8, s9)
        self.addLink(s9, s12)
        self.addLink(s10, s20)
        self.addLink(s10, s13)
        self.addLink(s10, s14)
        self.addLink(s11, s13)
        self.addLink(s11, s22)
        self.addLink(s11, s21)
        self.addLink(s13, s14)
        self.addLink(s15, s16)
        self.addLink(s15, s22)
        self.addLink(s16, s18)
        self.addLink(s17, s18)
        self.addLink(s18, s19)
        self.addLink(s18, s21)
        self.addLink(s19, s20)


topos = {"Abvt": (lambda: Abvt())}

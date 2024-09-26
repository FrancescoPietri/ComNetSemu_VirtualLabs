#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class GtsCzechRepublic(Topo):
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
        s23 = self.addSwitch("2323", dpid="0000000000000019")
        s24 = self.addSwitch("2424", dpid="000000000000001a")
        s25 = self.addSwitch("2525", dpid="000000000000001b")
        s26 = self.addSwitch("2626", dpid="000000000000001c")
        s27 = self.addSwitch("2727", dpid="000000000000001d")
        s28 = self.addSwitch("2828", dpid="000000000000001e")
        s29 = self.addSwitch("2929", dpid="000000000000001f")
        s30 = self.addSwitch("3030", dpid="0000000000000020")
        s31 = self.addSwitch("3131", dpid="0000000000000021")

        # Adding Links
        self.addLink(s0, s3)
        self.addLink(s1, s6)
        self.addLink(s2, s12)
        self.addLink(s2, s23)
        self.addLink(s3, s22)
        self.addLink(s3, s23)
        self.addLink(s4, s5)
        self.addLink(s4, s6)
        self.addLink(s5, s9)
        self.addLink(s6, s30)
        self.addLink(s6, s7)
        self.addLink(s8, s9)
        self.addLink(s9, s17)
        self.addLink(s9, s18)
        self.addLink(s10, s11)
        self.addLink(s11, s28)
        self.addLink(s11, s26)
        self.addLink(s11, s30)
        self.addLink(s12, s27)
        self.addLink(s13, s30)
        self.addLink(s14, s24)
        self.addLink(s14, s25)
        self.addLink(s14, s20)
        self.addLink(s14, s15)
        self.addLink(s15, s16)
        self.addLink(s16, s17)
        self.addLink(s19, s30)
        self.addLink(s21, s25)
        self.addLink(s22, s30)
        self.addLink(s25, s26)
        self.addLink(s27, s28)
        self.addLink(s29, s30)
        self.addLink(s30, s31)


topos = {"GtsCzechRepublic": (lambda: GtsCzechRepublic())}

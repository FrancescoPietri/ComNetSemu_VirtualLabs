#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Ernet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("pune0", dpid="0000000000000002")
        s1 = self.addSwitch("indore1", dpid="0000000000000003")
        s2 = self.addSwitch("trivandr2", dpid="0000000000000004")
        s3 = self.addSwitch("mumbai3", dpid="0000000000000005")
        s4 = self.addSwitch("none4", dpid="0000000000000006")
        s5 = self.addSwitch("none5", dpid="0000000000000007")
        s6 = self.addSwitch("ahmedaba6", dpid="0000000000000008")
        s7 = self.addSwitch("jaipur7", dpid="0000000000000009")
        s8 = self.addSwitch("none8", dpid="000000000000000a")
        s9 = self.addSwitch("none9", dpid="000000000000000b")
        s10 = self.addSwitch("none10", dpid="000000000000000c")
        s11 = self.addSwitch("none11", dpid="000000000000000d")
        s12 = self.addSwitch("none12", dpid="000000000000000e")
        s13 = self.addSwitch("none13", dpid="000000000000000f")
        s14 = self.addSwitch("none14", dpid="0000000000000010")
        s15 = self.addSwitch("none15", dpid="0000000000000011")
        s16 = self.addSwitch("none16", dpid="0000000000000012")
        s17 = self.addSwitch("none17", dpid="0000000000000013")
        s18 = self.addSwitch("none18", dpid="0000000000000014")
        s19 = self.addSwitch("none19", dpid="0000000000000015")
        s20 = self.addSwitch("chennai20", dpid="0000000000000016")
        s21 = self.addSwitch("bengalur1", dpid="0000000000000017")
        s22 = self.addSwitch("delhi22", dpid="0000000000000018")
        s23 = self.addSwitch("guwahati3", dpid="0000000000000019")
        s24 = self.addSwitch("gorakhpu4", dpid="000000000000001a")
        s25 = self.addSwitch("kanpur25", dpid="000000000000001b")
        s26 = self.addSwitch("allahaba6", dpid="000000000000001c")
        s27 = self.addSwitch("kalkota27", dpid="000000000000001d")
        s28 = self.addSwitch("bhubanes8", dpid="000000000000001e")
        s29 = self.addSwitch("hyderaba9", dpid="000000000000001f")

        # Adding Links
        self.addLink(s0, s3)
        self.addLink(s0, s13)
        self.addLink(s0, s21)
        self.addLink(s1, s3)
        self.addLink(s2, s18)
        self.addLink(s2, s21)
        self.addLink(s3, s4)
        self.addLink(s3, s14)
        self.addLink(s3, s22)
        self.addLink(s5, s21)
        self.addLink(s6, s22)
        self.addLink(s7, s22)
        self.addLink(s8, s25)
        self.addLink(s9, s22)
        self.addLink(s10, s27)
        self.addLink(s11, s28)
        self.addLink(s12, s21)
        self.addLink(s15, s22)
        self.addLink(s16, s20)
        self.addLink(s17, s29)
        self.addLink(s19, s21)
        self.addLink(s20, s21)
        self.addLink(s20, s29)
        self.addLink(s21, s22)
        self.addLink(s21, s29)
        self.addLink(s22, s25)
        self.addLink(s22, s27)
        self.addLink(s23, s27)
        self.addLink(s24, s25)
        self.addLink(s25, s26)
        self.addLink(s27, s28)
        self.addLink(s27, s29)


topos = {"Ernet": (lambda: Ernet())}

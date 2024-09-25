#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Shentel(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("hagersto0", dpid="0000000000000002")
        s1 = self.addSwitch("shepherd1", dpid="0000000000000003")
        s2 = self.addSwitch("winchest2", dpid="0000000000000004")
        s3 = self.addSwitch("berryvil3", dpid="0000000000000005")
        s4 = self.addSwitch("petersbu4", dpid="0000000000000006")
        s5 = self.addSwitch("franklin5", dpid="0000000000000007")
        s6 = self.addSwitch("martinsb6", dpid="0000000000000008")
        s7 = self.addSwitch("edinburg7", dpid="0000000000000009")
        s8 = self.addSwitch("harrison8", dpid="000000000000000a")
        s9 = self.addSwitch("covingto9", dpid="000000000000000b")
        s10 = self.addSwitch("glenvill0", dpid="000000000000000c")
        s11 = self.addSwitch("sutton11", dpid="000000000000000d")
        s12 = self.addSwitch("summersv2", dpid="000000000000000e")
        s13 = self.addSwitch("charlest3", dpid="000000000000000f")
        s14 = self.addSwitch("none14", dpid="0000000000000010")
        s15 = self.addSwitch("none15", dpid="0000000000000011")
        s16 = self.addSwitch("none16", dpid="0000000000000012")
        s17 = self.addSwitch("weston17", dpid="0000000000000013")
        s18 = self.addSwitch("warrento8", dpid="0000000000000014")
        s19 = self.addSwitch("frontroy9", dpid="0000000000000015")
        s20 = self.addSwitch("none20", dpid="0000000000000016")
        s21 = self.addSwitch("none21", dpid="0000000000000017")
        s22 = self.addSwitch("none22", dpid="0000000000000018")
        s23 = self.addSwitch("none23", dpid="0000000000000019")
        s24 = self.addSwitch("none24", dpid="000000000000001a")
        s25 = self.addSwitch("leesburg5", dpid="000000000000001b")
        s26 = self.addSwitch("ashburn26", dpid="000000000000001c")
        s27 = self.addSwitch("herndon27", dpid="000000000000001d")

        # Adding Links
        self.addLink(s0, s1)
        self.addLink(s0, s6)
        self.addLink(s1, s3)
        self.addLink(s1, s6)
        self.addLink(s2, s3)
        self.addLink(s2, s20)
        self.addLink(s2, s6)
        self.addLink(s2, s15)
        self.addLink(s3, s25)
        self.addLink(s4, s14)
        self.addLink(s5, s14)
        self.addLink(s7, s16)
        self.addLink(s7, s21)
        self.addLink(s8, s24)
        self.addLink(s8, s9)
        self.addLink(s8, s23)
        self.addLink(s9, s13)
        self.addLink(s10, s17)
        self.addLink(s10, s11)
        self.addLink(s11, s12)
        self.addLink(s12, s13)
        self.addLink(s14, s24)
        self.addLink(s14, s20)
        self.addLink(s15, s19)
        self.addLink(s15, s20)
        self.addLink(s15, s21)
        self.addLink(s16, s22)
        self.addLink(s16, s23)
        self.addLink(s18, s19)
        self.addLink(s18, s27)
        self.addLink(s20, s22)
        self.addLink(s22, s24)
        self.addLink(s23, s24)
        self.addLink(s25, s26)
        self.addLink(s26, s27)


topos = {"Shentel": (lambda: Shentel())}

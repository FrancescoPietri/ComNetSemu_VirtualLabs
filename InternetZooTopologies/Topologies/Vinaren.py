#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Vinaren(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("hue0", dpid="0000000000000002")
        s1 = self.addSwitch("vnhn1", dpid="0000000000000003")
        s2 = self.addSwitch("hcm2", dpid="0000000000000004")
        s3 = self.addSwitch("dn3", dpid="0000000000000005")
        s4 = self.addSwitch("kr4", dpid="0000000000000006")
        s5 = self.addSwitch("jp5", dpid="0000000000000007")
        s6 = self.addSwitch("hk6", dpid="0000000000000008")
        s7 = self.addSwitch("cn7", dpid="0000000000000009")
        s8 = self.addSwitch("ph8", dpid="000000000000000a")
        s9 = self.addSwitch("nhatrang9", dpid="000000000000000b")
        s10 = self.addSwitch("vinh10", dpid="000000000000000c")
        s11 = self.addSwitch("thainguy1", dpid="000000000000000d")
        s12 = self.addSwitch("angiang12", dpid="000000000000000e")
        s13 = self.addSwitch("dalat13", dpid="000000000000000f")
        s14 = self.addSwitch("haiphong4", dpid="0000000000000010")
        s15 = self.addSwitch("au15", dpid="0000000000000011")
        s16 = self.addSwitch("ct16", dpid="0000000000000012")
        s17 = self.addSwitch("th17", dpid="0000000000000013")
        s18 = self.addSwitch("my18", dpid="0000000000000014")
        s19 = self.addSwitch("id19", dpid="0000000000000015")
        s20 = self.addSwitch("abilenei0", dpid="0000000000000016")
        s21 = self.addSwitch("internet1", dpid="0000000000000017")
        s22 = self.addSwitch("eu22", dpid="0000000000000018")
        s23 = self.addSwitch("eu23", dpid="0000000000000019")
        s24 = self.addSwitch("sg24", dpid="000000000000001a")

        # Adding Links
        self.addLink(s0, s3)
        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s1, s6)
        self.addLink(s1, s10)
        self.addLink(s1, s11)
        self.addLink(s1, s14)
        self.addLink(s1, s21)
        self.addLink(s2, s16)
        self.addLink(s2, s3)
        self.addLink(s2, s13)
        self.addLink(s3, s9)
        self.addLink(s4, s24)
        self.addLink(s5, s8)
        self.addLink(s5, s24)
        self.addLink(s5, s20)
        self.addLink(s5, s6)
        self.addLink(s6, s24)
        self.addLink(s6, s7)
        self.addLink(s7, s22)
        self.addLink(s12, s16)
        self.addLink(s15, s24)
        self.addLink(s17, s24)
        self.addLink(s18, s24)
        self.addLink(s19, s24)
        self.addLink(s23, s24)


topos = {"Vinaren": (lambda: Vinaren())}

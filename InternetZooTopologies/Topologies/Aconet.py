#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Aconet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("eisensta0", dpid="0000000000000002")
        s1 = self.addSwitch("stpolte1", dpid="0000000000000003")
        s2 = self.addSwitch("graz22", dpid="0000000000000004")
        s3 = self.addSwitch("leoben3", dpid="0000000000000005")
        s4 = self.addSwitch("vienna24", dpid="0000000000000006")
        s5 = self.addSwitch("geant5", dpid="0000000000000007")
        s6 = self.addSwitch("krems6", dpid="0000000000000008")
        s7 = self.addSwitch("vienna17", dpid="0000000000000009")
        s8 = self.addSwitch("level38", dpid="000000000000000a")
        s9 = self.addSwitch("vix9", dpid="000000000000000b")
        s10 = self.addSwitch("none10", dpid="000000000000000c")
        s11 = self.addSwitch("sanet11", dpid="000000000000000d")
        s12 = self.addSwitch("cesnet12", dpid="000000000000000e")
        s13 = self.addSwitch("klagenfu3", dpid="000000000000000f")
        s14 = self.addSwitch("graz114", dpid="0000000000000010")
        s15 = self.addSwitch("linz115", dpid="0000000000000011")
        s16 = self.addSwitch("linz216", dpid="0000000000000012")
        s17 = self.addSwitch("salzburg7", dpid="0000000000000013")
        s18 = self.addSwitch("salzburg8", dpid="0000000000000014")
        s19 = self.addSwitch("innsbruc9", dpid="0000000000000015")
        s20 = self.addSwitch("innsbruc0", dpid="0000000000000016")
        s21 = self.addSwitch("dornbirn1", dpid="0000000000000017")
        s22 = self.addSwitch("klagenfu2", dpid="0000000000000018")

        # Adding Links
        self.addLink(s0, s4)
        self.addLink(s0, s7)
        self.addLink(s1, s6)
        self.addLink(s1, s7)
        self.addLink(s2, s3)
        self.addLink(s2, s14)
        self.addLink(s2, s7)
        self.addLink(s3, s14)
        self.addLink(s4, s6)
        self.addLink(s4, s10)
        self.addLink(s4, s13)
        self.addLink(s4, s14)
        self.addLink(s4, s15)
        self.addLink(s4, s18)
        self.addLink(s4, s19)
        self.addLink(s5, s10)
        self.addLink(s7, s10)
        self.addLink(s7, s16)
        self.addLink(s7, s17)
        self.addLink(s7, s20)
        self.addLink(s7, s22)
        self.addLink(s8, s10)
        self.addLink(s9, s10)
        self.addLink(s10, s11)
        self.addLink(s10, s12)
        self.addLink(s13, s22)
        self.addLink(s15, s16)
        self.addLink(s17, s18)
        self.addLink(s19, s20)
        self.addLink(s19, s21)
        self.addLink(s20, s21)


topos = {"Aconet": (lambda: Aconet())}

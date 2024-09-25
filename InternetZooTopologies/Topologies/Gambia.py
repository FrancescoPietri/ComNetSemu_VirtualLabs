#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Gambia(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("gamnet0", dpid="0000000000000002")
        s1 = self.addSwitch("qnetas1", dpid="0000000000000003")
        s2 = self.addSwitch("kerewan2", dpid="0000000000000004")
        s3 = self.addSwitch("banjul3", dpid="0000000000000005")
        s4 = self.addSwitch("mdi4", dpid="0000000000000006")
        s5 = self.addSwitch("gtmi5", dpid="0000000000000007")
        s6 = self.addSwitch("quantumn6", dpid="0000000000000008")
        s7 = self.addSwitch("mrc7", dpid="0000000000000009")
        s8 = self.addSwitch("univgamb8", dpid="000000000000000a")
        s9 = self.addSwitch("gtmi9", dpid="000000000000000b")
        s10 = self.addSwitch("manskgam0", dpid="000000000000000c")
        s11 = self.addSwitch("gamtelho1", dpid="000000000000000d")
        s12 = self.addSwitch("actionlt2", dpid="000000000000000e")
        s13 = self.addSwitch("undp13", dpid="000000000000000f")
        s14 = self.addSwitch("teleglob4", dpid="0000000000000010")
        s15 = self.addSwitch("intelsat5", dpid="0000000000000011")
        s16 = self.addSwitch("earthsta6", dpid="0000000000000012")
        s17 = self.addSwitch("gantdcen7", dpid="0000000000000013")
        s18 = self.addSwitch("basse18", dpid="0000000000000014")
        s19 = self.addSwitch("bansang19", dpid="0000000000000015")
        s20 = self.addSwitch("abuko20", dpid="0000000000000016")
        s21 = self.addSwitch("serekund1", dpid="0000000000000017")
        s22 = self.addSwitch("kotu22", dpid="0000000000000018")
        s23 = self.addSwitch("bakau23", dpid="0000000000000019")
        s24 = self.addSwitch("brikama24", dpid="000000000000001a")
        s25 = self.addSwitch("yundum25", dpid="000000000000001b")
        s26 = self.addSwitch("soma26", dpid="000000000000001c")
        s27 = self.addSwitch("farafenn7", dpid="000000000000001d")

        # Adding Links
        self.addLink(s0, s20)
        self.addLink(s1, s20)
        self.addLink(s2, s3)
        self.addLink(s2, s27)
        self.addLink(s3, s11)
        self.addLink(s3, s10)
        self.addLink(s3, s6)
        self.addLink(s3, s21)
        self.addLink(s4, s21)
        self.addLink(s5, s21)
        self.addLink(s7, s23)
        self.addLink(s8, s21)
        self.addLink(s9, s21)
        self.addLink(s12, s21)
        self.addLink(s13, s23)
        self.addLink(s14, s15)
        self.addLink(s15, s16)
        self.addLink(s16, s20)
        self.addLink(s17, s24)
        self.addLink(s18, s26)
        self.addLink(s18, s19)
        self.addLink(s20, s21)
        self.addLink(s21, s22)
        self.addLink(s21, s23)
        self.addLink(s21, s24)
        self.addLink(s21, s25)
        self.addLink(s25, s26)
        self.addLink(s26, s27)


topos = {"Gambia": (lambda: Gambia())}

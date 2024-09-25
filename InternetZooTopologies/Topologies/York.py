#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class York(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("leiceste0", dpid="0000000000000002")
        s1 = self.addSwitch("northamp1", dpid="0000000000000003")
        s2 = self.addSwitch("sheffiel2", dpid="0000000000000004")
        s3 = self.addSwitch("nottingh3", dpid="0000000000000005")
        s4 = self.addSwitch("croydon4", dpid="0000000000000006")
        s5 = self.addSwitch("slough5", dpid="0000000000000007")
        s6 = self.addSwitch("miltonke6", dpid="0000000000000008")
        s7 = self.addSwitch("london7", dpid="0000000000000009")
        s8 = self.addSwitch("reading8", dpid="000000000000000a")
        s9 = self.addSwitch("banbury9", dpid="000000000000000b")
        s10 = self.addSwitch("brighton0", dpid="000000000000000c")
        s11 = self.addSwitch("bristol11", dpid="000000000000000d")
        s12 = self.addSwitch("birmingh2", dpid="000000000000000e")
        s13 = self.addSwitch("preston13", dpid="000000000000000f")
        s14 = self.addSwitch("manchest4", dpid="0000000000000010")
        s15 = self.addSwitch("glasgow15", dpid="0000000000000011")
        s16 = self.addSwitch("edinburg6", dpid="0000000000000012")
        s17 = self.addSwitch("newcastl7", dpid="0000000000000013")
        s18 = self.addSwitch("middlesb8", dpid="0000000000000014")
        s19 = self.addSwitch("harrogat9", dpid="0000000000000015")
        s20 = self.addSwitch("york20", dpid="0000000000000016")
        s21 = self.addSwitch("leeds21", dpid="0000000000000017")
        s22 = self.addSwitch("carlisle2", dpid="0000000000000018")

        # Adding Links
        self.addLink(s0, s1)
        self.addLink(s0, s3)
        self.addLink(s1, s6)
        self.addLink(s2, s3)
        self.addLink(s2, s21)
        self.addLink(s4, s7)
        self.addLink(s5, s8)
        self.addLink(s5, s7)
        self.addLink(s6, s7)
        self.addLink(s8, s9)
        self.addLink(s8, s10)
        self.addLink(s8, s11)
        self.addLink(s9, s12)
        self.addLink(s12, s14)
        self.addLink(s13, s14)
        self.addLink(s13, s22)
        self.addLink(s15, s16)
        self.addLink(s15, s22)
        self.addLink(s16, s17)
        self.addLink(s17, s18)
        self.addLink(s18, s20)
        self.addLink(s19, s20)
        self.addLink(s19, s21)
        self.addLink(s20, s21)


topos = {"York": (lambda: York())}

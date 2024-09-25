#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Cynet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("cyprusun0", dpid="0000000000000002")
        s1 = self.addSwitch("intercol1", dpid="0000000000000003")
        s2 = self.addSwitch("unitedna2", dpid="0000000000000004")
        s3 = self.addSwitch("cyixcypr3", dpid="0000000000000005")
        s4 = self.addSwitch("users4", dpid="0000000000000006")
        s5 = self.addSwitch("grid5", dpid="0000000000000007")
        s6 = self.addSwitch("gridsw6", dpid="0000000000000008")
        s7 = self.addSwitch("none7", dpid="0000000000000009")
        s8 = self.addSwitch("kyprosne8", dpid="000000000000000a")
        s9 = self.addSwitch("instofn9", dpid="000000000000000b")
        s10 = self.addSwitch("pedagogi0", dpid="000000000000000c")
        s11 = self.addSwitch("nursings1", dpid="000000000000000d")
        s12 = self.addSwitch("phillips2", dpid="000000000000000e")
        s13 = self.addSwitch("european3", dpid="000000000000000f")
        s14 = self.addSwitch("openuni4", dpid="0000000000000010")
        s15 = self.addSwitch("univofn5", dpid="0000000000000011")
        s16 = self.addSwitch("agricult6", dpid="0000000000000012")
        s17 = self.addSwitch("cyprusin7", dpid="0000000000000013")
        s18 = self.addSwitch("englishs8", dpid="0000000000000014")
        s19 = self.addSwitch("unioffr9", dpid="0000000000000015")
        s20 = self.addSwitch("limassol0", dpid="0000000000000016")
        s21 = self.addSwitch("european1", dpid="0000000000000017")
        s22 = self.addSwitch("borderro2", dpid="0000000000000018")
        s23 = self.addSwitch("eumedcon3", dpid="0000000000000019")
        s24 = self.addSwitch("syrianre4", dpid="000000000000001a")
        s25 = self.addSwitch("geantath5", dpid="000000000000001b")
        s26 = self.addSwitch("geantmil6", dpid="000000000000001c")
        s27 = self.addSwitch("univofc7", dpid="000000000000001d")
        s28 = self.addSwitch("evagoras8", dpid="000000000000001e")
        s29 = self.addSwitch("nicosiap9", dpid="000000000000001f")

        # Adding Links
        self.addLink(s0, s20)
        self.addLink(s1, s20)
        self.addLink(s2, s28)
        self.addLink(s3, s29)
        self.addLink(s4, s7)
        self.addLink(s5, s6)
        self.addLink(s6, s7)
        self.addLink(s6, s29)
        self.addLink(s8, s29)
        self.addLink(s9, s29)
        self.addLink(s10, s29)
        self.addLink(s11, s29)
        self.addLink(s12, s29)
        self.addLink(s13, s29)
        self.addLink(s14, s29)
        self.addLink(s15, s29)
        self.addLink(s16, s29)
        self.addLink(s17, s29)
        self.addLink(s18, s29)
        self.addLink(s19, s29)
        self.addLink(s20, s22)
        self.addLink(s21, s28)
        self.addLink(s22, s23)
        self.addLink(s22, s25)
        self.addLink(s22, s26)
        self.addLink(s22, s27)
        self.addLink(s22, s28)
        self.addLink(s22, s29)
        self.addLink(s23, s24)


topos = {"Cynet": (lambda: Cynet())}

#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Ilan(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("telavivg0", dpid="0000000000000002")
        s1 = self.addSwitch("intlbac1", dpid="0000000000000003")
        s2 = self.addSwitch("iix2", dpid="0000000000000004")
        s3 = self.addSwitch("petachti3", dpid="0000000000000005")
        s4 = self.addSwitch("external4", dpid="0000000000000006")
        s5 = self.addSwitch("geant2ge5", dpid="0000000000000007")
        s6 = self.addSwitch("openuniv6", dpid="0000000000000008")
        s7 = self.addSwitch("haifauni7", dpid="0000000000000009")
        s8 = self.addSwitch("technion8", dpid="000000000000000a")
        s9 = self.addSwitch("barilanu9", dpid="000000000000000b")
        s10 = self.addSwitch("hebrewun0", dpid="000000000000000c")
        s11 = self.addSwitch("bengurio1", dpid="000000000000000d")
        s12 = self.addSwitch("weizmann2", dpid="000000000000000e")
        s13 = self.addSwitch("telavivu3", dpid="000000000000000f")

        # Adding Links
        self.addLink(s0, s1)
        self.addLink(s0, s7)
        self.addLink(s0, s8)
        self.addLink(s0, s9)
        self.addLink(s0, s10)
        self.addLink(s0, s11)
        self.addLink(s0, s12)
        self.addLink(s0, s13)
        self.addLink(s2, s3)
        self.addLink(s3, s4)
        self.addLink(s3, s5)
        self.addLink(s3, s6)
        self.addLink(s3, s7)
        self.addLink(s3, s9)
        self.addLink(s3, s13)


topos = {"Ilan": (lambda: Ilan())}

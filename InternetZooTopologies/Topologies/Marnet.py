#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Marnet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("fofmini0", dpid="0000000000000002")
        s1 = self.addSwitch("onnetneo1", dpid="0000000000000003")
        s2 = self.addSwitch("nocandca2", dpid="0000000000000004")
        s3 = self.addSwitch("iofecon3", dpid="0000000000000005")
        s4 = self.addSwitch("national4", dpid="0000000000000006")
        s5 = self.addSwitch("iofpolit5", dpid="0000000000000007")
        s6 = self.addSwitch("geantsee6", dpid="0000000000000008")
        s7 = self.addSwitch("campusna7", dpid="0000000000000009")
        s8 = self.addSwitch("fofpeda8", dpid="000000000000000a")
        s9 = self.addSwitch("mol9", dpid="000000000000000b")
        s10 = self.addSwitch("national0", dpid="000000000000000c")
        s11 = self.addSwitch("iofeart1", dpid="000000000000000d")
        s12 = self.addSwitch("iofnati2", dpid="000000000000000e")
        s13 = self.addSwitch("iofmace3", dpid="000000000000000f")
        s14 = self.addSwitch("stclemen4", dpid="0000000000000010")
        s15 = self.addSwitch("severalm5", dpid="0000000000000011")
        s16 = self.addSwitch("campusar6", dpid="0000000000000012")
        s17 = self.addSwitch("campuste7", dpid="0000000000000013")
        s18 = self.addSwitch("campusme8", dpid="0000000000000014")
        s19 = self.addSwitch("campusbi9", dpid="0000000000000015")

        # Adding Links
        self.addLink(s0, s2)
        self.addLink(s1, s4)
        self.addLink(s2, s3)
        self.addLink(s2, s4)
        self.addLink(s2, s5)
        self.addLink(s2, s6)
        self.addLink(s2, s7)
        self.addLink(s2, s9)
        self.addLink(s2, s10)
        self.addLink(s2, s11)
        self.addLink(s2, s12)
        self.addLink(s2, s13)
        self.addLink(s2, s14)
        self.addLink(s2, s15)
        self.addLink(s2, s16)
        self.addLink(s2, s17)
        self.addLink(s2, s18)
        self.addLink(s2, s19)
        self.addLink(s4, s7)
        self.addLink(s4, s10)
        self.addLink(s4, s11)
        self.addLink(s4, s16)
        self.addLink(s4, s17)
        self.addLink(s4, s18)
        self.addLink(s4, s19)
        self.addLink(s5, s17)
        self.addLink(s8, s17)


topos = {"Marnet": (lambda: Marnet())}

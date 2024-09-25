#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Aarnet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("sydney10", dpid="0000000000000002")
        s1 = self.addSwitch("brisbane1", dpid="0000000000000003")
        s2 = self.addSwitch("canberra2", dpid="0000000000000004")
        s3 = self.addSwitch("sydney23", dpid="0000000000000005")
        s4 = self.addSwitch("townsvil4", dpid="0000000000000006")
        s5 = self.addSwitch("cairns5", dpid="0000000000000007")
        s6 = self.addSwitch("brisbane6", dpid="0000000000000008")
        s7 = self.addSwitch("rockhamp7", dpid="0000000000000009")
        s8 = self.addSwitch("armidale8", dpid="000000000000000a")
        s9 = self.addSwitch("hobart9", dpid="000000000000000b")
        s10 = self.addSwitch("canberra0", dpid="000000000000000c")
        s11 = self.addSwitch("perth111", dpid="000000000000000d")
        s12 = self.addSwitch("perth212", dpid="000000000000000e")
        s13 = self.addSwitch("adelaide3", dpid="000000000000000f")
        s14 = self.addSwitch("adelaide4", dpid="0000000000000010")
        s15 = self.addSwitch("melbourn5", dpid="0000000000000011")
        s16 = self.addSwitch("melbourn6", dpid="0000000000000012")
        s17 = self.addSwitch("alicespr7", dpid="0000000000000013")
        s18 = self.addSwitch("darwin18", dpid="0000000000000014")

        # Adding Links
        self.addLink(s0, s10)
        self.addLink(s0, s3)
        self.addLink(s0, s6)
        self.addLink(s1, s3)
        self.addLink(s1, s6)
        self.addLink(s2, s10)
        self.addLink(s2, s15)
        self.addLink(s3, s8)
        self.addLink(s3, s16)
        self.addLink(s4, s5)
        self.addLink(s4, s7)
        self.addLink(s6, s7)
        self.addLink(s9, s16)
        self.addLink(s9, s15)
        self.addLink(s11, s12)
        self.addLink(s11, s13)
        self.addLink(s12, s14)
        self.addLink(s13, s18)
        self.addLink(s13, s14)
        self.addLink(s13, s15)
        self.addLink(s14, s16)
        self.addLink(s14, s17)
        self.addLink(s15, s16)
        self.addLink(s17, s18)


topos = {"Aarnet": (lambda: Aarnet())}

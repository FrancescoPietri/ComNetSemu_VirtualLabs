#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Twaren(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("ccu0", dpid="0000000000000002")
        s1 = self.addSwitch("nhlue1", dpid="0000000000000003")
        s2 = self.addSwitch("tn2", dpid="0000000000000004")
        s3 = self.addSwitch("ncku3", dpid="0000000000000005")
        s4 = self.addSwitch("tc4", dpid="0000000000000006")
        s5 = self.addSwitch("chi5", dpid="0000000000000007")
        s6 = self.addSwitch("ndhu6", dpid="0000000000000008")
        s7 = self.addSwitch("ncnu7", dpid="0000000000000009")
        s8 = self.addSwitch("la8", dpid="000000000000000a")
        s9 = self.addSwitch("niu9", dpid="000000000000000b")
        s10 = self.addSwitch("nttu10", dpid="000000000000000c")
        s11 = self.addSwitch("nsysu11", dpid="000000000000000d")
        s12 = self.addSwitch("nchu12", dpid="000000000000000e")
        s13 = self.addSwitch("hc13", dpid="000000000000000f")
        s14 = self.addSwitch("nctu14", dpid="0000000000000010")
        s15 = self.addSwitch("nthu15", dpid="0000000000000011")
        s16 = self.addSwitch("ncu16", dpid="0000000000000012")
        s17 = self.addSwitch("ascc17", dpid="0000000000000013")
        s18 = self.addSwitch("ntu18", dpid="0000000000000014")
        s19 = self.addSwitch("tp19", dpid="0000000000000015")

        # Adding Links
        self.addLink(s0, s2)
        self.addLink(s1, s19)
        self.addLink(s2, s3)
        self.addLink(s2, s4)
        self.addLink(s2, s10)
        self.addLink(s2, s11)
        self.addLink(s2, s13)
        self.addLink(s4, s19)
        self.addLink(s4, s12)
        self.addLink(s4, s7)
        self.addLink(s5, s19)
        self.addLink(s6, s19)
        self.addLink(s8, s13)
        self.addLink(s9, s19)
        self.addLink(s13, s14)
        self.addLink(s13, s15)
        self.addLink(s13, s16)
        self.addLink(s13, s19)
        self.addLink(s17, s19)
        self.addLink(s18, s19)


topos = {"Twaren": (lambda: Twaren())}

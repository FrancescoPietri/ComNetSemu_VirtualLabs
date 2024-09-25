#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Quest(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("auckland0", dpid="0000000000000002")
        s1 = self.addSwitch("fiji1", dpid="0000000000000003")
        s2 = self.addSwitch("sydney122", dpid="0000000000000004")
        s3 = self.addSwitch("auckland3", dpid="0000000000000005")
        s4 = self.addSwitch("sacramen4", dpid="0000000000000006")
        s5 = self.addSwitch("losangel5", dpid="0000000000000007")
        s6 = self.addSwitch("hawaii166", dpid="0000000000000008")
        s7 = self.addSwitch("hawaii277", dpid="0000000000000009")
        s8 = self.addSwitch("taiwan8", dpid="000000000000000a")
        s9 = self.addSwitch("philippi9", dpid="000000000000000b")
        s10 = self.addSwitch("melbourn0", dpid="000000000000000c")
        s11 = self.addSwitch("sydney211", dpid="000000000000000d")
        s12 = self.addSwitch("korea12", dpid="000000000000000e")
        s13 = self.addSwitch("japan13", dpid="000000000000000f")
        s14 = self.addSwitch("guam14", dpid="0000000000000010")
        s15 = self.addSwitch("philippi5", dpid="0000000000000011")
        s16 = self.addSwitch("hongkong6", dpid="0000000000000012")
        s17 = self.addSwitch("singapor7", dpid="0000000000000013")
        s18 = self.addSwitch("thailand8", dpid="0000000000000014")
        s19 = self.addSwitch("perth19", dpid="0000000000000015")

        # Adding Links
        self.addLink(s0, s11)
        self.addLink(s0, s3)
        self.addLink(s1, s2)
        self.addLink(s1, s6)
        self.addLink(s2, s10)
        self.addLink(s2, s11)
        self.addLink(s2, s14)
        self.addLink(s3, s7)
        self.addLink(s4, s13)
        self.addLink(s4, s6)
        self.addLink(s4, s5)
        self.addLink(s5, s7)
        self.addLink(s6, s13)
        self.addLink(s6, s14)
        self.addLink(s6, s7)
        self.addLink(s8, s16)
        self.addLink(s8, s12)
        self.addLink(s8, s15)
        self.addLink(s9, s16)
        self.addLink(s9, s14)
        self.addLink(s9, s15)
        self.addLink(s10, s19)
        self.addLink(s12, s13)
        self.addLink(s13, s16)
        self.addLink(s13, s14)
        self.addLink(s14, s15)
        self.addLink(s14, s17)
        self.addLink(s15, s16)
        self.addLink(s16, s17)
        self.addLink(s17, s18)
        self.addLink(s17, s19)


topos = {"Quest": (lambda: Quest())}

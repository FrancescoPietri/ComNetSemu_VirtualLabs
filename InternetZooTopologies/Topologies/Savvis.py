#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Savvis(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("newyork00", dpid="0000000000000002")
        s1 = self.addSwitch("philadel1", dpid="0000000000000003")
        s2 = self.addSwitch("detroit2", dpid="0000000000000004")
        s3 = self.addSwitch("pittsbur3", dpid="0000000000000005")
        s4 = self.addSwitch("houston4", dpid="0000000000000006")
        s5 = self.addSwitch("austin5", dpid="0000000000000007")
        s6 = self.addSwitch("washingt6", dpid="0000000000000008")
        s7 = self.addSwitch("atlanta7", dpid="0000000000000009")
        s8 = self.addSwitch("dallas8", dpid="000000000000000a")
        s9 = self.addSwitch("champaig9", dpid="000000000000000b")
        s10 = self.addSwitch("chicago10", dpid="000000000000000c")
        s11 = self.addSwitch("sanfranc1", dpid="000000000000000d")
        s12 = self.addSwitch("losangel2", dpid="000000000000000e")
        s13 = self.addSwitch("sandiego3", dpid="000000000000000f")
        s14 = self.addSwitch("phoenix14", dpid="0000000000000010")
        s15 = self.addSwitch("saltlake5", dpid="0000000000000011")
        s16 = self.addSwitch("denver16", dpid="0000000000000012")
        s17 = self.addSwitch("kansasci7", dpid="0000000000000013")
        s18 = self.addSwitch("stlouis18", dpid="0000000000000014")

        # Adding Links
        self.addLink(s0, s1)
        self.addLink(s0, s3)
        self.addLink(s1, s6)
        self.addLink(s2, s10)
        self.addLink(s2, s3)
        self.addLink(s4, s5)
        self.addLink(s4, s7)
        self.addLink(s5, s8)
        self.addLink(s6, s7)
        self.addLink(s8, s18)
        self.addLink(s8, s14)
        self.addLink(s9, s18)
        self.addLink(s10, s18)
        self.addLink(s11, s12)
        self.addLink(s11, s15)
        self.addLink(s12, s13)
        self.addLink(s12, s14)
        self.addLink(s15, s16)
        self.addLink(s16, s17)
        self.addLink(s17, s18)


topos = {"Savvis": (lambda: Savvis())}

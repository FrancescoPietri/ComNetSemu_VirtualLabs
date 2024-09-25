#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Goodnet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("tampa0", dpid="0000000000000002")
        s1 = self.addSwitch("oklahoma1", dpid="0000000000000003")
        s2 = self.addSwitch("neworlea2", dpid="0000000000000004")
        s3 = self.addSwitch("jacksonv3", dpid="0000000000000005")
        s4 = self.addSwitch("losangel4", dpid="0000000000000006")
        s5 = self.addSwitch("phoenix5", dpid="0000000000000007")
        s6 = self.addSwitch("tucson6", dpid="0000000000000008")
        s7 = self.addSwitch("atlanta7", dpid="0000000000000009")
        s8 = self.addSwitch("birmingh8", dpid="000000000000000a")
        s9 = self.addSwitch("sanjose99", dpid="000000000000000b")
        s10 = self.addSwitch("saltlake0", dpid="000000000000000c")
        s11 = self.addSwitch("denver11", dpid="000000000000000d")
        s12 = self.addSwitch("chicago12", dpid="000000000000000e")
        s13 = self.addSwitch("hartford3", dpid="000000000000000f")
        s14 = self.addSwitch("newyork14", dpid="0000000000000010")
        s15 = self.addSwitch("washingt5", dpid="0000000000000011")
        s16 = self.addSwitch("chattano6", dpid="0000000000000012")

        # Adding Links
        self.addLink(s0, s3)
        self.addLink(s0, s7)
        self.addLink(s1, s9)
        self.addLink(s1, s15)
        self.addLink(s2, s12)
        self.addLink(s2, s5)
        self.addLink(s2, s7)
        self.addLink(s3, s9)
        self.addLink(s3, s15)
        self.addLink(s4, s9)
        self.addLink(s4, s12)
        self.addLink(s4, s15)
        self.addLink(s5, s9)
        self.addLink(s5, s12)
        self.addLink(s5, s6)
        self.addLink(s5, s15)
        self.addLink(s7, s8)
        self.addLink(s7, s12)
        self.addLink(s7, s15)
        self.addLink(s9, s10)
        self.addLink(s9, s11)
        self.addLink(s9, s12)
        self.addLink(s9, s14)
        self.addLink(s9, s15)
        self.addLink(s10, s12)
        self.addLink(s11, s12)
        self.addLink(s12, s14)
        self.addLink(s12, s15)
        self.addLink(s13, s14)
        self.addLink(s14, s15)
        self.addLink(s15, s16)


topos = {"Goodnet": (lambda: Goodnet())}

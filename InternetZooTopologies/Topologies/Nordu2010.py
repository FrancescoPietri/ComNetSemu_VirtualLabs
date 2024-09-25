#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Nordu2010(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("poznan0", dpid="0000000000000002")
        s1 = self.addSwitch("geant1", dpid="0000000000000003")
        s2 = self.addSwitch("london2", dpid="0000000000000004")
        s3 = self.addSwitch("amsterda3", dpid="0000000000000005")
        s4 = self.addSwitch("icelink4", dpid="0000000000000006")
        s5 = self.addSwitch("london5", dpid="0000000000000007")
        s6 = self.addSwitch("gloriad6", dpid="0000000000000008")
        s7 = self.addSwitch("internet7", dpid="0000000000000009")
        s8 = self.addSwitch("internet8", dpid="000000000000000a")
        s9 = self.addSwitch("newyork99", dpid="000000000000000b")
        s10 = self.addSwitch("reyjavik0", dpid="000000000000000c")
        s11 = self.addSwitch("oslo11", dpid="000000000000000d")
        s12 = self.addSwitch("stockhol2", dpid="000000000000000e")
        s13 = self.addSwitch("espoo13", dpid="000000000000000f")
        s14 = self.addSwitch("helsinki4", dpid="0000000000000010")
        s15 = self.addSwitch("stpeters5", dpid="0000000000000011")
        s16 = self.addSwitch("copenhag6", dpid="0000000000000012")
        s17 = self.addSwitch("hamburg17", dpid="0000000000000013")

        # Adding Links
        self.addLink(s0, s17)
        self.addLink(s1, s16)
        self.addLink(s2, s16)
        self.addLink(s3, s17)
        self.addLink(s4, s10)
        self.addLink(s5, s10)
        self.addLink(s6, s15)
        self.addLink(s7, s12)
        self.addLink(s8, s16)
        self.addLink(s9, s16)
        self.addLink(s10, s16)
        self.addLink(s11, s16)
        self.addLink(s11, s12)
        self.addLink(s12, s16)
        self.addLink(s12, s14)
        self.addLink(s13, s15)
        self.addLink(s16, s17)


topos = {"Nordu2010": (lambda: Nordu2010())}

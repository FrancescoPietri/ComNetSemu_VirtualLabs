#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Fatman(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("carnegie0", dpid="0000000000000002")
        s1 = self.addSwitch("adamsmit1", dpid="0000000000000003")
        s2 = self.addSwitch("kirkcald2", dpid="0000000000000004")
        s3 = self.addSwitch("uodfifec3", dpid="0000000000000005")
        s4 = self.addSwitch("janetand4", dpid="0000000000000006")
        s5 = self.addSwitch("none5", dpid="0000000000000007")
        s6 = self.addSwitch("janetand6", dpid="0000000000000008")
        s7 = self.addSwitch("dundeeco7", dpid="0000000000000009")
        s8 = self.addSwitch("anguscol8", dpid="000000000000000a")
        s9 = self.addSwitch("glasgow9", dpid="000000000000000b")
        s10 = self.addSwitch("leeds10", dpid="000000000000000c")
        s11 = self.addSwitch("rnep111", dpid="000000000000000d")
        s12 = self.addSwitch("rnep212", dpid="000000000000000e")
        s13 = self.addSwitch("universi3", dpid="000000000000000f")
        s14 = self.addSwitch("universi4", dpid="0000000000000010")
        s15 = self.addSwitch("universi5", dpid="0000000000000011")
        s16 = self.addSwitch("elmwoodc6", dpid="0000000000000012")

        # Adding Links
        self.addLink(s0, s2)
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s2, s5)
        self.addLink(s4, s9)
        self.addLink(s5, s11)
        self.addLink(s5, s12)
        self.addLink(s6, s10)
        self.addLink(s7, s11)
        self.addLink(s8, s11)
        self.addLink(s9, s10)
        self.addLink(s9, s12)
        self.addLink(s10, s11)
        self.addLink(s11, s12)
        self.addLink(s11, s13)
        self.addLink(s11, s14)
        self.addLink(s11, s15)
        self.addLink(s11, s16)
        self.addLink(s12, s13)
        self.addLink(s12, s14)
        self.addLink(s12, s15)


topos = {"Fatman": (lambda: Fatman())}

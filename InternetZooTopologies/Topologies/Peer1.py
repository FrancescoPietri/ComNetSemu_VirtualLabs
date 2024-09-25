#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Peer1(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("herndon0", dpid="0000000000000002")
        s1 = self.addSwitch("miami1", dpid="0000000000000003")
        s2 = self.addSwitch("montreal2", dpid="0000000000000004")
        s3 = self.addSwitch("newyork33", dpid="0000000000000005")
        s4 = self.addSwitch("london4", dpid="0000000000000006")
        s5 = self.addSwitch("amsterda5", dpid="0000000000000007")
        s6 = self.addSwitch("chicago6", dpid="0000000000000008")
        s7 = self.addSwitch("toronto7", dpid="0000000000000009")
        s8 = self.addSwitch("vancouve8", dpid="000000000000000a")
        s9 = self.addSwitch("seattle9", dpid="000000000000000b")
        s10 = self.addSwitch("fremont10", dpid="000000000000000c")
        s11 = self.addSwitch("sanjose11", dpid="000000000000000d")
        s12 = self.addSwitch("losangel2", dpid="000000000000000e")
        s13 = self.addSwitch("dallas13", dpid="000000000000000f")
        s14 = self.addSwitch("sananton4", dpid="0000000000000010")
        s15 = self.addSwitch("atlanta15", dpid="0000000000000011")

        # Adding Links
        self.addLink(s0, s3)
        self.addLink(s0, s15)
        self.addLink(s1, s15)
        self.addLink(s2, s3)
        self.addLink(s2, s7)
        self.addLink(s3, s4)
        self.addLink(s3, s6)
        self.addLink(s3, s7)
        self.addLink(s4, s5)
        self.addLink(s6, s9)
        self.addLink(s6, s13)
        self.addLink(s6, s7)
        self.addLink(s7, s8)
        self.addLink(s8, s9)
        self.addLink(s9, s10)
        self.addLink(s10, s11)
        self.addLink(s11, s12)
        self.addLink(s12, s13)
        self.addLink(s13, s14)
        self.addLink(s13, s15)


topos = {"Peer1": (lambda: Peer1())}

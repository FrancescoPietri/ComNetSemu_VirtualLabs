#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class HiberniaCanada(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("newyork00", dpid="0000000000000002")
        s1 = self.addSwitch("none1", dpid="0000000000000003")
        s2 = self.addSwitch("none2", dpid="0000000000000004")
        s3 = self.addSwitch("moncton3", dpid="0000000000000005")
        s4 = self.addSwitch("none4", dpid="0000000000000006")
        s5 = self.addSwitch("edmundst5", dpid="0000000000000007")
        s6 = self.addSwitch("quebec6", dpid="0000000000000008")
        s7 = self.addSwitch("montreal7", dpid="0000000000000009")
        s8 = self.addSwitch("toronto8", dpid="000000000000000a")
        s9 = self.addSwitch("buffalo9", dpid="000000000000000b")
        s10 = self.addSwitch("albany10", dpid="000000000000000c")
        s11 = self.addSwitch("boston11", dpid="000000000000000d")
        s12 = self.addSwitch("halifax12", dpid="000000000000000e")

        # Adding Links
        self.addLink(s0, s10)
        self.addLink(s0, s11)
        self.addLink(s1, s4)
        self.addLink(s2, s12)
        self.addLink(s3, s12)
        self.addLink(s3, s5)
        self.addLink(s4, s11)
        self.addLink(s4, s12)
        self.addLink(s5, s6)
        self.addLink(s6, s7)
        self.addLink(s7, s8)
        self.addLink(s7, s10)
        self.addLink(s8, s9)
        self.addLink(s9, s10)


topos = {"HiberniaCanada": (lambda: HiberniaCanada())}

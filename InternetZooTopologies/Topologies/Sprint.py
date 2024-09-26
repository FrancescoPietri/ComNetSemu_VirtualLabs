#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Sprint(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("00", dpid="0000000000000002")
        s1 = self.addSwitch("11", dpid="0000000000000003")
        s2 = self.addSwitch("22", dpid="0000000000000004")
        s3 = self.addSwitch("33", dpid="0000000000000005")
        s4 = self.addSwitch("44", dpid="0000000000000006")
        s5 = self.addSwitch("55", dpid="0000000000000007")
        s6 = self.addSwitch("66", dpid="0000000000000008")
        s7 = self.addSwitch("77", dpid="0000000000000009")
        s8 = self.addSwitch("88", dpid="000000000000000a")
        s9 = self.addSwitch("99", dpid="000000000000000b")
        s10 = self.addSwitch("1010", dpid="000000000000000c")

        # Adding Links
        self.addLink(s0, s2)
        self.addLink(s0, s4)
        self.addLink(s0, s7)
        self.addLink(s1, s10)
        self.addLink(s1, s6)
        self.addLink(s3, s8)
        self.addLink(s3, s4)
        self.addLink(s4, s5)
        self.addLink(s4, s8)
        self.addLink(s4, s9)
        self.addLink(s4, s10)
        self.addLink(s5, s6)
        self.addLink(s6, s10)
        self.addLink(s6, s7)
        self.addLink(s7, s8)
        self.addLink(s7, s10)
        self.addLink(s8, s9)
        self.addLink(s9, s10)


topos = {"Sprint": (lambda: Sprint())}

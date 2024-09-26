#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Netrail(Topo):
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

        # Adding Links
        self.addLink(s0, s4)
        self.addLink(s0, s6)
        self.addLink(s1, s2)
        self.addLink(s1, s6)
        self.addLink(s2, s3)
        self.addLink(s2, s4)
        self.addLink(s3, s4)
        self.addLink(s4, s5)
        self.addLink(s4, s6)
        self.addLink(s5, s6)


topos = {"Netrail": (lambda: Netrail())}

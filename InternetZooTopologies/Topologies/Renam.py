#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Renam(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("chisinau0", dpid="0000000000000002")
        s1 = self.addSwitch("balti1", dpid="0000000000000003")
        s2 = self.addSwitch("cahul22", dpid="0000000000000004")
        s3 = self.addSwitch("starneti3", dpid="0000000000000005")
        s4 = self.addSwitch("roedunet4", dpid="0000000000000006")

        # Adding Links
        self.addLink(s0, s1)
        self.addLink(s0, s2)
        self.addLink(s0, s3)
        self.addLink(s0, s4)


topos = {"Renam": (lambda: Renam())}

#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Mren(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("bijelopo0", dpid="0000000000000002")
        s1 = self.addSwitch("niksic1", dpid="0000000000000003")
        s2 = self.addSwitch("podgoric2", dpid="0000000000000004")
        s3 = self.addSwitch("njegusi3", dpid="0000000000000005")
        s4 = self.addSwitch("kotor4", dpid="0000000000000006")
        s5 = self.addSwitch("hercegno5", dpid="0000000000000007")

        # Adding Links
        self.addLink(s0, s2)
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s2, s4)
        self.addLink(s2, s5)


topos = {"Mren": (lambda: Mren())}

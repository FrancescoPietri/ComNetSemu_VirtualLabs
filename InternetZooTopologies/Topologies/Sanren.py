#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Sanren(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("johannes0", dpid="0000000000000002")
        s1 = self.addSwitch("pretoria1", dpid="0000000000000003")
        s2 = self.addSwitch("durban2", dpid="0000000000000004")
        s3 = self.addSwitch("bloemfon3", dpid="0000000000000005")
        s4 = self.addSwitch("eastlond4", dpid="0000000000000006")
        s5 = self.addSwitch("porteliz5", dpid="0000000000000007")
        s6 = self.addSwitch("capetown6", dpid="0000000000000008")

        # Adding Links
        self.addLink(s0, s1)
        self.addLink(s0, s3)
        self.addLink(s1, s2)
        self.addLink(s2, s4)
        self.addLink(s3, s6)
        self.addLink(s4, s5)
        self.addLink(s5, s6)


topos = {"Sanren": (lambda: Sanren())}

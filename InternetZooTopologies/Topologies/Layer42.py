#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Layer42(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("seattle0", dpid="0000000000000002")
        s1 = self.addSwitch("sanfranc1", dpid="0000000000000003")
        s2 = self.addSwitch("losangel2", dpid="0000000000000004")
        s3 = self.addSwitch("chicago3", dpid="0000000000000005")
        s4 = self.addSwitch("newyorkc4", dpid="0000000000000006")
        s5 = self.addSwitch("washingt5", dpid="0000000000000007")

        # Adding Links
        self.addLink(s0, s1)
        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s1, s5)
        self.addLink(s3, s4)
        self.addLink(s3, s5)
        self.addLink(s4, s5)


topos = {"Layer42": (lambda: Layer42())}

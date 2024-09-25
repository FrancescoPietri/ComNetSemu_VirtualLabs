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
        seattle = self.addSwitch("seattle", dpid="0000000000000002")
        sanfranc = self.addSwitch("sanfranc", dpid="0000000000000003")
        losangel = self.addSwitch("losangel", dpid="0000000000000004")
        chicago = self.addSwitch("chicago", dpid="0000000000000005")
        newyorkc = self.addSwitch("newyorkc", dpid="0000000000000006")
        washingt = self.addSwitch("washingt", dpid="0000000000000007")

        # Adding Links
        self.addLink(seattle, sanfranc)
        self.addLink(sanfranc, losangel)
        self.addLink(sanfranc, chicago)
        self.addLink(sanfranc, washingt)
        self.addLink(chicago, newyorkc)
        self.addLink(chicago, washingt)
        self.addLink(newyorkc, washingt)


topos = {"Layer42": (lambda: Layer42())}

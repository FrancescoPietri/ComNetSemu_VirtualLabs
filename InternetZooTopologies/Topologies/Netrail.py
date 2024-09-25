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
        paloalto = self.addSwitch("paloalto", dpid="0000000000000002")
        chicago = self.addSwitch("chicago", dpid="0000000000000003")
        newyork = self.addSwitch("newyork", dpid="0000000000000004")
        baltimor = self.addSwitch("baltimor", dpid="0000000000000005")
        washingt = self.addSwitch("washingt", dpid="0000000000000006")
        miami = self.addSwitch("miami", dpid="0000000000000007")
        atlanta = self.addSwitch("atlanta", dpid="0000000000000008")

        # Adding Links
        self.addLink(paloalto, washingt)
        self.addLink(paloalto, atlanta)
        self.addLink(chicago, newyork)
        self.addLink(chicago, atlanta)
        self.addLink(newyork, baltimor)
        self.addLink(newyork, washingt)
        self.addLink(baltimor, washingt)
        self.addLink(washingt, miami)
        self.addLink(washingt, atlanta)
        self.addLink(miami, atlanta)


topos = {"Netrail": (lambda: Netrail())}

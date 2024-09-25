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
        cheyenne = self.addSwitch("cheyenne", dpid="0000000000000002")
        atlanta = self.addSwitch("atlanta", dpid="0000000000000003")
        boulder = self.addSwitch("boulder", dpid="0000000000000004")
        seattle = self.addSwitch("seattle", dpid="0000000000000005")
        stockton = self.addSwitch("stockton", dpid="0000000000000006")
        anaheim = self.addSwitch("anaheim", dpid="0000000000000007")
        fortwort = self.addSwitch("fortwort", dpid="0000000000000008")
        kansasci = self.addSwitch("kansasci", dpid="0000000000000009")
        chicago = self.addSwitch("chicago", dpid="000000000000000a")
        newyork = self.addSwitch("newyork", dpid="000000000000000b")
        washingt = self.addSwitch("washingt", dpid="000000000000000c")

        # Adding Links
        self.addLink(cheyenne, boulder)
        self.addLink(cheyenne, stockton)
        self.addLink(cheyenne, kansasci)
        self.addLink(atlanta, washingt)
        self.addLink(atlanta, fortwort)
        self.addLink(seattle, chicago)
        self.addLink(seattle, stockton)
        self.addLink(stockton, anaheim)
        self.addLink(stockton, chicago)
        self.addLink(stockton, newyork)
        self.addLink(stockton, washingt)
        self.addLink(anaheim, fortwort)
        self.addLink(fortwort, washingt)
        self.addLink(fortwort, kansasci)
        self.addLink(kansasci, chicago)
        self.addLink(kansasci, washingt)
        self.addLink(chicago, newyork)
        self.addLink(newyork, washingt)


topos = {"Sprint": (lambda: Sprint())}

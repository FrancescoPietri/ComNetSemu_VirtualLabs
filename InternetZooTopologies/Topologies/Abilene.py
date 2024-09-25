#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Abilene(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        newyork = self.addSwitch("newyork", dpid="0000000000000002")
        chicago = self.addSwitch("chicago", dpid="0000000000000003")
        washingt = self.addSwitch("washingt", dpid="0000000000000004")
        seattle = self.addSwitch("seattle", dpid="0000000000000005")
        sunnyval = self.addSwitch("sunnyval", dpid="0000000000000006")
        losangel = self.addSwitch("losangel", dpid="0000000000000007")
        denver = self.addSwitch("denver", dpid="0000000000000008")
        kansasci = self.addSwitch("kansasci", dpid="0000000000000009")
        houston = self.addSwitch("houston", dpid="000000000000000a")
        atlanta = self.addSwitch("atlanta", dpid="000000000000000b")
        indianap = self.addSwitch("indianap", dpid="000000000000000c")

        # Adding Links
        self.addLink(newyork, chicago)
        self.addLink(newyork, washingt)
        self.addLink(chicago, indianap)
        self.addLink(washingt, atlanta)
        self.addLink(seattle, sunnyval)
        self.addLink(seattle, denver)
        self.addLink(sunnyval, losangel)
        self.addLink(sunnyval, denver)
        self.addLink(losangel, houston)
        self.addLink(denver, kansasci)
        self.addLink(kansasci, houston)
        self.addLink(kansasci, indianap)
        self.addLink(houston, atlanta)
        self.addLink(atlanta, indianap)


topos = {"Abilene": (lambda: Abilene())}

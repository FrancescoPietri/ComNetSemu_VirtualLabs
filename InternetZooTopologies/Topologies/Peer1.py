#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Peer1(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        herndon = self.addSwitch("herndon", dpid="0000000000000002")
        miami = self.addSwitch("miami", dpid="0000000000000003")
        montreal = self.addSwitch("montreal", dpid="0000000000000004")
        newyork = self.addSwitch("newyork", dpid="0000000000000005")
        london = self.addSwitch("london", dpid="0000000000000006")
        amsterda = self.addSwitch("amsterda", dpid="0000000000000007")
        chicago = self.addSwitch("chicago", dpid="0000000000000008")
        toronto = self.addSwitch("toronto", dpid="0000000000000009")
        vancouve = self.addSwitch("vancouve", dpid="000000000000000a")
        seattle = self.addSwitch("seattle", dpid="000000000000000b")
        fremont = self.addSwitch("fremont", dpid="000000000000000c")
        sanjose = self.addSwitch("sanjose", dpid="000000000000000d")
        losangel = self.addSwitch("losangel", dpid="000000000000000e")
        dallas = self.addSwitch("dallas", dpid="000000000000000f")
        sananton = self.addSwitch("sananton", dpid="0000000000000010")
        atlanta = self.addSwitch("atlanta", dpid="0000000000000011")

        # Adding Links
        self.addLink(herndon, newyork)
        self.addLink(herndon, atlanta)
        self.addLink(miami, atlanta)
        self.addLink(montreal, newyork)
        self.addLink(montreal, toronto)
        self.addLink(newyork, london)
        self.addLink(newyork, chicago)
        self.addLink(newyork, toronto)
        self.addLink(london, amsterda)
        self.addLink(chicago, seattle)
        self.addLink(chicago, dallas)
        self.addLink(chicago, toronto)
        self.addLink(toronto, vancouve)
        self.addLink(vancouve, seattle)
        self.addLink(seattle, fremont)
        self.addLink(fremont, sanjose)
        self.addLink(sanjose, losangel)
        self.addLink(losangel, dallas)
        self.addLink(dallas, sananton)
        self.addLink(dallas, atlanta)


topos = {"Peer1": (lambda: Peer1())}

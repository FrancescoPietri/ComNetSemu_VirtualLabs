#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Ans(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        hartford = self.addSwitch("hartford", dpid="0000000000000002")
        newyork = self.addSwitch("newyork", dpid="0000000000000003")
        chicago = self.addSwitch("chicago", dpid="0000000000000004")
        clevelan = self.addSwitch("clevelan", dpid="0000000000000005")
        greensbo = self.addSwitch("greensbo", dpid="0000000000000006")
        atlanta = self.addSwitch("atlanta", dpid="0000000000000007")
        washingt = self.addSwitch("washingt", dpid="0000000000000008")
        reston = self.addSwitch("reston", dpid="0000000000000009")
        dallas = self.addSwitch("dallas", dpid="000000000000000a")
        stlouis = self.addSwitch("stlouis", dpid="000000000000000b")
        seattle = self.addSwitch("seattle", dpid="000000000000000c")
        denver = self.addSwitch("denver", dpid="000000000000000d")
        sanfranc = self.addSwitch("sanfranc", dpid="000000000000000e")
        sanjose = self.addSwitch("sanjose", dpid="000000000000000f")
        losangel = self.addSwitch("losangel", dpid="0000000000000010")
        albuquer = self.addSwitch("albuquer", dpid="0000000000000011")
        hawaii = self.addSwitch("hawaii", dpid="0000000000000012")
        houston = self.addSwitch("houston", dpid="0000000000000013")

        # Adding Links
        self.addLink(hartford, newyork)
        self.addLink(hartford, clevelan)
        self.addLink(newyork, clevelan)
        self.addLink(newyork, washingt)
        self.addLink(newyork, reston)
        self.addLink(chicago, clevelan)
        self.addLink(chicago, stlouis)
        self.addLink(chicago, denver)
        self.addLink(greensbo, atlanta)
        self.addLink(greensbo, washingt)
        self.addLink(atlanta, houston)
        self.addLink(washingt, reston)
        self.addLink(reston, dallas)
        self.addLink(reston, stlouis)
        self.addLink(dallas, stlouis)
        self.addLink(dallas, sanjose)
        self.addLink(dallas, houston)
        self.addLink(seattle, denver)
        self.addLink(seattle, sanfranc)
        self.addLink(denver, sanfranc)
        self.addLink(sanfranc, sanjose)
        self.addLink(sanfranc, losangel)
        self.addLink(losangel, albuquer)
        self.addLink(albuquer, hawaii)
        self.addLink(albuquer, houston)


topos = {"Ans": (lambda: Ans())}

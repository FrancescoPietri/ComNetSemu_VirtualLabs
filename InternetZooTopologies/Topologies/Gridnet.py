#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Gridnet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        houston = self.addSwitch("houston", dpid="0000000000000002")
        sanfranc = self.addSwitch("sanfranc", dpid="0000000000000003")
        losangel = self.addSwitch("losangel", dpid="0000000000000004")
        newyork = self.addSwitch("newyork", dpid="0000000000000005")
        newark = self.addSwitch("newark", dpid="0000000000000006")
        washingt = self.addSwitch("washingt", dpid="0000000000000007")
        atlanta = self.addSwitch("atlanta", dpid="0000000000000008")
        dallas = self.addSwitch("dallas", dpid="0000000000000009")
        miami = self.addSwitch("miami", dpid="000000000000000a")

        # Adding Links
        self.addLink(houston, miami)
        self.addLink(houston, losangel)
        self.addLink(houston, newyork)
        self.addLink(houston, dallas)
        self.addLink(sanfranc, losangel)
        self.addLink(sanfranc, newark)
        self.addLink(sanfranc, washingt)
        self.addLink(sanfranc, atlanta)
        self.addLink(sanfranc, dallas)
        self.addLink(losangel, newyork)
        self.addLink(losangel, miami)
        self.addLink(newyork, miami)
        self.addLink(newyork, newark)
        self.addLink(newark, washingt)
        self.addLink(newark, atlanta)
        self.addLink(newark, dallas)
        self.addLink(washingt, atlanta)
        self.addLink(washingt, dallas)
        self.addLink(atlanta, miami)
        self.addLink(atlanta, dallas)


topos = {"Gridnet": (lambda: Gridnet())}

#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Dataxchange(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        sanfranc = self.addSwitch("sanfranc", dpid="0000000000000002")
        losangel = self.addSwitch("losangel", dpid="0000000000000003")
        chicago = self.addSwitch("chicago", dpid="0000000000000004")
        mclean = self.addSwitch("mclean", dpid="0000000000000005")
        washingt = self.addSwitch("washingt", dpid="0000000000000006")
        atlanta = self.addSwitch("atlanta", dpid="0000000000000007")

        # Adding Links
        self.addLink(sanfranc, losangel)
        self.addLink(sanfranc, chicago)
        self.addLink(sanfranc, washingt)
        self.addLink(sanfranc, atlanta)
        self.addLink(losangel, chicago)
        self.addLink(losangel, washingt)
        self.addLink(losangel, atlanta)
        self.addLink(chicago, washingt)
        self.addLink(chicago, atlanta)
        self.addLink(mclean, washingt)
        self.addLink(washingt, atlanta)


topos = {"Dataxchange": (lambda: Dataxchange())}

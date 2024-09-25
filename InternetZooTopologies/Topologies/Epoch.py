#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Epoch(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        paloalto = self.addSwitch("paloalto", dpid="0000000000000002")
        losangel = self.addSwitch("losangel", dpid="0000000000000003")
        denver = self.addSwitch("denver", dpid="0000000000000004")
        chicago = self.addSwitch("chicago", dpid="0000000000000005")
        vienna = self.addSwitch("vienna", dpid="0000000000000006")
        atlanta = self.addSwitch("atlanta", dpid="0000000000000007")

        # Adding Links
        self.addLink(paloalto, losangel)
        self.addLink(paloalto, denver)
        self.addLink(paloalto, vienna)
        self.addLink(losangel, atlanta)
        self.addLink(denver, chicago)
        self.addLink(chicago, vienna)
        self.addLink(vienna, atlanta)


topos = {"Epoch": (lambda: Epoch())}

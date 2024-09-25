#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Globalcenter(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        minneapo = self.addSwitch("minneapo", dpid="0000000000000002")
        seattle = self.addSwitch("seattle", dpid="0000000000000003")
        sanjose = self.addSwitch("sanjose", dpid="0000000000000004")
        phoenix = self.addSwitch("phoenix", dpid="0000000000000005")
        dallas = self.addSwitch("dallas", dpid="0000000000000006")
        atlanta = self.addSwitch("atlanta", dpid="0000000000000007")
        vienna = self.addSwitch("vienna", dpid="0000000000000008")
        whippany = self.addSwitch("whippany", dpid="0000000000000009")
        chicago = self.addSwitch("chicago", dpid="000000000000000a")

        # Adding Links
        self.addLink(minneapo, seattle)
        self.addLink(minneapo, sanjose)
        self.addLink(minneapo, phoenix)
        self.addLink(minneapo, dallas)
        self.addLink(minneapo, atlanta)
        self.addLink(minneapo, vienna)
        self.addLink(minneapo, whippany)
        self.addLink(minneapo, chicago)
        self.addLink(seattle, sanjose)
        self.addLink(seattle, phoenix)
        self.addLink(seattle, dallas)
        self.addLink(seattle, atlanta)
        self.addLink(seattle, vienna)
        self.addLink(seattle, whippany)
        self.addLink(seattle, chicago)
        self.addLink(sanjose, phoenix)
        self.addLink(sanjose, dallas)
        self.addLink(sanjose, atlanta)
        self.addLink(sanjose, vienna)
        self.addLink(sanjose, whippany)
        self.addLink(sanjose, chicago)
        self.addLink(phoenix, dallas)
        self.addLink(phoenix, atlanta)
        self.addLink(phoenix, vienna)
        self.addLink(phoenix, whippany)
        self.addLink(phoenix, chicago)
        self.addLink(dallas, atlanta)
        self.addLink(dallas, vienna)
        self.addLink(dallas, whippany)
        self.addLink(dallas, chicago)
        self.addLink(atlanta, vienna)
        self.addLink(atlanta, whippany)
        self.addLink(atlanta, chicago)
        self.addLink(vienna, whippany)
        self.addLink(vienna, chicago)
        self.addLink(whippany, chicago)


topos = {"Globalcenter": (lambda: Globalcenter())}

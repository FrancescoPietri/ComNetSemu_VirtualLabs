#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Napnet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        seattle = self.addSwitch("seattle", dpid="0000000000000002")
        sanjose = self.addSwitch("sanjose", dpid="0000000000000003")
        minneapo = self.addSwitch("minneapo", dpid="0000000000000004")
        chicago = self.addSwitch("chicago", dpid="0000000000000005")
        vienna = self.addSwitch("vienna", dpid="0000000000000006")
        dallas = self.addSwitch("dallas", dpid="0000000000000007")

        # Adding Links
        self.addLink(seattle, sanjose)
        self.addLink(seattle, chicago)
        self.addLink(sanjose, chicago)
        self.addLink(sanjose, vienna)
        self.addLink(minneapo, chicago)
        self.addLink(chicago, vienna)
        self.addLink(chicago, dallas)


topos = {"Napnet": (lambda: Napnet())}

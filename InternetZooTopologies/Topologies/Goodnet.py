#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Goodnet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        tampa = self.addSwitch("tampa", dpid="0000000000000002")
        oklahoma = self.addSwitch("oklahoma", dpid="0000000000000003")
        neworlea = self.addSwitch("neworlea", dpid="0000000000000004")
        jacksonv = self.addSwitch("jacksonv", dpid="0000000000000005")
        losangel = self.addSwitch("losangel", dpid="0000000000000006")
        phoenix = self.addSwitch("phoenix", dpid="0000000000000007")
        tucson = self.addSwitch("tucson", dpid="0000000000000008")
        atlanta = self.addSwitch("atlanta", dpid="0000000000000009")
        birmingh = self.addSwitch("birmingh", dpid="000000000000000a")
        sanjose = self.addSwitch("sanjose", dpid="000000000000000b")
        saltlake = self.addSwitch("saltlake", dpid="000000000000000c")
        denver = self.addSwitch("denver", dpid="000000000000000d")
        chicago = self.addSwitch("chicago", dpid="000000000000000e")
        hartford = self.addSwitch("hartford", dpid="000000000000000f")
        newyork = self.addSwitch("newyork", dpid="0000000000000010")
        washingt = self.addSwitch("washingt", dpid="0000000000000011")
        chattano = self.addSwitch("chattano", dpid="0000000000000012")

        # Adding Links
        self.addLink(tampa, jacksonv)
        self.addLink(tampa, atlanta)
        self.addLink(oklahoma, sanjose)
        self.addLink(oklahoma, washingt)
        self.addLink(neworlea, chicago)
        self.addLink(neworlea, phoenix)
        self.addLink(neworlea, atlanta)
        self.addLink(jacksonv, sanjose)
        self.addLink(jacksonv, washingt)
        self.addLink(losangel, sanjose)
        self.addLink(losangel, chicago)
        self.addLink(losangel, washingt)
        self.addLink(phoenix, sanjose)
        self.addLink(phoenix, chicago)
        self.addLink(phoenix, tucson)
        self.addLink(phoenix, washingt)
        self.addLink(atlanta, birmingh)
        self.addLink(atlanta, chicago)
        self.addLink(atlanta, washingt)
        self.addLink(sanjose, saltlake)
        self.addLink(sanjose, denver)
        self.addLink(sanjose, chicago)
        self.addLink(sanjose, newyork)
        self.addLink(sanjose, washingt)
        self.addLink(saltlake, chicago)
        self.addLink(denver, chicago)
        self.addLink(chicago, newyork)
        self.addLink(chicago, washingt)
        self.addLink(hartford, newyork)
        self.addLink(newyork, washingt)
        self.addLink(washingt, chattano)


topos = {"Goodnet": (lambda: Goodnet())}

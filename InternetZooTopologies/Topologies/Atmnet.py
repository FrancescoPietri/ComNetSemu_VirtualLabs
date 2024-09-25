#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Atmnet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        saltlake = self.addSwitch("saltlake", dpid="0000000000000002")
        minneapo = self.addSwitch("minneapo", dpid="0000000000000003")
        kansasci = self.addSwitch("kansasci", dpid="0000000000000004")
        denver = self.addSwitch("denver", dpid="0000000000000005")
        pittsbur = self.addSwitch("pittsbur", dpid="0000000000000006")
        philadel = self.addSwitch("philadel", dpid="0000000000000007")
        chicago = self.addSwitch("chicago", dpid="0000000000000008")
        detroit = self.addSwitch("detroit", dpid="0000000000000009")
        newyork = self.addSwitch("newyork", dpid="000000000000000a")
        washingt = self.addSwitch("washingt", dpid="000000000000000b")
        losangel = self.addSwitch("losangel", dpid="000000000000000c")
        houston = self.addSwitch("houston", dpid="000000000000000d")
        stlouis = self.addSwitch("stlouis", dpid="000000000000000e")
        seattle = self.addSwitch("seattle", dpid="000000000000000f")
        oakland = self.addSwitch("oakland", dpid="0000000000000010")
        santacla = self.addSwitch("santacla", dpid="0000000000000011")
        atlanta = self.addSwitch("atlanta", dpid="0000000000000012")
        sandiego = self.addSwitch("sandiego", dpid="0000000000000013")
        phoenix = self.addSwitch("phoenix", dpid="0000000000000014")
        tucson = self.addSwitch("tucson", dpid="0000000000000015")
        dallas = self.addSwitch("dallas", dpid="0000000000000016")

        # Adding Links
        self.addLink(saltlake, denver)
        self.addLink(saltlake, oakland)
        self.addLink(minneapo, chicago)
        self.addLink(kansasci, denver)
        self.addLink(kansasci, stlouis)
        self.addLink(pittsbur, philadel)
        self.addLink(pittsbur, detroit)
        self.addLink(philadel, newyork)
        self.addLink(chicago, stlouis)
        self.addLink(chicago, detroit)
        self.addLink(newyork, washingt)
        self.addLink(washingt, atlanta)
        self.addLink(losangel, sandiego)
        self.addLink(losangel, santacla)
        self.addLink(houston, atlanta)
        self.addLink(houston, stlouis)
        self.addLink(houston, dallas)
        self.addLink(seattle, oakland)
        self.addLink(oakland, santacla)
        self.addLink(sandiego, phoenix)
        self.addLink(phoenix, tucson)
        self.addLink(tucson, dallas)


topos = {"Atmnet": (lambda: Atmnet())}

#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Savvis(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        newyork = self.addSwitch("newyork", dpid="0000000000000002")
        philadel = self.addSwitch("philadel", dpid="0000000000000003")
        detroit = self.addSwitch("detroit", dpid="0000000000000004")
        pittsbur = self.addSwitch("pittsbur", dpid="0000000000000005")
        houston = self.addSwitch("houston", dpid="0000000000000006")
        austin = self.addSwitch("austin", dpid="0000000000000007")
        washingt = self.addSwitch("washingt", dpid="0000000000000008")
        atlanta = self.addSwitch("atlanta", dpid="0000000000000009")
        dallas = self.addSwitch("dallas", dpid="000000000000000a")
        champaig = self.addSwitch("champaig", dpid="000000000000000b")
        chicago = self.addSwitch("chicago", dpid="000000000000000c")
        sanfranc = self.addSwitch("sanfranc", dpid="000000000000000d")
        losangel = self.addSwitch("losangel", dpid="000000000000000e")
        sandiego = self.addSwitch("sandiego", dpid="000000000000000f")
        phoenix = self.addSwitch("phoenix", dpid="0000000000000010")
        saltlake = self.addSwitch("saltlake", dpid="0000000000000011")
        denver = self.addSwitch("denver", dpid="0000000000000012")
        kansasci = self.addSwitch("kansasci", dpid="0000000000000013")
        stlouis = self.addSwitch("stlouis", dpid="0000000000000014")

        # Adding Links
        self.addLink(newyork, philadel)
        self.addLink(newyork, pittsbur)
        self.addLink(philadel, washingt)
        self.addLink(detroit, chicago)
        self.addLink(detroit, pittsbur)
        self.addLink(houston, austin)
        self.addLink(houston, atlanta)
        self.addLink(austin, dallas)
        self.addLink(washingt, atlanta)
        self.addLink(dallas, stlouis)
        self.addLink(dallas, phoenix)
        self.addLink(champaig, stlouis)
        self.addLink(chicago, stlouis)
        self.addLink(sanfranc, losangel)
        self.addLink(sanfranc, saltlake)
        self.addLink(losangel, sandiego)
        self.addLink(losangel, phoenix)
        self.addLink(saltlake, denver)
        self.addLink(denver, kansasci)
        self.addLink(kansasci, stlouis)


topos = {"Savvis": (lambda: Savvis())}

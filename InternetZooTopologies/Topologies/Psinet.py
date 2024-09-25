#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Psinet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        detroit = self.addSwitch("detroit", dpid="0000000000000002")
        dublin = self.addSwitch("dublin", dpid="0000000000000003")
        chicago = self.addSwitch("chicago", dpid="0000000000000004")
        toledo = self.addSwitch("toledo", dpid="0000000000000005")
        washingt = self.addSwitch("washingt", dpid="0000000000000006")
        baltimor = self.addSwitch("baltimor", dpid="0000000000000007")
        herndon = self.addSwitch("herndon", dpid="0000000000000008")
        atlanta = self.addSwitch("atlanta", dpid="0000000000000009")
        wilmingt = self.addSwitch("wilmingt", dpid="000000000000000a")
        philadel = self.addSwitch("philadel", dpid="000000000000000b")
        boston = self.addSwitch("boston", dpid="000000000000000c")
        troy = self.addSwitch("troy", dpid="000000000000000d")
        newyork = self.addSwitch("newyork", dpid="000000000000000e")
        newark = self.addSwitch("newark", dpid="000000000000000f")
        kansasci = self.addSwitch("kansasci", dpid="0000000000000010")
        stlouis = self.addSwitch("stlouis", dpid="0000000000000011")
        sanfranc = self.addSwitch("sanfranc", dpid="0000000000000012")
        santacla = self.addSwitch("santacla", dpid="0000000000000013")
        losangel = self.addSwitch("losangel", dpid="0000000000000014")
        phoenix = self.addSwitch("phoenix", dpid="0000000000000015")
        austin = self.addSwitch("austin", dpid="0000000000000016")
        fortwort = self.addSwitch("fortwort", dpid="0000000000000017")
        dallas = self.addSwitch("dallas", dpid="0000000000000018")
        houston = self.addSwitch("houston", dpid="0000000000000019")

        # Adding Links
        self.addLink(detroit, toledo)
        self.addLink(dublin, chicago)
        self.addLink(dublin, toledo)
        self.addLink(dublin, washingt)
        self.addLink(chicago, toledo)
        self.addLink(chicago, stlouis)
        self.addLink(washingt, baltimor)
        self.addLink(baltimor, wilmingt)
        self.addLink(herndon, newyork)
        self.addLink(herndon, atlanta)
        self.addLink(atlanta, houston)
        self.addLink(wilmingt, philadel)
        self.addLink(philadel, newark)
        self.addLink(boston, newyork)
        self.addLink(troy, newyork)
        self.addLink(newyork, newark)
        self.addLink(kansasci, phoenix)
        self.addLink(kansasci, dallas)
        self.addLink(kansasci, stlouis)
        self.addLink(sanfranc, santacla)
        self.addLink(sanfranc, losangel)
        self.addLink(losangel, phoenix)
        self.addLink(austin, houston)
        self.addLink(fortwort, dallas)
        self.addLink(dallas, houston)


topos = {"Psinet": (lambda: Psinet())}

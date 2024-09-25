#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Darkstrand(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        tulsa = self.addSwitch("tulsa", dpid="0000000000000002")
        kansasci = self.addSwitch("kansasci", dpid="0000000000000003")
        sananton = self.addSwitch("sananton", dpid="0000000000000004")
        dallas = self.addSwitch("dallas", dpid="0000000000000005")
        pensacol = self.addSwitch("pensacol", dpid="0000000000000006")
        jacksonv = self.addSwitch("jacksonv", dpid="0000000000000007")
        houston = self.addSwitch("houston", dpid="0000000000000008")
        batonrou = self.addSwitch("batonrou", dpid="0000000000000009")
        atlanta = self.addSwitch("atlanta", dpid="000000000000000a")
        raleigh = self.addSwitch("raleigh", dpid="000000000000000b")
        newyork = self.addSwitch("newyork", dpid="000000000000000c")
        syracuse = self.addSwitch("syracuse", dpid="000000000000000d")
        clevelan = self.addSwitch("clevelan", dpid="000000000000000e")
        chicago = self.addSwitch("chicago", dpid="000000000000000f")
        raton = self.addSwitch("raton", dpid="0000000000000010")
        pittsbur = self.addSwitch("pittsbur", dpid="0000000000000011")
        washingt = self.addSwitch("washingt", dpid="0000000000000012")
        philadel = self.addSwitch("philadel", dpid="0000000000000013")
        losangel = self.addSwitch("losangel", dpid="0000000000000014")
        elpasol = self.addSwitch("elpasol", dpid="0000000000000015")
        seattle = self.addSwitch("seattle", dpid="0000000000000016")
        portland = self.addSwitch("portland", dpid="0000000000000017")
        sunnyval = self.addSwitch("sunnyval", dpid="0000000000000018")
        boise = self.addSwitch("boise", dpid="0000000000000019")
        saltlake = self.addSwitch("saltlake", dpid="000000000000001a")
        denver = self.addSwitch("denver", dpid="000000000000001b")
        albuquer = self.addSwitch("albuquer", dpid="000000000000001c")
        phoenix = self.addSwitch("phoenix", dpid="000000000000001d")

        # Adding Links
        self.addLink(tulsa, kansasci)
        self.addLink(tulsa, dallas)
        self.addLink(kansasci, denver)
        self.addLink(kansasci, chicago)
        self.addLink(sananton, elpasol)
        self.addLink(sananton, houston)
        self.addLink(dallas, houston)
        self.addLink(pensacol, jacksonv)
        self.addLink(pensacol, batonrou)
        self.addLink(jacksonv, atlanta)
        self.addLink(houston, batonrou)
        self.addLink(atlanta, raleigh)
        self.addLink(raleigh, washingt)
        self.addLink(newyork, philadel)
        self.addLink(newyork, syracuse)
        self.addLink(syracuse, clevelan)
        self.addLink(clevelan, chicago)
        self.addLink(clevelan, pittsbur)
        self.addLink(raton, denver)
        self.addLink(raton, albuquer)
        self.addLink(pittsbur, washingt)
        self.addLink(washingt, philadel)
        self.addLink(losangel, phoenix)
        self.addLink(losangel, sunnyval)
        self.addLink(elpasol, phoenix)
        self.addLink(elpasol, albuquer)
        self.addLink(seattle, portland)
        self.addLink(seattle, boise)
        self.addLink(portland, sunnyval)
        self.addLink(boise, saltlake)
        self.addLink(saltlake, denver)


topos = {"Darkstrand": (lambda: Darkstrand())}

#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Bbnplanet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        jackson = self.addSwitch("jackson", dpid="0000000000000002")
        atlanta = self.addSwitch("atlanta", dpid="0000000000000003")
        austin = self.addSwitch("austin", dpid="0000000000000004")
        houston = self.addSwitch("houston", dpid="0000000000000005")
        detroit = self.addSwitch("detroit", dpid="0000000000000006")
        columbus = self.addSwitch("columbus", dpid="0000000000000007")
        cincinna = self.addSwitch("cincinna", dpid="0000000000000008")
        clevelan = self.addSwitch("clevelan", dpid="0000000000000009")
        chicago = self.addSwitch("chicago", dpid="000000000000000a")
        minneapo = self.addSwitch("minneapo", dpid="000000000000000b")
        philadel = self.addSwitch("philadel", dpid="000000000000000c")
        newyork = self.addSwitch("newyork", dpid="000000000000000d")
        cambridg = self.addSwitch("cambridg", dpid="000000000000000e")
        boston = self.addSwitch("boston", dpid="000000000000000f")
        richmond = self.addSwitch("richmond", dpid="0000000000000010")
        washingt = self.addSwitch("washingt", dpid="0000000000000011")
        baltimor = self.addSwitch("baltimor", dpid="0000000000000012")
        denver = self.addSwitch("denver", dpid="0000000000000013")
        dallas = self.addSwitch("dallas", dpid="0000000000000014")
        sacramen = self.addSwitch("sacramen", dpid="0000000000000015")
        oakland = self.addSwitch("oakland", dpid="0000000000000016")
        sanfranc = self.addSwitch("sanfranc", dpid="0000000000000017")
        paloalto = self.addSwitch("paloalto", dpid="0000000000000018")
        sanjose = self.addSwitch("sanjose", dpid="0000000000000019")
        losangel = self.addSwitch("losangel", dpid="000000000000001a")
        sandiego = self.addSwitch("sandiego", dpid="000000000000001b")
        orange = self.addSwitch("orange", dpid="000000000000001c")

        # Adding Links
        self.addLink(jackson, atlanta)
        self.addLink(atlanta, dallas)
        self.addLink(atlanta, washingt)
        self.addLink(austin, dallas)
        self.addLink(houston, dallas)
        self.addLink(detroit, clevelan)
        self.addLink(columbus, clevelan)
        self.addLink(cincinna, clevelan)
        self.addLink(clevelan, chicago)
        self.addLink(clevelan, newyork)
        self.addLink(chicago, denver)
        self.addLink(chicago, boston)
        self.addLink(chicago, minneapo)
        self.addLink(philadel, newyork)
        self.addLink(newyork, cambridg)
        self.addLink(newyork, washingt)
        self.addLink(richmond, washingt)
        self.addLink(washingt, baltimor)
        self.addLink(washingt, sanjose)
        self.addLink(denver, oakland)
        self.addLink(dallas, losangel)
        self.addLink(sacramen, oakland)
        self.addLink(oakland, sanfranc)
        self.addLink(oakland, sanjose)
        self.addLink(paloalto, sanjose)
        self.addLink(sanjose, losangel)
        self.addLink(losangel, sandiego)
        self.addLink(losangel, orange)


topos = {"Bbnplanet": (lambda: Bbnplanet())}

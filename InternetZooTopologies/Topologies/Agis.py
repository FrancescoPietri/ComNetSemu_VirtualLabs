#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Agis(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        miami = self.addSwitch("miami", dpid="0000000000000002")
        houston = self.addSwitch("houston", dpid="0000000000000003")
        washingt = self.addSwitch("washingt", dpid="0000000000000004")
        atlanta = self.addSwitch("atlanta", dpid="0000000000000005")
        mexicoci = self.addSwitch("mexicoci", dpid="0000000000000006")
        phoenix = self.addSwitch("phoenix", dpid="0000000000000007")
        dallas = self.addSwitch("dallas", dpid="0000000000000008")
        stlouis = self.addSwitch("stlouis", dpid="0000000000000009")
        sandiego = self.addSwitch("sandiego", dpid="000000000000000a")
        losangel = self.addSwitch("losangel", dpid="000000000000000b")
        santacla = self.addSwitch("santacla", dpid="000000000000000c")
        stockton = self.addSwitch("stockton", dpid="000000000000000d")
        sacramen = self.addSwitch("sacramen", dpid="000000000000000e")
        fresno = self.addSwitch("fresno", dpid="000000000000000f")
        sanfranc = self.addSwitch("sanfranc", dpid="0000000000000010")
        newyork = self.addSwitch("newyork", dpid="0000000000000011")
        boston = self.addSwitch("boston", dpid="0000000000000012")
        seattle = self.addSwitch("seattle", dpid="0000000000000013")
        saltlake = self.addSwitch("saltlake", dpid="0000000000000014")
        chicago = self.addSwitch("chicago", dpid="0000000000000015")
        minneapo = self.addSwitch("minneapo", dpid="0000000000000016")
        detroit = self.addSwitch("detroit", dpid="0000000000000017")
        pittsbur = self.addSwitch("pittsbur", dpid="0000000000000018")
        philadel = self.addSwitch("philadel", dpid="0000000000000019")
        pennsauk = self.addSwitch("pennsauk", dpid="000000000000001a")

        # Adding Links
        self.addLink(miami, atlanta)
        self.addLink(houston, dallas)
        self.addLink(washingt, atlanta)
        self.addLink(washingt, philadel)
        self.addLink(atlanta, dallas)
        self.addLink(atlanta, newyork)
        self.addLink(mexicoci, dallas)
        self.addLink(phoenix, losangel)
        self.addLink(phoenix, dallas)
        self.addLink(dallas, stlouis)
        self.addLink(stlouis, chicago)
        self.addLink(sandiego, losangel)
        self.addLink(losangel, santacla)
        self.addLink(losangel, sacramen)
        self.addLink(losangel, chicago)
        self.addLink(losangel, pennsauk)
        self.addLink(santacla, stockton)
        self.addLink(santacla, sacramen)
        self.addLink(santacla, fresno)
        self.addLink(santacla, sanfranc)
        self.addLink(sanfranc, seattle)
        self.addLink(newyork, boston)
        self.addLink(newyork, philadel)
        self.addLink(seattle, saltlake)
        self.addLink(seattle, chicago)
        self.addLink(chicago, minneapo)
        self.addLink(chicago, detroit)
        self.addLink(detroit, pittsbur)
        self.addLink(pittsbur, philadel)
        self.addLink(philadel, pennsauk)


topos = {"Agis": (lambda: Agis())}

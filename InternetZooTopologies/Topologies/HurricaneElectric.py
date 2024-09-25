#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class HurricaneElectric(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        amsterda = self.addSwitch("amsterda", dpid="0000000000000002")
        frankfur = self.addSwitch("frankfur", dpid="0000000000000003")
        london = self.addSwitch("london", dpid="0000000000000004")
        paris = self.addSwitch("paris", dpid="0000000000000005")
        paloalto = self.addSwitch("paloalto", dpid="0000000000000006")
        fremont11 = self.addSwitch("fremont11", dpid="0000000000000007")
        zurich = self.addSwitch("zurich", dpid="0000000000000008")
        stockhol = self.addSwitch("stockhol", dpid="0000000000000009")
        fremont22 = self.addSwitch("fremont22", dpid="000000000000000a")
        sanjose22 = self.addSwitch("sanjose22", dpid="000000000000000b")
        newyork33 = self.addSwitch("newyork33", dpid="000000000000000c")
        newyork22 = self.addSwitch("newyork22", dpid="000000000000000d")
        newyork11 = self.addSwitch("newyork11", dpid="000000000000000e")
        sanjose11 = self.addSwitch("sanjose11", dpid="000000000000000f")
        atlanta = self.addSwitch("atlanta", dpid="0000000000000010")
        miami = self.addSwitch("miami", dpid="0000000000000011")
        hongkong = self.addSwitch("hongkong", dpid="0000000000000012")
        tokyo = self.addSwitch("tokyo", dpid="0000000000000013")
        seattle = self.addSwitch("seattle", dpid="0000000000000014")
        losangel = self.addSwitch("losangel", dpid="0000000000000015")
        dallas = self.addSwitch("dallas", dpid="0000000000000016")
        chicago = self.addSwitch("chicago", dpid="0000000000000017")
        toronto = self.addSwitch("toronto", dpid="0000000000000018")
        ashburn = self.addSwitch("ashburn", dpid="0000000000000019")

        # Adding Links
        self.addLink(amsterda, frankfur)
        self.addLink(amsterda, london)
        self.addLink(amsterda, paris)
        self.addLink(amsterda, newyork11)
        self.addLink(frankfur, paris)
        self.addLink(frankfur, zurich)
        self.addLink(frankfur, stockhol)
        self.addLink(london, newyork11)
        self.addLink(london, ashburn)
        self.addLink(paris, ashburn)
        self.addLink(paloalto, fremont11)
        self.addLink(paloalto, fremont22)
        self.addLink(paloalto, sanjose22)
        self.addLink(paloalto, sanjose11)
        self.addLink(paloalto, losangel)
        self.addLink(paloalto, ashburn)
        self.addLink(fremont11, sanjose22)
        self.addLink(fremont22, sanjose22)
        self.addLink(sanjose22, newyork11)
        self.addLink(sanjose22, sanjose11)
        self.addLink(sanjose22, seattle)
        self.addLink(sanjose22, chicago)
        self.addLink(newyork33, newyork22)
        self.addLink(newyork33, newyork11)
        self.addLink(newyork22, newyork11)
        self.addLink(newyork22, toronto)
        self.addLink(newyork11, losangel)
        self.addLink(newyork11, chicago)
        self.addLink(newyork11, ashburn)
        self.addLink(sanjose11, hongkong)
        self.addLink(sanjose11, tokyo)
        self.addLink(atlanta, dallas)
        self.addLink(atlanta, ashburn)
        self.addLink(miami, ashburn)
        self.addLink(losangel, dallas)
        self.addLink(dallas, chicago)
        self.addLink(dallas, ashburn)


topos = {"HurricaneElectric": (lambda: HurricaneElectric())}

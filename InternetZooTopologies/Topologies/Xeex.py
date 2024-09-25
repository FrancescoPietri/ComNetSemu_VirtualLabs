#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Xeex(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        denver = self.addSwitch("denver", dpid="0000000000000002")
        lasvegas = self.addSwitch("lasvegas", dpid="0000000000000003")
        indianap = self.addSwitch("indianap", dpid="0000000000000004")
        nashvill = self.addSwitch("nashvill", dpid="0000000000000005")
        phoenix = self.addSwitch("phoenix", dpid="0000000000000006")
        hongkong = self.addSwitch("hongkong", dpid="0000000000000007")
        sanfranc = self.addSwitch("sanfranc", dpid="0000000000000008")
        sandiego = self.addSwitch("sandiego", dpid="0000000000000009")
        tokyo = self.addSwitch("tokyo", dpid="000000000000000a")
        chennai = self.addSwitch("chennai", dpid="000000000000000b")
        london = self.addSwitch("london", dpid="000000000000000c")
        pittsbur = self.addSwitch("pittsbur", dpid="000000000000000d")
        columbus = self.addSwitch("columbus", dpid="000000000000000e")
        amsterda = self.addSwitch("amsterda", dpid="000000000000000f")
        miami = self.addSwitch("miami", dpid="0000000000000010")
        cincinna = self.addSwitch("cincinna", dpid="0000000000000011")
        seattle = self.addSwitch("seattle", dpid="0000000000000012")
        sanjose = self.addSwitch("sanjose", dpid="0000000000000013")
        losangel = self.addSwitch("losangel", dpid="0000000000000014")
        chicago = self.addSwitch("chicago", dpid="0000000000000015")
        ashburn = self.addSwitch("ashburn", dpid="0000000000000016")
        newyork = self.addSwitch("newyork", dpid="0000000000000017")
        atlanta = self.addSwitch("atlanta", dpid="0000000000000018")
        dallas = self.addSwitch("dallas", dpid="0000000000000019")

        # Adding Links
        self.addLink(denver, lasvegas)
        self.addLink(denver, chicago)
        self.addLink(lasvegas, losangel)
        self.addLink(indianap, chicago)
        self.addLink(indianap, columbus)
        self.addLink(nashvill, cincinna)
        self.addLink(nashvill, atlanta)
        self.addLink(nashvill, dallas)
        self.addLink(phoenix, losangel)
        self.addLink(phoenix, sandiego)
        self.addLink(phoenix, dallas)
        self.addLink(hongkong, tokyo)
        self.addLink(hongkong, chennai)
        self.addLink(hongkong, losangel)
        self.addLink(sanfranc, seattle)
        self.addLink(sanfranc, sanjose)
        self.addLink(sandiego, losangel)
        self.addLink(tokyo, sanjose)
        self.addLink(tokyo, chennai)
        self.addLink(london, newyork)
        self.addLink(pittsbur, columbus)
        self.addLink(pittsbur, ashburn)
        self.addLink(amsterda, ashburn)
        self.addLink(miami, ashburn)
        self.addLink(miami, atlanta)
        self.addLink(cincinna, chicago)
        self.addLink(seattle, chicago)
        self.addLink(sanjose, losangel)
        self.addLink(sanjose, chicago)
        self.addLink(chicago, newyork)
        self.addLink(chicago, dallas)
        self.addLink(ashburn, atlanta)
        self.addLink(ashburn, newyork)
        self.addLink(atlanta, dallas)


topos = {"Xeex": (lambda: Xeex())}

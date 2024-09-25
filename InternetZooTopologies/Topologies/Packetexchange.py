#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Packetexchange(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        miami = self.addSwitch("miami", dpid="0000000000000002")
        london = self.addSwitch("london", dpid="0000000000000003")
        ashburn = self.addSwitch("ashburn", dpid="0000000000000004")
        newyork = self.addSwitch("newyork", dpid="0000000000000005")
        paris = self.addSwitch("paris", dpid="0000000000000006")
        milan = self.addSwitch("milan", dpid="0000000000000007")
        amsterda = self.addSwitch("amsterda", dpid="0000000000000008")
        frankfur = self.addSwitch("frankfur", dpid="0000000000000009")
        hongkong = self.addSwitch("hongkong", dpid="000000000000000a")
        singapor = self.addSwitch("singapor", dpid="000000000000000b")
        losangel = self.addSwitch("losangel", dpid="000000000000000c")
        kansasci = self.addSwitch("kansasci", dpid="000000000000000d")
        chicago = self.addSwitch("chicago", dpid="000000000000000e")
        seattle = self.addSwitch("seattle", dpid="000000000000000f")
        sanfranc = self.addSwitch("sanfranc", dpid="0000000000000010")
        sanjose = self.addSwitch("sanjose", dpid="0000000000000011")
        houston = self.addSwitch("houston", dpid="0000000000000012")
        lasvegas = self.addSwitch("lasvegas", dpid="0000000000000013")
        phoenix = self.addSwitch("phoenix", dpid="0000000000000014")
        dallas = self.addSwitch("dallas", dpid="0000000000000015")
        atlanta = self.addSwitch("atlanta", dpid="0000000000000016")

        # Adding Links
        self.addLink(miami, houston)
        self.addLink(miami, atlanta)
        self.addLink(london, ashburn)
        self.addLink(london, newyork)
        self.addLink(london, paris)
        self.addLink(london, amsterda)
        self.addLink(ashburn, chicago)
        self.addLink(ashburn, atlanta)
        self.addLink(newyork, paris)
        self.addLink(paris, frankfur)
        self.addLink(milan, frankfur)
        self.addLink(amsterda, frankfur)
        self.addLink(hongkong, singapor)
        self.addLink(hongkong, sanfranc)
        self.addLink(singapor, losangel)
        self.addLink(losangel, phoenix)
        self.addLink(losangel, sanjose)
        self.addLink(losangel, lasvegas)
        self.addLink(kansasci, dallas)
        self.addLink(kansasci, chicago)
        self.addLink(kansasci, seattle)
        self.addLink(kansasci, sanfranc)
        self.addLink(seattle, sanfranc)
        self.addLink(sanfranc, sanjose)
        self.addLink(houston, dallas)
        self.addLink(phoenix, dallas)
        self.addLink(dallas, atlanta)


topos = {"Packetexchange": (lambda: Packetexchange())}

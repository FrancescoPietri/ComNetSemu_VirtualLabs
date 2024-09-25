#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Abvt(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        washingt = self.addSwitch("washingt", dpid="0000000000000002")
        newyork = self.addSwitch("newyork", dpid="0000000000000003")
        atlanta = self.addSwitch("atlanta", dpid="0000000000000004")
        miami = self.addSwitch("miami", dpid="0000000000000005")
        boston = self.addSwitch("boston", dpid="0000000000000006")
        london = self.addSwitch("london", dpid="0000000000000007")
        philadel = self.addSwitch("philadel", dpid="0000000000000008")
        baltimor = self.addSwitch("baltimor", dpid="0000000000000009")
        amsterda = self.addSwitch("amsterda", dpid="000000000000000a")
        frankfur = self.addSwitch("frankfur", dpid="000000000000000b")
        houston = self.addSwitch("houston", dpid="000000000000000c")
        none = self.addSwitch("none", dpid="000000000000000d")
        paris = self.addSwitch("paris", dpid="000000000000000e")
        dallas = self.addSwitch("dallas", dpid="000000000000000f")
        austin = self.addSwitch("austin", dpid="0000000000000010")
        seattle = self.addSwitch("seattle", dpid="0000000000000011")
        portland = self.addSwitch("portland", dpid="0000000000000012")
        tokyo = self.addSwitch("tokyo", dpid="0000000000000013")
        sanfranc = self.addSwitch("sanfranc", dpid="0000000000000014")
        losangel = self.addSwitch("losangel", dpid="0000000000000015")
        phoenix = self.addSwitch("phoenix", dpid="0000000000000016")
        denver = self.addSwitch("denver", dpid="0000000000000017")
        chicago = self.addSwitch("chicago", dpid="0000000000000018")

        # Adding Links
        self.addLink(washingt, atlanta)
        self.addLink(washingt, boston)
        self.addLink(washingt, london)
        self.addLink(washingt, baltimor)
        self.addLink(newyork, amsterda)
        self.addLink(newyork, philadel)
        self.addLink(newyork, boston)
        self.addLink(newyork, london)
        self.addLink(newyork, chicago)
        self.addLink(atlanta, houston)
        self.addLink(atlanta, miami)
        self.addLink(miami, houston)
        self.addLink(london, paris)
        self.addLink(london, amsterda)
        self.addLink(philadel, baltimor)
        self.addLink(amsterda, frankfur)
        self.addLink(frankfur, paris)
        self.addLink(houston, phoenix)
        self.addLink(houston, dallas)
        self.addLink(houston, austin)
        self.addLink(none, dallas)
        self.addLink(none, chicago)
        self.addLink(none, denver)
        self.addLink(dallas, austin)
        self.addLink(seattle, portland)
        self.addLink(seattle, chicago)
        self.addLink(portland, sanfranc)
        self.addLink(tokyo, sanfranc)
        self.addLink(sanfranc, losangel)
        self.addLink(sanfranc, denver)
        self.addLink(losangel, phoenix)


topos = {"Abvt": (lambda: Abvt())}

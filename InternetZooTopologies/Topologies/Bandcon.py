#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Bandcon(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        paris = self.addSwitch("paris", dpid="0000000000000002")
        atlanta = self.addSwitch("atlanta", dpid="0000000000000003")
        brussels = self.addSwitch("brussels", dpid="0000000000000004")
        frankfur = self.addSwitch("frankfur", dpid="0000000000000005")
        phoenix = self.addSwitch("phoenix", dpid="0000000000000006")
        lasvegas = self.addSwitch("lasvegas", dpid="0000000000000007")
        miami = self.addSwitch("miami", dpid="0000000000000008")
        dallas = self.addSwitch("dallas", dpid="0000000000000009")
        losangel = self.addSwitch("losangel", dpid="000000000000000a")
        houston = self.addSwitch("houston", dpid="000000000000000b")
        philadel = self.addSwitch("philadel", dpid="000000000000000c")
        boston = self.addSwitch("boston", dpid="000000000000000d")
        london = self.addSwitch("london", dpid="000000000000000e")
        amsterda = self.addSwitch("amsterda", dpid="000000000000000f")
        sanjose = self.addSwitch("sanjose", dpid="0000000000000010")
        sanfranc = self.addSwitch("sanfranc", dpid="0000000000000011")
        seattle = self.addSwitch("seattle", dpid="0000000000000012")
        chicago = self.addSwitch("chicago", dpid="0000000000000013")
        toronto = self.addSwitch("toronto", dpid="0000000000000014")
        ashburn = self.addSwitch("ashburn", dpid="0000000000000015")
        newjerse = self.addSwitch("newjerse", dpid="0000000000000016")
        newyork = self.addSwitch("newyork", dpid="0000000000000017")

        # Adding Links
        self.addLink(paris, frankfur)
        self.addLink(paris, london)
        self.addLink(atlanta, ashburn)
        self.addLink(atlanta, miami)
        self.addLink(brussels, frankfur)
        self.addLink(brussels, amsterda)
        self.addLink(phoenix, losangel)
        self.addLink(phoenix, dallas)
        self.addLink(lasvegas, losangel)
        self.addLink(lasvegas, sanjose)
        self.addLink(miami, dallas)
        self.addLink(dallas, houston)
        self.addLink(dallas, ashburn)
        self.addLink(dallas, chicago)
        self.addLink(losangel, sanjose)
        self.addLink(philadel, toronto)
        self.addLink(philadel, ashburn)
        self.addLink(boston, toronto)
        self.addLink(boston, newyork)
        self.addLink(london, amsterda)
        self.addLink(london, newyork)
        self.addLink(amsterda, ashburn)
        self.addLink(sanjose, chicago)
        self.addLink(sanjose, sanfranc)
        self.addLink(sanfranc, seattle)
        self.addLink(seattle, chicago)
        self.addLink(chicago, toronto)
        self.addLink(chicago, ashburn)


topos = {"Bandcon": (lambda: Bandcon())}

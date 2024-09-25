#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class EliBackbone(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        lasvegas = self.addSwitch("lasvegas", dpid="0000000000000002")
        losangel = self.addSwitch("losangel", dpid="0000000000000003")
        dallas = self.addSwitch("dallas", dpid="0000000000000004")
        phoenix = self.addSwitch("phoenix", dpid="0000000000000005")
        santacla = self.addSwitch("santacla", dpid="0000000000000006")
        portland = self.addSwitch("portland", dpid="0000000000000007")
        sacramen = self.addSwitch("sacramen", dpid="0000000000000008")
        paloalto = self.addSwitch("paloalto", dpid="0000000000000009")
        tacoma = self.addSwitch("tacoma", dpid="000000000000000a")
        seattle = self.addSwitch("seattle", dpid="000000000000000b")
        atlanta = self.addSwitch("atlanta", dpid="000000000000000c")
        houston = self.addSwitch("houston", dpid="000000000000000d")
        spokane = self.addSwitch("spokane", dpid="000000000000000e")
        boise = self.addSwitch("boise", dpid="000000000000000f")
        saltlake = self.addSwitch("saltlake", dpid="0000000000000010")
        minneapo = self.addSwitch("minneapo", dpid="0000000000000011")
        chicago = self.addSwitch("chicago", dpid="0000000000000012")
        rocheste = self.addSwitch("rocheste", dpid="0000000000000013")
        newark = self.addSwitch("newark", dpid="0000000000000014")
        washingt = self.addSwitch("washingt", dpid="0000000000000015")

        # Adding Links
        self.addLink(lasvegas, losangel)
        self.addLink(lasvegas, phoenix)
        self.addLink(lasvegas, saltlake)
        self.addLink(losangel, phoenix)
        self.addLink(losangel, santacla)
        self.addLink(dallas, chicago)
        self.addLink(dallas, houston)
        self.addLink(dallas, phoenix)
        self.addLink(dallas, washingt)
        self.addLink(santacla, paloalto)
        self.addLink(portland, tacoma)
        self.addLink(portland, sacramen)
        self.addLink(sacramen, tacoma)
        self.addLink(sacramen, saltlake)
        self.addLink(sacramen, paloalto)
        self.addLink(paloalto, seattle)
        self.addLink(tacoma, seattle)
        self.addLink(seattle, spokane)
        self.addLink(seattle, boise)
        self.addLink(seattle, saltlake)
        self.addLink(seattle, minneapo)
        self.addLink(atlanta, houston)
        self.addLink(atlanta, washingt)
        self.addLink(spokane, boise)
        self.addLink(boise, saltlake)
        self.addLink(saltlake, chicago)
        self.addLink(minneapo, chicago)
        self.addLink(chicago, rocheste)
        self.addLink(rocheste, newark)
        self.addLink(newark, washingt)


topos = {"EliBackbone": (lambda: EliBackbone())}

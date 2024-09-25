#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Integra(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        chicago = self.addSwitch("chicago", dpid="0000000000000002")
        dallas = self.addSwitch("dallas", dpid="0000000000000003")
        stcloud = self.addSwitch("stcloud", dpid="0000000000000004")
        minneapo = self.addSwitch("minneapo", dpid="0000000000000005")
        losangel = self.addSwitch("losangel", dpid="0000000000000006")
        santacla = self.addSwitch("santacla", dpid="0000000000000007")
        lasvegas = self.addSwitch("lasvegas", dpid="0000000000000008")
        phoenix = self.addSwitch("phoenix", dpid="0000000000000009")
        sacramen = self.addSwitch("sacramen", dpid="000000000000000a")
        santaros = self.addSwitch("santaros", dpid="000000000000000b")
        salem = self.addSwitch("salem", dpid="000000000000000c")
        bend = self.addSwitch("bend", dpid="000000000000000d")
        eugene = self.addSwitch("eugene", dpid="000000000000000e")
        reno = self.addSwitch("reno", dpid="000000000000000f")
        ranchoco = self.addSwitch("ranchoco", dpid="0000000000000010")
        newyork = self.addSwitch("newyork", dpid="0000000000000011")
        ashburn = self.addSwitch("ashburn", dpid="0000000000000012")
        spokane = self.addSwitch("spokane", dpid="0000000000000013")
        fargo = self.addSwitch("fargo", dpid="0000000000000014")
        billings = self.addSwitch("billings", dpid="0000000000000015")
        denver = self.addSwitch("denver", dpid="0000000000000016")
        ogden = self.addSwitch("ogden", dpid="0000000000000017")
        orem = self.addSwitch("orem", dpid="0000000000000018")
        saltlake = self.addSwitch("saltlake", dpid="0000000000000019")
        boise = self.addSwitch("boise", dpid="000000000000001a")
        portland = self.addSwitch("portland", dpid="000000000000001b")
        seattle = self.addSwitch("seattle", dpid="000000000000001c")

        # Adding Links
        self.addLink(chicago, ashburn)
        self.addLink(chicago, minneapo)
        self.addLink(chicago, denver)
        self.addLink(dallas, denver)
        self.addLink(dallas, phoenix)
        self.addLink(stcloud, fargo)
        self.addLink(stcloud, minneapo)
        self.addLink(minneapo, fargo)
        self.addLink(minneapo, seattle)
        self.addLink(minneapo, newyork)
        self.addLink(losangel, santacla)
        self.addLink(losangel, lasvegas)
        self.addLink(losangel, phoenix)
        self.addLink(santacla, sacramen)
        self.addLink(lasvegas, saltlake)
        self.addLink(lasvegas, phoenix)
        self.addLink(sacramen, santaros)
        self.addLink(sacramen, reno)
        self.addLink(sacramen, ranchoco)
        self.addLink(sacramen, portland)
        self.addLink(salem, portland)
        self.addLink(salem, eugene)
        self.addLink(bend, portland)
        self.addLink(bend, seattle)
        self.addLink(reno, saltlake)
        self.addLink(newyork, ashburn)
        self.addLink(spokane, seattle)
        self.addLink(spokane, billings)
        self.addLink(billings, denver)
        self.addLink(denver, ogden)
        self.addLink(ogden, orem)
        self.addLink(ogden, saltlake)
        self.addLink(orem, saltlake)
        self.addLink(saltlake, boise)
        self.addLink(boise, portland)
        self.addLink(portland, seattle)


topos = {"Integra": (lambda: Integra())}

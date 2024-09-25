#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Aconet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        eisensta = self.addSwitch("eisensta", dpid="0000000000000002")
        stpolte = self.addSwitch("stpolte", dpid="0000000000000003")
        graz2 = self.addSwitch("graz2", dpid="0000000000000004")
        leoben = self.addSwitch("leoben", dpid="0000000000000005")
        vienna2 = self.addSwitch("vienna2", dpid="0000000000000006")
        geant = self.addSwitch("geant", dpid="0000000000000007")
        krems = self.addSwitch("krems", dpid="0000000000000008")
        vienna1 = self.addSwitch("vienna1", dpid="0000000000000009")
        level3 = self.addSwitch("level3", dpid="000000000000000a")
        vix = self.addSwitch("vix", dpid="000000000000000b")
        none = self.addSwitch("none", dpid="000000000000000c")
        sanet = self.addSwitch("sanet", dpid="000000000000000d")
        cesnet = self.addSwitch("cesnet", dpid="000000000000000e")
        klagenfu2 = self.addSwitch("klagenfu2", dpid="000000000000000f")
        graz1 = self.addSwitch("graz1", dpid="0000000000000010")
        linz1 = self.addSwitch("linz1", dpid="0000000000000011")
        linz2 = self.addSwitch("linz2", dpid="0000000000000012")
        salzburg1 = self.addSwitch("salzburg1", dpid="0000000000000013")
        salzburg2 = self.addSwitch("salzburg2", dpid="0000000000000014")
        innsbruc1 = self.addSwitch("innsbruc1", dpid="0000000000000015")
        innsbruc2 = self.addSwitch("innsbruc2", dpid="0000000000000016")
        dornbirn = self.addSwitch("dornbirn", dpid="0000000000000017")
        klagenfu1 = self.addSwitch("klagenfu1", dpid="0000000000000018")

        # Adding Links
        self.addLink(eisensta, vienna2)
        self.addLink(eisensta, vienna1)
        self.addLink(stpolte, krems)
        self.addLink(stpolte, vienna1)
        self.addLink(graz2, leoben)
        self.addLink(graz2, graz1)
        self.addLink(graz2, vienna1)
        self.addLink(leoben, graz1)
        self.addLink(vienna2, krems)
        self.addLink(vienna2, none)
        self.addLink(vienna2, klagenfu2)
        self.addLink(vienna2, graz1)
        self.addLink(vienna2, linz1)
        self.addLink(vienna2, salzburg2)
        self.addLink(vienna2, innsbruc1)
        self.addLink(geant, none)
        self.addLink(vienna1, none)
        self.addLink(vienna1, linz2)
        self.addLink(vienna1, salzburg1)
        self.addLink(vienna1, innsbruc2)
        self.addLink(vienna1, klagenfu1)
        self.addLink(level3, none)
        self.addLink(vix, none)
        self.addLink(none, sanet)
        self.addLink(none, cesnet)
        self.addLink(klagenfu2, klagenfu1)
        self.addLink(linz1, linz2)
        self.addLink(salzburg1, salzburg2)
        self.addLink(innsbruc1, innsbruc2)
        self.addLink(innsbruc1, dornbirn)
        self.addLink(innsbruc2, dornbirn)


topos = {"Aconet": (lambda: Aconet())}

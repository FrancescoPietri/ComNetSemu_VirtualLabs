#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Padi(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        aqsa = self.addSwitch("aqsa", dpid="0000000000000002")
        iug = self.addSwitch("iug", dpid="0000000000000003")
        hu = self.addSwitch("hu", dpid="0000000000000004")
        ppu = self.addSwitch("ppu", dpid="0000000000000005")
        azhr = self.addSwitch("azhr", dpid="0000000000000006")
        arij = self.addSwitch("arij", dpid="0000000000000007")
        icb = self.addSwitch("icb", dpid="0000000000000008")
        geant = self.addSwitch("geant", dpid="0000000000000009")
        annajahn = self.addSwitch("annajahn", dpid="000000000000000a")
        aauj = self.addSwitch("aauj", dpid="000000000000000b")
        bzu = self.addSwitch("bzu", dpid="000000000000000c")
        padi2 = self.addSwitch("padi2", dpid="000000000000000d")
        qou = self.addSwitch("qou", dpid="000000000000000e")
        aqu = self.addSwitch("aqu", dpid="000000000000000f")
        bu = self.addSwitch("bu", dpid="0000000000000010")

        # Adding Links
        self.addLink(ppu, padi2)
        self.addLink(geant, padi2)
        self.addLink(bzu, padi2)
        self.addLink(padi2, qou)
        self.addLink(padi2, aqu)
        self.addLink(padi2, bu)


topos = {"Padi": (lambda: Padi())}

#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Ilan(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        telavivg = self.addSwitch("telavivg", dpid="0000000000000002")
        intlbac = self.addSwitch("intlbac", dpid="0000000000000003")
        iix = self.addSwitch("iix", dpid="0000000000000004")
        petachti = self.addSwitch("petachti", dpid="0000000000000005")
        external = self.addSwitch("external", dpid="0000000000000006")
        geant2ge = self.addSwitch("geant2ge", dpid="0000000000000007")
        openuniv = self.addSwitch("openuniv", dpid="0000000000000008")
        haifauni = self.addSwitch("haifauni", dpid="0000000000000009")
        technion = self.addSwitch("technion", dpid="000000000000000a")
        barilanu = self.addSwitch("barilanu", dpid="000000000000000b")
        hebrewun = self.addSwitch("hebrewun", dpid="000000000000000c")
        bengurio = self.addSwitch("bengurio", dpid="000000000000000d")
        weizmann = self.addSwitch("weizmann", dpid="000000000000000e")
        telavivu = self.addSwitch("telavivu", dpid="000000000000000f")

        # Adding Links
        self.addLink(telavivg, intlbac)
        self.addLink(telavivg, haifauni)
        self.addLink(telavivg, technion)
        self.addLink(telavivg, barilanu)
        self.addLink(telavivg, hebrewun)
        self.addLink(telavivg, bengurio)
        self.addLink(telavivg, weizmann)
        self.addLink(telavivg, telavivu)
        self.addLink(iix, petachti)
        self.addLink(petachti, external)
        self.addLink(petachti, geant2ge)
        self.addLink(petachti, openuniv)
        self.addLink(petachti, haifauni)
        self.addLink(petachti, barilanu)
        self.addLink(petachti, telavivu)


topos = {"Ilan": (lambda: Ilan())}

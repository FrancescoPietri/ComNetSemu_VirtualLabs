#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Amres(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        bor = self.addSwitch("bor", dpid="0000000000000002")
        kosovska = self.addSwitch("kosovska", dpid="0000000000000003")
        novipaza = self.addSwitch("novipaza", dpid="0000000000000004")
        krusteva = self.addSwitch("krusteva", dpid="0000000000000005")
        vranje = self.addSwitch("vranje", dpid="0000000000000006")
        nis = self.addSwitch("nis", dpid="0000000000000007")
        pirot = self.addSwitch("pirot", dpid="0000000000000008")
        leskovac = self.addSwitch("leskovac", dpid="0000000000000009")
        kragujev = self.addSwitch("kragujev", dpid="000000000000000a")
        novisad = self.addSwitch("novisad", dpid="000000000000000b")
        bosniaan = self.addSwitch("bosniaan", dpid="000000000000000c")
        hungarne = self.addSwitch("hungarne", dpid="000000000000000d")
        beograd = self.addSwitch("beograd", dpid="000000000000000e")
        pancevo = self.addSwitch("pancevo", dpid="000000000000000f")
        telekoms = self.addSwitch("telekoms", dpid="0000000000000010")
        kraljevo = self.addSwitch("kraljevo", dpid="0000000000000011")
        raska = self.addSwitch("raska", dpid="0000000000000012")
        subotica = self.addSwitch("subotica", dpid="0000000000000013")
        sombor = self.addSwitch("sombor", dpid="0000000000000014")
        zrenjani = self.addSwitch("zrenjani", dpid="0000000000000015")
        sabac = self.addSwitch("sabac", dpid="0000000000000016")
        valjevo = self.addSwitch("valjevo", dpid="0000000000000017")
        uzice = self.addSwitch("uzice", dpid="0000000000000018")
        cacak = self.addSwitch("cacak", dpid="0000000000000019")
        velikapl = self.addSwitch("velikapl", dpid="000000000000001a")

        # Adding Links
        self.addLink(bor, nis)
        self.addLink(kosovska, beograd)
        self.addLink(novipaza, raska)
        self.addLink(krusteva, nis)
        self.addLink(krusteva, kraljevo)
        self.addLink(vranje, leskovac)
        self.addLink(nis, pirot)
        self.addLink(nis, leskovac)
        self.addLink(kragujev, velikapl)
        self.addLink(kragujev, kraljevo)
        self.addLink(novisad, subotica)
        self.addLink(novisad, sombor)
        self.addLink(novisad, zrenjani)
        self.addLink(novisad, beograd)
        self.addLink(bosniaan, sabac)
        self.addLink(hungarne, subotica)
        self.addLink(beograd, pancevo)
        self.addLink(beograd, telekoms)
        self.addLink(beograd, sabac)
        self.addLink(beograd, valjevo)
        self.addLink(beograd, velikapl)
        self.addLink(kraljevo, raska)
        self.addLink(valjevo, uzice)
        self.addLink(uzice, cacak)


topos = {"Amres": (lambda: Amres())}

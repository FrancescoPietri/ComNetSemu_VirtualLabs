#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Rnp(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        revife = self.addSwitch("revife", dpid="0000000000000002")
        maceio = self.addSwitch("maceio", dpid="0000000000000003")
        campinag = self.addSwitch("campinag", dpid="0000000000000004")
        jobopass = self.addSwitch("jobopass", dpid="0000000000000005")
        brasilia = self.addSwitch("brasilia", dpid="0000000000000006")
        belohori = self.addSwitch("belohori", dpid="0000000000000007")
        aracaju = self.addSwitch("aracaju", dpid="0000000000000008")
        salvador = self.addSwitch("salvador", dpid="0000000000000009")
        vitoria = self.addSwitch("vitoria", dpid="000000000000000a")
        riodejan = self.addSwitch("riodejan", dpid="000000000000000b")
        manaus = self.addSwitch("manaus", dpid="000000000000000c")
        goiania = self.addSwitch("goiania", dpid="000000000000000d")
        cuiaba = self.addSwitch("cuiaba", dpid="000000000000000e")
        curitiba = self.addSwitch("curitiba", dpid="000000000000000f")
        portoale = self.addSwitch("portoale", dpid="0000000000000010")
        floriano = self.addSwitch("floriano", dpid="0000000000000011")
        saopaulo = self.addSwitch("saopaulo", dpid="0000000000000012")
        portovel = self.addSwitch("portovel", dpid="0000000000000013")
        riobranc = self.addSwitch("riobranc", dpid="0000000000000014")
        palmas = self.addSwitch("palmas", dpid="0000000000000015")
        campogra = self.addSwitch("campogra", dpid="0000000000000016")
        teresina = self.addSwitch("teresina", dpid="0000000000000017")
        natal = self.addSwitch("natal", dpid="0000000000000018")
        redclara = self.addSwitch("redclara", dpid="0000000000000019")
        inetnetc = self.addSwitch("inetnetc", dpid="000000000000001a")
        americas = self.addSwitch("americas", dpid="000000000000001b")
        boavista = self.addSwitch("boavista", dpid="000000000000001c")
        macapa = self.addSwitch("macapa", dpid="000000000000001d")
        belem = self.addSwitch("belem", dpid="000000000000001e")
        saoluis = self.addSwitch("saoluis", dpid="000000000000001f")
        fortalez = self.addSwitch("fortalez", dpid="0000000000000020")

        # Adding Links
        self.addLink(revife, campinag)
        self.addLink(revife, teresina)
        self.addLink(maceio, aracaju)
        self.addLink(campinag, jobopass)
        self.addLink(jobopass, natal)
        self.addLink(brasilia, riodejan)
        self.addLink(brasilia, boavista)
        self.addLink(brasilia, macapa)
        self.addLink(brasilia, manaus)
        self.addLink(brasilia, belohori)
        self.addLink(belohori, saopaulo)
        self.addLink(belohori, fortalez)
        self.addLink(belohori, salvador)
        self.addLink(aracaju, salvador)
        self.addLink(salvador, vitoria)
        self.addLink(vitoria, riodejan)
        self.addLink(riodejan, saopaulo)
        self.addLink(goiania, palmas)
        self.addLink(goiania, cuiaba)
        self.addLink(cuiaba, portovel)
        self.addLink(cuiaba, campogra)
        self.addLink(curitiba, saopaulo)
        self.addLink(curitiba, campogra)
        self.addLink(curitiba, portoale)
        self.addLink(portoale, floriano)
        self.addLink(floriano, saopaulo)
        self.addLink(saopaulo, redclara)
        self.addLink(saopaulo, inetnetc)
        self.addLink(saopaulo, americas)
        self.addLink(portovel, riobranc)
        self.addLink(teresina, belem)
        self.addLink(natal, fortalez)
        self.addLink(belem, saoluis)
        self.addLink(saoluis, fortalez)


topos = {"Rnp": (lambda: Rnp())}

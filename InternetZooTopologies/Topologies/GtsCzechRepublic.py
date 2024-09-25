#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class GtsCzechRepublic(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        klatovy = self.addSwitch("klatovy", dpid="0000000000000002")
        pisek = self.addSwitch("pisek", dpid="0000000000000003")
        chomutov = self.addSwitch("chomutov", dpid="0000000000000004")
        plzen = self.addSwitch("plzen", dpid="0000000000000005")
        jindrich = self.addSwitch("jindrich", dpid="0000000000000006")
        havlicku = self.addSwitch("havlicku", dpid="0000000000000007")
        ceskebud = self.addSwitch("ceskebud", dpid="0000000000000008")
        tabor = self.addSwitch("tabor", dpid="0000000000000009")
        zmjno = self.addSwitch("zmjno", dpid="000000000000000a")
        brno = self.addSwitch("brno", dpid="000000000000000b")
        none = self.addSwitch("none", dpid="000000000000000c")
        hardeckr = self.addSwitch("hardeckr", dpid="000000000000000d")
        ustinadl = self.addSwitch("ustinadl", dpid="000000000000000e")
        kolin = self.addSwitch("kolin", dpid="000000000000000f")
        ostrava = self.addSwitch("ostrava", dpid="0000000000000010")
        zlin = self.addSwitch("zlin", dpid="0000000000000011")
        ostrokov = self.addSwitch("ostrokov", dpid="0000000000000012")
        hodonin = self.addSwitch("hodonin", dpid="0000000000000013")
        bratisla = self.addSwitch("bratisla", dpid="0000000000000014")
        frankfur = self.addSwitch("frankfur", dpid="0000000000000015")
        warsaw = self.addSwitch("warsaw", dpid="0000000000000016")
        prostejo = self.addSwitch("prostejo", dpid="0000000000000017")
        beroun = self.addSwitch("beroun", dpid="0000000000000018")
        karlovyv = self.addSwitch("karlovyv", dpid="0000000000000019")
        opava = self.addSwitch("opava", dpid="000000000000001a")
        olomouc = self.addSwitch("olomouc", dpid="000000000000001b")
        ceskatre = self.addSwitch("ceskatre", dpid="000000000000001c")
        liberec = self.addSwitch("liberec", dpid="000000000000001d")
        semily = self.addSwitch("semily", dpid="000000000000001e")
        kladno = self.addSwitch("kladno", dpid="000000000000001f")
        prague = self.addSwitch("prague", dpid="0000000000000020")
        mladabol = self.addSwitch("mladabol", dpid="0000000000000021")

        # Adding Links
        self.addLink(klatovy, plzen)
        self.addLink(pisek, ceskebud)
        self.addLink(chomutov, ustinadl)
        self.addLink(chomutov, karlovyv)
        self.addLink(plzen, beroun)
        self.addLink(plzen, karlovyv)
        self.addLink(jindrich, havlicku)
        self.addLink(jindrich, ceskebud)
        self.addLink(havlicku, brno)
        self.addLink(ceskebud, prague)
        self.addLink(ceskebud, tabor)
        self.addLink(zmjno, brno)
        self.addLink(brno, hodonin)
        self.addLink(brno, bratisla)
        self.addLink(none, hardeckr)
        self.addLink(hardeckr, semily)
        self.addLink(hardeckr, ceskatre)
        self.addLink(hardeckr, prague)
        self.addLink(ustinadl, liberec)
        self.addLink(kolin, prague)
        self.addLink(ostrava, opava)
        self.addLink(ostrava, olomouc)
        self.addLink(ostrava, warsaw)
        self.addLink(ostrava, zlin)
        self.addLink(zlin, ostrokov)
        self.addLink(ostrokov, hodonin)
        self.addLink(frankfur, prague)
        self.addLink(prostejo, olomouc)
        self.addLink(beroun, prague)
        self.addLink(olomouc, ceskatre)
        self.addLink(liberec, semily)
        self.addLink(kladno, prague)
        self.addLink(prague, mladabol)


topos = {"GtsCzechRepublic": (lambda: GtsCzechRepublic())}

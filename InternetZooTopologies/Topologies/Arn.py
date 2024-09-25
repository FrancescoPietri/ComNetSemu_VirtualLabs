#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Arn(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        djelfa = self.addSwitch("djelfa", dpid="0000000000000002")
        medea = self.addSwitch("medea", dpid="0000000000000003")
        internet = self.addSwitch("internet", dpid="0000000000000004")
        blida = self.addSwitch("blida", dpid="0000000000000005")
        eloued = self.addSwitch("eloued", dpid="0000000000000006")
        msila = self.addSwitch("msila", dpid="0000000000000007")
        laghouat = self.addSwitch("laghouat", dpid="0000000000000008")
        ouargla = self.addSwitch("ouargla", dpid="0000000000000009")
        constant = self.addSwitch("constant", dpid="000000000000000a")
        biskra = self.addSwitch("biskra", dpid="000000000000000b")
        batna = self.addSwitch("batna", dpid="000000000000000c")
        tiziouzo = self.addSwitch("tiziouzo", dpid="000000000000000d")
        annaba = self.addSwitch("annaba", dpid="000000000000000e")
        guelma = self.addSwitch("guelma", dpid="000000000000000f")
        tebessa = self.addSwitch("tebessa", dpid="0000000000000010")
        oumelbou = self.addSwitch("oumelbou", dpid="0000000000000011")
        bejaia = self.addSwitch("bejaia", dpid="0000000000000012")
        setif = self.addSwitch("setif", dpid="0000000000000013")
        skikda = self.addSwitch("skikda", dpid="0000000000000014")
        jijel = self.addSwitch("jijel", dpid="0000000000000015")
        tiaret = self.addSwitch("tiaret", dpid="0000000000000016")
        geant = self.addSwitch("geant", dpid="0000000000000017")
        alger = self.addSwitch("alger", dpid="0000000000000018")
        chlef = self.addSwitch("chlef", dpid="0000000000000019")
        oran = self.addSwitch("oran", dpid="000000000000001a")
        mostagan = self.addSwitch("mostagan", dpid="000000000000001b")
        tlemcen = self.addSwitch("tlemcen", dpid="000000000000001c")
        sidibela = self.addSwitch("sidibela", dpid="000000000000001d")
        saida = self.addSwitch("saida", dpid="000000000000001e")
        mascara = self.addSwitch("mascara", dpid="000000000000001f")

        # Adding Links
        self.addLink(djelfa, alger)
        self.addLink(medea, alger)
        self.addLink(internet, alger)
        self.addLink(blida, alger)
        self.addLink(eloued, ouargla)
        self.addLink(msila, constant)
        self.addLink(laghouat, ouargla)
        self.addLink(ouargla, alger)
        self.addLink(constant, biskra)
        self.addLink(constant, batna)
        self.addLink(constant, annaba)
        self.addLink(constant, guelma)
        self.addLink(constant, tebessa)
        self.addLink(constant, oumelbou)
        self.addLink(constant, skikda)
        self.addLink(constant, jijel)
        self.addLink(constant, alger)
        self.addLink(tiziouzo, alger)
        self.addLink(bejaia, alger)
        self.addLink(setif, alger)
        self.addLink(tiaret, oran)
        self.addLink(geant, alger)
        self.addLink(alger, chlef)
        self.addLink(alger, oran)
        self.addLink(oran, mostagan)
        self.addLink(oran, tlemcen)
        self.addLink(oran, sidibela)
        self.addLink(oran, saida)
        self.addLink(oran, mascara)


topos = {"Arn": (lambda: Arn())}

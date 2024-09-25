#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Cynet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        cyprusun = self.addSwitch("cyprusun", dpid="0000000000000002")
        intercol = self.addSwitch("intercol", dpid="0000000000000003")
        unitedna = self.addSwitch("unitedna", dpid="0000000000000004")
        cyixcypr = self.addSwitch("cyixcypr", dpid="0000000000000005")
        users = self.addSwitch("users", dpid="0000000000000006")
        grid = self.addSwitch("grid", dpid="0000000000000007")
        gridsw = self.addSwitch("gridsw", dpid="0000000000000008")
        none = self.addSwitch("none", dpid="0000000000000009")
        kyprosne = self.addSwitch("kyprosne", dpid="000000000000000a")
        instofn = self.addSwitch("instofn", dpid="000000000000000b")
        pedagogi = self.addSwitch("pedagogi", dpid="000000000000000c")
        nursings = self.addSwitch("nursings", dpid="000000000000000d")
        phillips = self.addSwitch("phillips", dpid="000000000000000e")
        european = self.addSwitch("european", dpid="000000000000000f")
        openuni = self.addSwitch("openuni", dpid="0000000000000010")
        univofn = self.addSwitch("univofn", dpid="0000000000000011")
        agricult = self.addSwitch("agricult", dpid="0000000000000012")
        cyprusin = self.addSwitch("cyprusin", dpid="0000000000000013")
        englishs = self.addSwitch("englishs", dpid="0000000000000014")
        unioffr = self.addSwitch("unioffr", dpid="0000000000000015")
        limassol = self.addSwitch("limassol", dpid="0000000000000016")
        european = self.addSwitch("european", dpid="0000000000000017")
        borderro = self.addSwitch("borderro", dpid="0000000000000018")
        eumedcon = self.addSwitch("eumedcon", dpid="0000000000000019")
        syrianre = self.addSwitch("syrianre", dpid="000000000000001a")
        geantath = self.addSwitch("geantath", dpid="000000000000001b")
        geantmil = self.addSwitch("geantmil", dpid="000000000000001c")
        univofc = self.addSwitch("univofc", dpid="000000000000001d")
        evagoras = self.addSwitch("evagoras", dpid="000000000000001e")
        nicosiap = self.addSwitch("nicosiap", dpid="000000000000001f")

        # Adding Links
        self.addLink(cyprusun, limassol)
        self.addLink(intercol, limassol)
        self.addLink(unitedna, evagoras)
        self.addLink(cyixcypr, nicosiap)
        self.addLink(users, none)
        self.addLink(grid, gridsw)
        self.addLink(gridsw, none)
        self.addLink(gridsw, nicosiap)
        self.addLink(kyprosne, nicosiap)
        self.addLink(instofn, nicosiap)
        self.addLink(pedagogi, nicosiap)
        self.addLink(nursings, nicosiap)
        self.addLink(phillips, nicosiap)
        self.addLink(european, nicosiap)
        self.addLink(openuni, nicosiap)
        self.addLink(univofn, nicosiap)
        self.addLink(agricult, nicosiap)
        self.addLink(cyprusin, nicosiap)
        self.addLink(englishs, nicosiap)
        self.addLink(unioffr, nicosiap)
        self.addLink(limassol, borderro)
        self.addLink(european, evagoras)
        self.addLink(borderro, eumedcon)
        self.addLink(borderro, geantath)
        self.addLink(borderro, geantmil)
        self.addLink(borderro, univofc)
        self.addLink(borderro, evagoras)
        self.addLink(borderro, nicosiap)
        self.addLink(eumedcon, syrianre)


topos = {"Cynet": (lambda: Cynet())}

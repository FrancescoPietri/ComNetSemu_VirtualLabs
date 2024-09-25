#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class VisionNet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        glasgow = self.addSwitch("glasgow", dpid="0000000000000002")
        bainvill = self.addSwitch("bainvill", dpid="0000000000000003")
        glendive = self.addSwitch("glendive", dpid="0000000000000004")
        culberts = self.addSwitch("culberts", dpid="0000000000000005")
        lincoln = self.addSwitch("lincoln", dpid="0000000000000006")
        helena = self.addSwitch("helena", dpid="0000000000000007")
        dillion = self.addSwitch("dillion", dpid="0000000000000008")
        missoula = self.addSwitch("missoula", dpid="0000000000000009")
        bozeman = self.addSwitch("bozeman", dpid="000000000000000a")
        sheridan = self.addSwitch("sheridan", dpid="000000000000000b")
        dcnnetwo = self.addSwitch("dcnnetwo", dpid="000000000000000c")
        fortbent = self.addSwitch("fortbent", dpid="000000000000000d")
        seattle = self.addSwitch("seattle", dpid="000000000000000e")
        havre = self.addSwitch("havre", dpid="000000000000000f")
        forsyth = self.addSwitch("forsyth", dpid="0000000000000010")
        milescit = self.addSwitch("milescit", dpid="0000000000000011")
        noxon = self.addSwitch("noxon", dpid="0000000000000012")
        kalispel = self.addSwitch("kalispel", dpid="0000000000000013")
        ncutbank = self.addSwitch("ncutbank", dpid="0000000000000014")
        fairfiel = self.addSwitch("fairfiel", dpid="0000000000000015")
        greatfal = self.addSwitch("greatfal", dpid="0000000000000016")
        moore = self.addSwitch("moore", dpid="0000000000000017")
        bigtimbe = self.addSwitch("bigtimbe", dpid="0000000000000018")
        billings = self.addSwitch("billings", dpid="0000000000000019")

        # Adding Links
        self.addLink(glasgow, culberts)
        self.addLink(glasgow, havre)
        self.addLink(bainvill, dcnnetwo)
        self.addLink(bainvill, culberts)
        self.addLink(glendive, milescit)
        self.addLink(lincoln, fairfiel)
        self.addLink(lincoln, helena)
        self.addLink(lincoln, missoula)
        self.addLink(helena, bozeman)
        self.addLink(helena, dillion)
        self.addLink(missoula, noxon)
        self.addLink(sheridan, forsyth)
        self.addLink(fortbent, greatfal)
        self.addLink(fortbent, havre)
        self.addLink(fortbent, moore)
        self.addLink(seattle, noxon)
        self.addLink(havre, ncutbank)
        self.addLink(forsyth, milescit)
        self.addLink(forsyth, billings)
        self.addLink(noxon, kalispel)
        self.addLink(fairfiel, greatfal)
        self.addLink(moore, bigtimbe)
        self.addLink(bigtimbe, billings)


topos = {"VisionNet": (lambda: VisionNet())}

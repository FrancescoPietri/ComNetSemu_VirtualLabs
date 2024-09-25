#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Nsfnet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        seqsuine = self.addSwitch("seqsuine", dpid="0000000000000002")
        jonvonne = self.addSwitch("jonvonne", dpid="0000000000000003")
        suranet = self.addSwitch("suranet", dpid="0000000000000004")
        pittsbur = self.addSwitch("pittsbur", dpid="0000000000000005")
        cornellt = self.addSwitch("cornellt", dpid="0000000000000006")
        northwes = self.addSwitch("northwes", dpid="0000000000000007")
        barrnet = self.addSwitch("barrnet", dpid="0000000000000008")
        sandiego = self.addSwitch("sandiego", dpid="0000000000000009")
        westnet = self.addSwitch("westnet", dpid="000000000000000a")
        ncarbou = self.addSwitch("ncarbou", dpid="000000000000000b")
        midnetl = self.addSwitch("midnetl", dpid="000000000000000c")
        ncsauni = self.addSwitch("ncsauni", dpid="000000000000000d")
        merituni = self.addSwitch("merituni", dpid="000000000000000e")

        # Adding Links
        self.addLink(seqsuine, suranet)
        self.addLink(seqsuine, ncsauni)
        self.addLink(seqsuine, sandiego)
        self.addLink(jonvonne, suranet)
        self.addLink(jonvonne, cornellt)
        self.addLink(pittsbur, merituni)
        self.addLink(cornellt, merituni)
        self.addLink(northwes, ncarbou)
        self.addLink(northwes, barrnet)
        self.addLink(barrnet, merituni)
        self.addLink(barrnet, sandiego)
        self.addLink(westnet, ncarbou)
        self.addLink(ncarbou, ncsauni)
        self.addLink(midnetl, ncsauni)
        self.addLink(ncsauni, merituni)


topos = {"Nsfnet": (lambda: Nsfnet())}

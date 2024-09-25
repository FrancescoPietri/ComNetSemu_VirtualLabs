#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Getnet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        seattle = self.addSwitch("seattle", dpid="0000000000000002")
        santacla = self.addSwitch("santacla", dpid="0000000000000003")
        phoenix = self.addSwitch("phoenix", dpid="0000000000000004")
        tucson = self.addSwitch("tucson", dpid="0000000000000005")
        washingt = self.addSwitch("washingt", dpid="0000000000000006")
        baltimor = self.addSwitch("baltimor", dpid="0000000000000007")
        pittsbur = self.addSwitch("pittsbur", dpid="0000000000000008")

        # Adding Links
        self.addLink(seattle, santacla)
        self.addLink(santacla, phoenix)
        self.addLink(santacla, washingt)
        self.addLink(santacla, pittsbur)
        self.addLink(phoenix, tucson)
        self.addLink(phoenix, washingt)
        self.addLink(washingt, baltimor)
        self.addLink(baltimor, pittsbur)


topos = {"Getnet": (lambda: Getnet())}

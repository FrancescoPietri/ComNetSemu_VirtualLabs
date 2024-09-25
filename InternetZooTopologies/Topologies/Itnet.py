#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Itnet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        limerick = self.addSwitch("limerick", dpid="0000000000000002")
        cork = self.addSwitch("cork", dpid="0000000000000003")
        tralee = self.addSwitch("tralee", dpid="0000000000000004")
        galway = self.addSwitch("galway", dpid="0000000000000005")
        sligo = self.addSwitch("sligo", dpid="0000000000000006")
        letterke = self.addSwitch("letterke", dpid="0000000000000007")
        athlone = self.addSwitch("athlone", dpid="0000000000000008")
        dundalk = self.addSwitch("dundalk", dpid="0000000000000009")
        blanchar = self.addSwitch("blanchar", dpid="000000000000000a")
        carlow = self.addSwitch("carlow", dpid="000000000000000b")
        waterfor = self.addSwitch("waterfor", dpid="000000000000000c")

        # Adding Links
        self.addLink(limerick, blanchar)
        self.addLink(cork, blanchar)
        self.addLink(tralee, blanchar)
        self.addLink(galway, blanchar)
        self.addLink(sligo, blanchar)
        self.addLink(letterke, blanchar)
        self.addLink(athlone, blanchar)
        self.addLink(dundalk, blanchar)
        self.addLink(blanchar, carlow)
        self.addLink(blanchar, waterfor)


topos = {"Itnet": (lambda: Itnet())}

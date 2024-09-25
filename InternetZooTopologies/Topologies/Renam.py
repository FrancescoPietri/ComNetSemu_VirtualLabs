#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Renam(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        chisinau = self.addSwitch("chisinau", dpid="0000000000000002")
        balti = self.addSwitch("balti", dpid="0000000000000003")
        cahul = self.addSwitch("cahul", dpid="0000000000000004")
        starneti = self.addSwitch("starneti", dpid="0000000000000005")
        roedunet = self.addSwitch("roedunet", dpid="0000000000000006")

        # Adding Links
        self.addLink(chisinau, balti)
        self.addLink(chisinau, cahul)
        self.addLink(chisinau, starneti)
        self.addLink(chisinau, roedunet)


topos = {"Renam": (lambda: Renam())}

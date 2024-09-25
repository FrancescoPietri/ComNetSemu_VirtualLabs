#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Basnet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        grodno = self.addSwitch("grodno", dpid="0000000000000002")
        minsk = self.addSwitch("minsk", dpid="0000000000000003")
        vitebsk = self.addSwitch("vitebsk", dpid="0000000000000004")
        mogilev = self.addSwitch("mogilev", dpid="0000000000000005")
        gomel = self.addSwitch("gomel", dpid="0000000000000006")
        brest = self.addSwitch("brest", dpid="0000000000000007")
        pionierg2 = self.addSwitch("pionierg2", dpid="0000000000000008")

        # Adding Links
        self.addLink(grodno, minsk)
        self.addLink(minsk, vitebsk)
        self.addLink(minsk, mogilev)
        self.addLink(minsk, gomel)
        self.addLink(minsk, brest)
        self.addLink(minsk, pionierg2)


topos = {"Basnet": (lambda: Basnet())}

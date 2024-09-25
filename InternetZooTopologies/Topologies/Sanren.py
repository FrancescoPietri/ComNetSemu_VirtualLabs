#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Sanren(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        johannes = self.addSwitch("johannes", dpid="0000000000000002")
        pretoria = self.addSwitch("pretoria", dpid="0000000000000003")
        durban = self.addSwitch("durban", dpid="0000000000000004")
        bloemfon = self.addSwitch("bloemfon", dpid="0000000000000005")
        eastlond = self.addSwitch("eastlond", dpid="0000000000000006")
        porteliz = self.addSwitch("porteliz", dpid="0000000000000007")
        capetown = self.addSwitch("capetown", dpid="0000000000000008")

        # Adding Links
        self.addLink(johannes, pretoria)
        self.addLink(johannes, bloemfon)
        self.addLink(pretoria, durban)
        self.addLink(durban, eastlond)
        self.addLink(bloemfon, capetown)
        self.addLink(eastlond, porteliz)
        self.addLink(porteliz, capetown)


topos = {"Sanren": (lambda: Sanren())}

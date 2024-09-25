#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Mren(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        bijelopo = self.addSwitch("bijelopo", dpid="0000000000000002")
        niksic = self.addSwitch("niksic", dpid="0000000000000003")
        podgoric = self.addSwitch("podgoric", dpid="0000000000000004")
        njegusi = self.addSwitch("njegusi", dpid="0000000000000005")
        kotor = self.addSwitch("kotor", dpid="0000000000000006")
        hercegno = self.addSwitch("hercegno", dpid="0000000000000007")

        # Adding Links
        self.addLink(bijelopo, podgoric)
        self.addLink(niksic, podgoric)
        self.addLink(podgoric, njegusi)
        self.addLink(podgoric, kotor)
        self.addLink(podgoric, hercegno)


topos = {"Mren": (lambda: Mren())}

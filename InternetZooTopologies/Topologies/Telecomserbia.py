#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Telecomserbia(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        novisad = self.addSwitch("novisad", dpid="0000000000000002")
        belgrade = self.addSwitch("belgrade", dpid="0000000000000003")
        kragujev = self.addSwitch("kragujev", dpid="0000000000000004")
        nis = self.addSwitch("nis", dpid="0000000000000005")
        krusevac = self.addSwitch("krusevac", dpid="0000000000000006")
        podgoric = self.addSwitch("podgoric", dpid="0000000000000007")

        # Adding Links
        self.addLink(novisad, belgrade)
        self.addLink(novisad, podgoric)
        self.addLink(belgrade, kragujev)
        self.addLink(kragujev, nis)
        self.addLink(nis, krusevac)
        self.addLink(krusevac, podgoric)


topos = {"Telecomserbia": (lambda: Telecomserbia())}

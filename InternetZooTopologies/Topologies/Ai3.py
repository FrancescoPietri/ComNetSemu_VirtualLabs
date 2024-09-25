#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Ai3(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        unibraw = self.addSwitch("unibraw", dpid="0000000000000002")
        naist = self.addSwitch("naist", dpid="0000000000000003")
        keio = self.addSwitch("keio", dpid="0000000000000004")
        ioit = self.addSwitch("ioit", dpid="0000000000000005")
        asti = self.addSwitch("asti", dpid="0000000000000006")
        tu = self.addSwitch("tu", dpid="0000000000000007")
        ait = self.addSwitch("ait", dpid="0000000000000008")
        itb = self.addSwitch("itb", dpid="0000000000000009")
        tp = self.addSwitch("tp", dpid="000000000000000a")
        usm = self.addSwitch("usm", dpid="000000000000000b")

        # Adding Links
        self.addLink(unibraw, itb)
        self.addLink(naist, keio)
        self.addLink(keio, ioit)
        self.addLink(keio, asti)
        self.addLink(keio, ait)
        self.addLink(keio, itb)
        self.addLink(keio, tp)
        self.addLink(keio, usm)
        self.addLink(tu, ait)


topos = {"Ai3": (lambda: Ai3())}

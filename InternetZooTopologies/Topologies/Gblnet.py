#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Gblnet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        newyork = self.addSwitch("newyork", dpid="0000000000000002")
        london = self.addSwitch("london", dpid="0000000000000003")
        stockhol = self.addSwitch("stockhol", dpid="0000000000000004")
        stpeters = self.addSwitch("stpeters", dpid="0000000000000005")
        moscow = self.addSwitch("moscow", dpid="0000000000000006")
        amsterda = self.addSwitch("amsterda", dpid="0000000000000007")
        frankfur = self.addSwitch("frankfur", dpid="0000000000000008")
        paris = self.addSwitch("paris", dpid="0000000000000009")

        # Adding Links
        self.addLink(newyork, amsterda)
        self.addLink(london, amsterda)
        self.addLink(stockhol, stpeters)
        self.addLink(stockhol, amsterda)
        self.addLink(stpeters, moscow)
        self.addLink(amsterda, frankfur)
        self.addLink(amsterda, paris)


topos = {"Gblnet": (lambda: Gblnet())}

#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Navigata(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        newyork = self.addSwitch("newyork", dpid="0000000000000002")
        montreal = self.addSwitch("montreal", dpid="0000000000000003")
        halifax = self.addSwitch("halifax", dpid="0000000000000004")
        losangel = self.addSwitch("losangel", dpid="0000000000000005")
        toronto = self.addSwitch("toronto", dpid="0000000000000006")
        vancouve = self.addSwitch("vancouve", dpid="0000000000000007")
        victoria = self.addSwitch("victoria", dpid="0000000000000008")
        seattle = self.addSwitch("seattle", dpid="0000000000000009")
        calgary = self.addSwitch("calgary", dpid="000000000000000a")
        edmonton = self.addSwitch("edmonton", dpid="000000000000000b")
        saskatoo = self.addSwitch("saskatoo", dpid="000000000000000c")
        regina = self.addSwitch("regina", dpid="000000000000000d")
        winnipeg = self.addSwitch("winnipeg", dpid="000000000000000e")

        # Adding Links
        self.addLink(newyork, toronto)
        self.addLink(montreal, toronto)
        self.addLink(halifax, toronto)
        self.addLink(losangel, vancouve)
        self.addLink(toronto, regina)
        self.addLink(toronto, saskatoo)
        self.addLink(vancouve, victoria)
        self.addLink(vancouve, seattle)
        self.addLink(vancouve, calgary)
        self.addLink(vancouve, edmonton)
        self.addLink(vancouve, saskatoo)
        self.addLink(vancouve, regina)
        self.addLink(calgary, edmonton)
        self.addLink(calgary, saskatoo)
        self.addLink(calgary, regina)
        self.addLink(saskatoo, winnipeg)
        self.addLink(regina, winnipeg)


topos = {"Navigata": (lambda: Navigata())}

#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Ibm(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        montreal = self.addSwitch("montreal", dpid="0000000000000002")
        whitepla = self.addSwitch("whitepla", dpid="0000000000000003")
        detroit = self.addSwitch("detroit", dpid="0000000000000004")
        toronto = self.addSwitch("toronto", dpid="0000000000000005")
        columbus = self.addSwitch("columbus", dpid="0000000000000006")
        bethesda = self.addSwitch("bethesda", dpid="0000000000000007")
        newyork = self.addSwitch("newyork", dpid="0000000000000008")
        philadel = self.addSwitch("philadel", dpid="0000000000000009")
        schaumbu = self.addSwitch("schaumbu", dpid="000000000000000a")
        stlouis = self.addSwitch("stlouis", dpid="000000000000000b")
        vancouve = self.addSwitch("vancouve", dpid="000000000000000c")
        sanfranc = self.addSwitch("sanfranc", dpid="000000000000000d")
        losangel = self.addSwitch("losangel", dpid="000000000000000e")
        phoenix = self.addSwitch("phoenix", dpid="000000000000000f")
        dallas = self.addSwitch("dallas", dpid="0000000000000010")
        atlanta = self.addSwitch("atlanta", dpid="0000000000000011")
        tampa = self.addSwitch("tampa", dpid="0000000000000012")
        chicago = self.addSwitch("chicago", dpid="0000000000000013")

        # Adding Links
        self.addLink(montreal, toronto)
        self.addLink(montreal, philadel)
        self.addLink(whitepla, chicago)
        self.addLink(whitepla, bethesda)
        self.addLink(whitepla, newyork)
        self.addLink(detroit, stlouis)
        self.addLink(detroit, toronto)
        self.addLink(detroit, columbus)
        self.addLink(columbus, schaumbu)
        self.addLink(columbus, bethesda)
        self.addLink(columbus, newyork)
        self.addLink(bethesda, atlanta)
        self.addLink(newyork, tampa)
        self.addLink(newyork, philadel)
        self.addLink(schaumbu, losangel)
        self.addLink(stlouis, chicago)
        self.addLink(vancouve, sanfranc)
        self.addLink(sanfranc, chicago)
        self.addLink(sanfranc, losangel)
        self.addLink(losangel, phoenix)
        self.addLink(phoenix, dallas)
        self.addLink(dallas, chicago)
        self.addLink(dallas, atlanta)
        self.addLink(atlanta, tampa)


topos = {"Ibm": (lambda: Ibm())}

#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class HostwayInternational(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        seattle = self.addSwitch("seattle", dpid="0000000000000002")
        tampa = self.addSwitch("tampa", dpid="0000000000000003")
        chicago = self.addSwitch("chicago", dpid="0000000000000004")
        vancouve = self.addSwitch("vancouve", dpid="0000000000000005")
        miami = self.addSwitch("miami", dpid="0000000000000006")
        austin = self.addSwitch("austin", dpid="0000000000000007")
        newyork = self.addSwitch("newyork", dpid="0000000000000008")
        atlanta = self.addSwitch("atlanta", dpid="0000000000000009")
        buchares = self.addSwitch("buchares", dpid="000000000000000a")
        seoul = self.addSwitch("seoul", dpid="000000000000000b")
        sydney = self.addSwitch("sydney", dpid="000000000000000c")
        hannover = self.addSwitch("hannover", dpid="000000000000000d")
        amsterda = self.addSwitch("amsterda", dpid="000000000000000e")
        antwerp = self.addSwitch("antwerp", dpid="000000000000000f")
        frankfur = self.addSwitch("frankfur", dpid="0000000000000010")
        london = self.addSwitch("london", dpid="0000000000000011")

        # Adding Links
        self.addLink(seattle, chicago)
        self.addLink(seattle, vancouve)
        self.addLink(seattle, austin)
        self.addLink(tampa, miami)
        self.addLink(tampa, atlanta)
        self.addLink(chicago, austin)
        self.addLink(chicago, atlanta)
        self.addLink(miami, sydney)
        self.addLink(miami, newyork)
        self.addLink(miami, atlanta)
        self.addLink(newyork, sydney)
        self.addLink(newyork, atlanta)
        self.addLink(newyork, london)
        self.addLink(buchares, seoul)
        self.addLink(buchares, frankfur)
        self.addLink(seoul, sydney)
        self.addLink(hannover, amsterda)
        self.addLink(hannover, frankfur)
        self.addLink(amsterda, antwerp)
        self.addLink(amsterda, london)
        self.addLink(antwerp, frankfur)


topos = {"HostwayInternational": (lambda: HostwayInternational())}

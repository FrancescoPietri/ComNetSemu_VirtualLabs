#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Claranet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        faro = self.addSwitch("faro", dpid="0000000000000002")
        madrid = self.addSwitch("madrid", dpid="0000000000000003")
        porto = self.addSwitch("porto", dpid="0000000000000004")
        lisbon = self.addSwitch("lisbon", dpid="0000000000000005")
        barcelon = self.addSwitch("barcelon", dpid="0000000000000006")
        manchest = self.addSwitch("manchest", dpid="0000000000000007")
        newyork = self.addSwitch("newyork", dpid="0000000000000008")
        amsterda = self.addSwitch("amsterda", dpid="0000000000000009")
        eindhove = self.addSwitch("eindhove", dpid="000000000000000a")
        berlin = self.addSwitch("berlin", dpid="000000000000000b")
        frankfur = self.addSwitch("frankfur", dpid="000000000000000c")
        munich = self.addSwitch("munich", dpid="000000000000000d")
        paris = self.addSwitch("paris", dpid="000000000000000e")
        rennes = self.addSwitch("rennes", dpid="000000000000000f")
        london = self.addSwitch("london", dpid="0000000000000010")

        # Adding Links
        self.addLink(faro, lisbon)
        self.addLink(madrid, lisbon)
        self.addLink(madrid, barcelon)
        self.addLink(porto, lisbon)
        self.addLink(lisbon, london)
        self.addLink(barcelon, paris)
        self.addLink(manchest, london)
        self.addLink(newyork, london)
        self.addLink(amsterda, eindhove)
        self.addLink(amsterda, frankfur)
        self.addLink(amsterda, london)
        self.addLink(berlin, frankfur)
        self.addLink(berlin, munich)
        self.addLink(frankfur, munich)
        self.addLink(frankfur, paris)
        self.addLink(frankfur, london)
        self.addLink(paris, rennes)
        self.addLink(paris, london)


topos = {"Claranet": (lambda: Claranet())}

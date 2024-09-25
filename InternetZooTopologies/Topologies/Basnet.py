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
        s0 = self.addSwitch("grodno0", dpid="0000000000000002")
        s1 = self.addSwitch("minsk1", dpid="0000000000000003")
        s2 = self.addSwitch("vitebsk2", dpid="0000000000000004")
        s3 = self.addSwitch("mogilev3", dpid="0000000000000005")
        s4 = self.addSwitch("gomel4", dpid="0000000000000006")
        s5 = self.addSwitch("brest5", dpid="0000000000000007")
        s6 = self.addSwitch("pionierg6", dpid="0000000000000008")

        # Adding Links
        self.addLink(s0, s1)
        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s1, s4)
        self.addLink(s1, s5)
        self.addLink(s1, s6)


topos = {"Basnet": (lambda: Basnet())}

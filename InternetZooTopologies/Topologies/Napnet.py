#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Napnet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("seattle0", dpid="0000000000000002")
        s1 = self.addSwitch("sanjose11", dpid="0000000000000003")
        s2 = self.addSwitch("minneapo2", dpid="0000000000000004")
        s3 = self.addSwitch("chicago3", dpid="0000000000000005")
        s4 = self.addSwitch("vienna4", dpid="0000000000000006")
        s5 = self.addSwitch("dallas5", dpid="0000000000000007")

        # Adding Links
        self.addLink(s0, s1)
        self.addLink(s0, s3)
        self.addLink(s1, s3)
        self.addLink(s1, s4)
        self.addLink(s2, s3)
        self.addLink(s3, s4)
        self.addLink(s3, s5)


topos = {"Napnet": (lambda: Napnet())}

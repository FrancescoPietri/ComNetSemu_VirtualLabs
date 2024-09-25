#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Marnet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        fofmini = self.addSwitch("fofmini", dpid="0000000000000002")
        onnetneo = self.addSwitch("onnetneo", dpid="0000000000000003")
        nocandca = self.addSwitch("nocandca", dpid="0000000000000004")
        iofecon = self.addSwitch("iofecon", dpid="0000000000000005")
        national = self.addSwitch("national", dpid="0000000000000006")
        iofpolit = self.addSwitch("iofpolit", dpid="0000000000000007")
        geantsee = self.addSwitch("geantsee", dpid="0000000000000008")
        campusna = self.addSwitch("campusna", dpid="0000000000000009")
        fofpeda = self.addSwitch("fofpeda", dpid="000000000000000a")
        mol = self.addSwitch("mol", dpid="000000000000000b")
        national = self.addSwitch("national", dpid="000000000000000c")
        iofeart = self.addSwitch("iofeart", dpid="000000000000000d")
        iofnati = self.addSwitch("iofnati", dpid="000000000000000e")
        iofmace = self.addSwitch("iofmace", dpid="000000000000000f")
        stclemen = self.addSwitch("stclemen", dpid="0000000000000010")
        severalm = self.addSwitch("severalm", dpid="0000000000000011")
        campusar = self.addSwitch("campusar", dpid="0000000000000012")
        campuste = self.addSwitch("campuste", dpid="0000000000000013")
        campusme = self.addSwitch("campusme", dpid="0000000000000014")
        campusbi = self.addSwitch("campusbi", dpid="0000000000000015")

        # Adding Links
        self.addLink(fofmini, nocandca)
        self.addLink(onnetneo, national)
        self.addLink(nocandca, iofecon)
        self.addLink(nocandca, national)
        self.addLink(nocandca, iofpolit)
        self.addLink(nocandca, geantsee)
        self.addLink(nocandca, campusna)
        self.addLink(nocandca, mol)
        self.addLink(nocandca, national)
        self.addLink(nocandca, iofeart)
        self.addLink(nocandca, iofnati)
        self.addLink(nocandca, iofmace)
        self.addLink(nocandca, stclemen)
        self.addLink(nocandca, severalm)
        self.addLink(nocandca, campusar)
        self.addLink(nocandca, campuste)
        self.addLink(nocandca, campusme)
        self.addLink(nocandca, campusbi)
        self.addLink(national, campusna)
        self.addLink(national, national)
        self.addLink(national, iofeart)
        self.addLink(national, campusar)
        self.addLink(national, campuste)
        self.addLink(national, campusme)
        self.addLink(national, campusbi)
        self.addLink(iofpolit, campuste)
        self.addLink(fofpeda, campuste)


topos = {"Marnet": (lambda: Marnet())}

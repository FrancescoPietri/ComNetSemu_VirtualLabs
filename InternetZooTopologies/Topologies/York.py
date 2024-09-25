#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class York(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        leiceste = self.addSwitch("leiceste", dpid="0000000000000002")
        northamp = self.addSwitch("northamp", dpid="0000000000000003")
        sheffiel = self.addSwitch("sheffiel", dpid="0000000000000004")
        nottingh = self.addSwitch("nottingh", dpid="0000000000000005")
        croydon = self.addSwitch("croydon", dpid="0000000000000006")
        slough = self.addSwitch("slough", dpid="0000000000000007")
        miltonke = self.addSwitch("miltonke", dpid="0000000000000008")
        london = self.addSwitch("london", dpid="0000000000000009")
        reading = self.addSwitch("reading", dpid="000000000000000a")
        banbury = self.addSwitch("banbury", dpid="000000000000000b")
        brighton = self.addSwitch("brighton", dpid="000000000000000c")
        bristol = self.addSwitch("bristol", dpid="000000000000000d")
        birmingh = self.addSwitch("birmingh", dpid="000000000000000e")
        preston = self.addSwitch("preston", dpid="000000000000000f")
        manchest = self.addSwitch("manchest", dpid="0000000000000010")
        glasgow = self.addSwitch("glasgow", dpid="0000000000000011")
        edinburg = self.addSwitch("edinburg", dpid="0000000000000012")
        newcastl = self.addSwitch("newcastl", dpid="0000000000000013")
        middlesb = self.addSwitch("middlesb", dpid="0000000000000014")
        harrogat = self.addSwitch("harrogat", dpid="0000000000000015")
        york = self.addSwitch("york", dpid="0000000000000016")
        leeds = self.addSwitch("leeds", dpid="0000000000000017")
        carlisle = self.addSwitch("carlisle", dpid="0000000000000018")

        # Adding Links
        self.addLink(leiceste, northamp)
        self.addLink(leiceste, nottingh)
        self.addLink(northamp, miltonke)
        self.addLink(sheffiel, nottingh)
        self.addLink(sheffiel, leeds)
        self.addLink(croydon, london)
        self.addLink(slough, reading)
        self.addLink(slough, london)
        self.addLink(miltonke, london)
        self.addLink(reading, banbury)
        self.addLink(reading, brighton)
        self.addLink(reading, bristol)
        self.addLink(banbury, birmingh)
        self.addLink(birmingh, manchest)
        self.addLink(preston, manchest)
        self.addLink(preston, carlisle)
        self.addLink(glasgow, edinburg)
        self.addLink(glasgow, carlisle)
        self.addLink(edinburg, newcastl)
        self.addLink(newcastl, middlesb)
        self.addLink(middlesb, york)
        self.addLink(harrogat, york)
        self.addLink(harrogat, leeds)
        self.addLink(york, leeds)


topos = {"York": (lambda: York())}

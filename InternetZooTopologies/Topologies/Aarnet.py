#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Aarnet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        sydney1 = self.addSwitch("sydney1", dpid="0000000000000002")
        brisbane2 = self.addSwitch("brisbane2", dpid="0000000000000003")
        canberra1 = self.addSwitch("canberra1", dpid="0000000000000004")
        sydney2 = self.addSwitch("sydney2", dpid="0000000000000005")
        townsvil = self.addSwitch("townsvil", dpid="0000000000000006")
        cairns = self.addSwitch("cairns", dpid="0000000000000007")
        brisbane1 = self.addSwitch("brisbane1", dpid="0000000000000008")
        rockhamp = self.addSwitch("rockhamp", dpid="0000000000000009")
        armidale = self.addSwitch("armidale", dpid="000000000000000a")
        hobart = self.addSwitch("hobart", dpid="000000000000000b")
        canberra2 = self.addSwitch("canberra2", dpid="000000000000000c")
        perth1 = self.addSwitch("perth1", dpid="000000000000000d")
        perth2 = self.addSwitch("perth2", dpid="000000000000000e")
        adelaide1 = self.addSwitch("adelaide1", dpid="000000000000000f")
        adelaide2 = self.addSwitch("adelaide2", dpid="0000000000000010")
        melbourn1 = self.addSwitch("melbourn1", dpid="0000000000000011")
        melbourn2 = self.addSwitch("melbourn2", dpid="0000000000000012")
        alicespr = self.addSwitch("alicespr", dpid="0000000000000013")
        darwin = self.addSwitch("darwin", dpid="0000000000000014")

        # Adding Links
        self.addLink(sydney1, canberra2)
        self.addLink(sydney1, sydney2)
        self.addLink(sydney1, brisbane1)
        self.addLink(brisbane2, sydney2)
        self.addLink(brisbane2, brisbane1)
        self.addLink(canberra1, canberra2)
        self.addLink(canberra1, melbourn1)
        self.addLink(sydney2, armidale)
        self.addLink(sydney2, melbourn2)
        self.addLink(townsvil, cairns)
        self.addLink(townsvil, rockhamp)
        self.addLink(brisbane1, rockhamp)
        self.addLink(hobart, melbourn2)
        self.addLink(hobart, melbourn1)
        self.addLink(perth1, perth2)
        self.addLink(perth1, adelaide1)
        self.addLink(perth2, adelaide2)
        self.addLink(adelaide1, darwin)
        self.addLink(adelaide1, adelaide2)
        self.addLink(adelaide1, melbourn1)
        self.addLink(adelaide2, melbourn2)
        self.addLink(adelaide2, alicespr)
        self.addLink(melbourn1, melbourn2)
        self.addLink(alicespr, darwin)


topos = {"Aarnet": (lambda: Aarnet())}

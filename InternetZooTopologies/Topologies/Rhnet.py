#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Rhnet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        solborg = self.addSwitch("solborg", dpid="0000000000000002")
        fjarski = self.addSwitch("fjarski", dpid="0000000000000003")
        fsaakur = self.addSwitch("fsaakur", dpid="0000000000000004")
        dstakur = self.addSwitch("dstakur", dpid="0000000000000005")
        rix = self.addSwitch("rix", dpid="0000000000000006")
        nordunet = self.addSwitch("nordunet", dpid="0000000000000007")
        hvanneyr = self.addSwitch("hvanneyr", dpid="0000000000000008")
        bifrost = self.addSwitch("bifrost", dpid="0000000000000009")
        grensas = self.addSwitch("grensas", dpid="000000000000000a")
        skulagat = self.addSwitch("skulagat", dpid="000000000000000b")
        taekniga = self.addSwitch("taekniga", dpid="000000000000000c")
        sturluga = self.addSwitch("sturluga", dpid="000000000000000d")
        hringbra = self.addSwitch("hringbra", dpid="000000000000000e")
        bustaoav = self.addSwitch("bustaoav", dpid="000000000000000f")
        ofanleit = self.addSwitch("ofanleit", dpid="0000000000000010")
        keldhaho = self.addSwitch("keldhaho", dpid="0000000000000011")

        # Adding Links
        self.addLink(solborg, fsaakur)
        self.addLink(solborg, dstakur)
        self.addLink(fjarski, taekniga)
        self.addLink(fjarski, dstakur)
        self.addLink(fsaakur, dstakur)
        self.addLink(rix, taekniga)
        self.addLink(nordunet, taekniga)
        self.addLink(nordunet, sturluga)
        self.addLink(hvanneyr, bifrost)
        self.addLink(hvanneyr, keldhaho)
        self.addLink(grensas, skulagat)
        self.addLink(grensas, keldhaho)
        self.addLink(skulagat, taekniga)
        self.addLink(taekniga, sturluga)
        self.addLink(sturluga, hringbra)
        self.addLink(hringbra, bustaoav)
        self.addLink(bustaoav, ofanleit)
        self.addLink(ofanleit, keldhaho)


topos = {"Rhnet": (lambda: Rhnet())}

#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Restena(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        walferda = self.addSwitch("walferda", dpid="0000000000000002")
        ccrn = self.addSwitch("ccrn", dpid="0000000000000003")
        ettelbru = self.addSwitch("ettelbru", dpid="0000000000000004")
        diekirch = self.addSwitch("diekirch", dpid="0000000000000005")
        geantpar = self.addSwitch("geantpar", dpid="0000000000000006")
        internet = self.addSwitch("internet", dpid="0000000000000007")
        adslvia = self.addSwitch("adslvia", dpid="0000000000000008")
        france = self.addSwitch("france", dpid="0000000000000009")
        geantfra = self.addSwitch("geantfra", dpid="000000000000000a")
        restena = self.addSwitch("restena", dpid="000000000000000b")
        bce = self.addSwitch("bce", dpid="000000000000000c")
        adslvia = self.addSwitch("adslvia", dpid="000000000000000d")
        uniiu = self.addSwitch("uniiu", dpid="000000000000000e")
        rollinge = self.addSwitch("rollinge", dpid="000000000000000f")
        campusge = self.addSwitch("campusge", dpid="0000000000000010")
        eschsur = self.addSwitch("eschsur", dpid="0000000000000011")
        bettembo = self.addSwitch("bettembo", dpid="0000000000000012")
        luxembou = self.addSwitch("luxembou", dpid="0000000000000013")
        limperts = self.addSwitch("limperts", dpid="0000000000000014")

        # Adding Links
        self.addLink(walferda, restena)
        self.addLink(ccrn, restena)
        self.addLink(ettelbru, bce)
        self.addLink(ettelbru, diekirch)
        self.addLink(diekirch, restena)
        self.addLink(geantpar, bce)
        self.addLink(internet, bce)
        self.addLink(adslvia, restena)
        self.addLink(france, eschsur)
        self.addLink(geantfra, bce)
        self.addLink(restena, bce)
        self.addLink(restena, bettembo)
        self.addLink(restena, luxembou)
        self.addLink(bce, adslvia)
        self.addLink(bce, limperts)
        self.addLink(uniiu, limperts)
        self.addLink(uniiu, campusge)
        self.addLink(rollinge, campusge)
        self.addLink(campusge, luxembou)
        self.addLink(campusge, eschsur)
        self.addLink(eschsur, bettembo)


topos = {"Restena": (lambda: Restena())}

#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Noel(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        spokane = self.addSwitch("spokane", dpid="0000000000000002")
        coeurda = self.addSwitch("coeurda", dpid="0000000000000003")
        wenatche = self.addSwitch("wenatche", dpid="0000000000000004")
        othello = self.addSwitch("othello", dpid="0000000000000005")
        wallawal = self.addSwitch("wallawal", dpid="0000000000000006")
        pasco = self.addSwitch("pasco", dpid="0000000000000007")
        pullman = self.addSwitch("pullman", dpid="0000000000000008")
        lewiston = self.addSwitch("lewiston", dpid="0000000000000009")
        kennewic = self.addSwitch("kennewic", dpid="000000000000000a")
        yakima = self.addSwitch("yakima", dpid="000000000000000b")
        ellensbu = self.addSwitch("ellensbu", dpid="000000000000000c")
        vancouve = self.addSwitch("vancouve", dpid="000000000000000d")
        bellingh = self.addSwitch("bellingh", dpid="000000000000000e")
        mtvernon = self.addSwitch("mtvernon", dpid="000000000000000f")
        everett = self.addSwitch("everett", dpid="0000000000000010")
        westins = self.addSwitch("westins", dpid="0000000000000011")
        tacoma = self.addSwitch("tacoma", dpid="0000000000000012")
        olympia = self.addSwitch("olympia", dpid="0000000000000013")
        portland = self.addSwitch("portland", dpid="0000000000000014")

        # Adding Links
        self.addLink(spokane, coeurda)
        self.addLink(spokane, wenatche)
        self.addLink(spokane, othello)
        self.addLink(spokane, pullman)
        self.addLink(wenatche, ellensbu)
        self.addLink(wenatche, westins)
        self.addLink(othello, yakima)
        self.addLink(wallawal, kennewic)
        self.addLink(wallawal, pasco)
        self.addLink(pasco, kennewic)
        self.addLink(pasco, yakima)
        self.addLink(pullman, lewiston)
        self.addLink(kennewic, yakima)
        self.addLink(kennewic, portland)
        self.addLink(yakima, ellensbu)
        self.addLink(yakima, westins)
        self.addLink(vancouve, bellingh)
        self.addLink(vancouve, westins)
        self.addLink(bellingh, mtvernon)
        self.addLink(mtvernon, everett)
        self.addLink(everett, westins)
        self.addLink(westins, tacoma)
        self.addLink(westins, portland)
        self.addLink(tacoma, olympia)
        self.addLink(olympia, portland)


topos = {"Noel": (lambda: Noel())}

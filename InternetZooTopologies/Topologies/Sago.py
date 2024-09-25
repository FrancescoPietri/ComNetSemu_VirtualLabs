#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Sago(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        ftpierc = self.addSwitch("ftpierc", dpid="0000000000000002")
        melbourn = self.addSwitch("melbourn", dpid="0000000000000003")
        lakealfr = self.addSwitch("lakealfr", dpid="0000000000000004")
        orlando = self.addSwitch("orlando", dpid="0000000000000005")
        westpalm = self.addSwitch("westpalm", dpid="0000000000000006")
        tampa = self.addSwitch("tampa", dpid="0000000000000007")
        miami = self.addSwitch("miami", dpid="0000000000000008")
        ftlaude = self.addSwitch("ftlaude", dpid="0000000000000009")
        flovilla = self.addSwitch("flovilla", dpid="000000000000000a")
        atlanta = self.addSwitch("atlanta", dpid="000000000000000b")
        tarrytow = self.addSwitch("tarrytow", dpid="000000000000000c")
        gordon = self.addSwitch("gordon", dpid="000000000000000d")
        newell = self.addSwitch("newell", dpid="000000000000000e")
        surrency = self.addSwitch("surrency", dpid="000000000000000f")
        staugus = self.addSwitch("staugus", dpid="0000000000000010")
        jacksonv = self.addSwitch("jacksonv", dpid="0000000000000011")
        titusvil = self.addSwitch("titusvil", dpid="0000000000000012")
        daytonab = self.addSwitch("daytonab", dpid="0000000000000013")

        # Adding Links
        self.addLink(ftpierc, melbourn)
        self.addLink(ftpierc, westpalm)
        self.addLink(melbourn, titusvil)
        self.addLink(lakealfr, orlando)
        self.addLink(lakealfr, tampa)
        self.addLink(orlando, daytonab)
        self.addLink(westpalm, ftlaude)
        self.addLink(miami, ftlaude)
        self.addLink(flovilla, atlanta)
        self.addLink(flovilla, gordon)
        self.addLink(tarrytow, gordon)
        self.addLink(tarrytow, surrency)
        self.addLink(newell, surrency)
        self.addLink(newell, jacksonv)
        self.addLink(staugus, daytonab)
        self.addLink(staugus, jacksonv)
        self.addLink(titusvil, daytonab)


topos = {"Sago": (lambda: Sago())}

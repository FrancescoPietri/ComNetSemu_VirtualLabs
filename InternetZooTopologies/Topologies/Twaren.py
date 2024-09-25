#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Twaren(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        ccu = self.addSwitch("ccu", dpid="0000000000000002")
        nhlue = self.addSwitch("nhlue", dpid="0000000000000003")
        tn = self.addSwitch("tn", dpid="0000000000000004")
        ncku = self.addSwitch("ncku", dpid="0000000000000005")
        tc = self.addSwitch("tc", dpid="0000000000000006")
        chi = self.addSwitch("chi", dpid="0000000000000007")
        ndhu = self.addSwitch("ndhu", dpid="0000000000000008")
        ncnu = self.addSwitch("ncnu", dpid="0000000000000009")
        la = self.addSwitch("la", dpid="000000000000000a")
        niu = self.addSwitch("niu", dpid="000000000000000b")
        nttu = self.addSwitch("nttu", dpid="000000000000000c")
        nsysu = self.addSwitch("nsysu", dpid="000000000000000d")
        nchu = self.addSwitch("nchu", dpid="000000000000000e")
        hc = self.addSwitch("hc", dpid="000000000000000f")
        nctu = self.addSwitch("nctu", dpid="0000000000000010")
        nthu = self.addSwitch("nthu", dpid="0000000000000011")
        ncu = self.addSwitch("ncu", dpid="0000000000000012")
        ascc = self.addSwitch("ascc", dpid="0000000000000013")
        ntu = self.addSwitch("ntu", dpid="0000000000000014")
        tp = self.addSwitch("tp", dpid="0000000000000015")

        # Adding Links
        self.addLink(ccu, tn)
        self.addLink(nhlue, tp)
        self.addLink(tn, ncku)
        self.addLink(tn, tc)
        self.addLink(tn, nttu)
        self.addLink(tn, nsysu)
        self.addLink(tn, hc)
        self.addLink(tc, tp)
        self.addLink(tc, nchu)
        self.addLink(tc, ncnu)
        self.addLink(chi, tp)
        self.addLink(ndhu, tp)
        self.addLink(la, hc)
        self.addLink(niu, tp)
        self.addLink(hc, nctu)
        self.addLink(hc, nthu)
        self.addLink(hc, ncu)
        self.addLink(hc, tp)
        self.addLink(ascc, tp)
        self.addLink(ntu, tp)


topos = {"Twaren": (lambda: Twaren())}

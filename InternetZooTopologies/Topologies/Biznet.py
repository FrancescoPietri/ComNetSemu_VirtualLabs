#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Biznet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        cilacap = self.addSwitch("cilacap", dpid="0000000000000002")
        purwoker = self.addSwitch("purwoker", dpid="0000000000000003")
        sukabumi = self.addSwitch("sukabumi", dpid="0000000000000004")
        tasikmal = self.addSwitch("tasikmal", dpid="0000000000000005")
        pekalong = self.addSwitch("pekalong", dpid="0000000000000006")
        semarang = self.addSwitch("semarang", dpid="0000000000000007")
        magelang = self.addSwitch("magelang", dpid="0000000000000008")
        yogyakar = self.addSwitch("yogyakar", dpid="0000000000000009")
        kudus = self.addSwitch("kudus", dpid="000000000000000a")
        surakart = self.addSwitch("surakart", dpid="000000000000000b")
        nusadua = self.addSwitch("nusadua", dpid="000000000000000c")
        surabaya = self.addSwitch("surabaya", dpid="000000000000000d")
        kediri = self.addSwitch("kediri", dpid="000000000000000e")
        madium = self.addSwitch("madium", dpid="000000000000000f")
        tuban = self.addSwitch("tuban", dpid="0000000000000010")
        banyunwa = self.addSwitch("banyunwa", dpid="0000000000000011")
        jember = self.addSwitch("jember", dpid="0000000000000012")
        probolin = self.addSwitch("probolin", dpid="0000000000000013")
        malang = self.addSwitch("malang", dpid="0000000000000014")
        bakauhun = self.addSwitch("bakauhun", dpid="0000000000000015")
        cibaliun = self.addSwitch("cibaliun", dpid="0000000000000016")
        tegal = self.addSwitch("tegal", dpid="0000000000000017")
        cirebon = self.addSwitch("cirebon", dpid="0000000000000018")
        bandung = self.addSwitch("bandung", dpid="0000000000000019")
        karawang = self.addSwitch("karawang", dpid="000000000000001a")
        jakarta = self.addSwitch("jakarta", dpid="000000000000001b")
        bogor = self.addSwitch("bogor", dpid="000000000000001c")
        serang = self.addSwitch("serang", dpid="000000000000001d")
        anyer = self.addSwitch("anyer", dpid="000000000000001e")

        # Adding Links
        self.addLink(cilacap, purwoker)
        self.addLink(cilacap, tasikmal)
        self.addLink(purwoker, magelang)
        self.addLink(sukabumi, bogor)
        self.addLink(sukabumi, bandung)
        self.addLink(tasikmal, bandung)
        self.addLink(pekalong, tegal)
        self.addLink(pekalong, semarang)
        self.addLink(semarang, kudus)
        self.addLink(semarang, surakart)
        self.addLink(magelang, yogyakar)
        self.addLink(yogyakar, surakart)
        self.addLink(kudus, tuban)
        self.addLink(surakart, madium)
        self.addLink(nusadua, banyunwa)
        self.addLink(surabaya, probolin)
        self.addLink(surabaya, kediri)
        self.addLink(surabaya, tuban)
        self.addLink(kediri, malang)
        self.addLink(kediri, madium)
        self.addLink(banyunwa, jember)
        self.addLink(jember, probolin)
        self.addLink(jember, malang)
        self.addLink(bakauhun, anyer)
        self.addLink(cibaliun, bogor)
        self.addLink(cibaliun, anyer)
        self.addLink(tegal, cirebon)
        self.addLink(cirebon, bandung)
        self.addLink(bandung, karawang)
        self.addLink(karawang, jakarta)
        self.addLink(jakarta, bogor)
        self.addLink(jakarta, serang)
        self.addLink(serang, anyer)


topos = {"Biznet": (lambda: Biznet())}

#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Forthnet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        komotini = self.addSwitch("komotini", dpid="0000000000000002")
        alexandr = self.addSwitch("alexandr", dpid="0000000000000003")
        xanthi = self.addSwitch("xanthi", dpid="0000000000000004")
        kavala = self.addSwitch("kavala", dpid="0000000000000005")
        intercon = self.addSwitch("intercon", dpid="0000000000000006")
        chios = self.addSwitch("chios", dpid="0000000000000007")
        lesbos = self.addSwitch("lesbos", dpid="0000000000000008")
        athens = self.addSwitch("athens", dpid="0000000000000009")
        zakyntho = self.addSwitch("zakyntho", dpid="000000000000000a")
        pyrgos = self.addSwitch("pyrgos", dpid="000000000000000b")
        samos = self.addSwitch("samos", dpid="000000000000000c")
        rhodes = self.addSwitch("rhodes", dpid="000000000000000d")
        agrinio = self.addSwitch("agrinio", dpid="000000000000000e")
        mesologg = self.addSwitch("mesologg", dpid="000000000000000f")
        prevezza = self.addSwitch("prevezza", dpid="0000000000000010")
        arta = self.addSwitch("arta", dpid="0000000000000011")
        lamia = self.addSwitch("lamia", dpid="0000000000000012")
        inofita = self.addSwitch("inofita", dpid="0000000000000013")
        rethymno = self.addSwitch("rethymno", dpid="0000000000000014")
        moires = self.addSwitch("moires", dpid="0000000000000015")
        agnikol = self.addSwitch("agnikol", dpid="0000000000000016")
        ierapetr = self.addSwitch("ierapetr", dpid="0000000000000017")
        siteia = self.addSwitch("siteia", dpid="0000000000000018")
        corinth = self.addSwitch("corinth", dpid="0000000000000019")
        itea = self.addSwitch("itea", dpid="000000000000001a")
        livadia = self.addSwitch("livadia", dpid="000000000000001b")
        kastoria = self.addSwitch("kastoria", dpid="000000000000001c")
        larissa = self.addSwitch("larissa", dpid="000000000000001d")
        lefkada = self.addSwitch("lefkada", dpid="000000000000001e")
        grevena = self.addSwitch("grevena", dpid="000000000000001f")
        igoumeni = self.addSwitch("igoumeni", dpid="0000000000000020")
        argostol = self.addSwitch("argostol", dpid="0000000000000021")
        internet = self.addSwitch("internet", dpid="0000000000000022")
        patra = self.addSwitch("patra", dpid="0000000000000023")
        sklathos = self.addSwitch("sklathos", dpid="0000000000000024")
        chalkida = self.addSwitch("chalkida", dpid="0000000000000025")
        karditsa = self.addSwitch("karditsa", dpid="0000000000000026")
        volos = self.addSwitch("volos", dpid="0000000000000027")
        karpenis = self.addSwitch("karpenis", dpid="0000000000000028")
        trikana = self.addSwitch("trikana", dpid="0000000000000029")
        corfu = self.addSwitch("corfu", dpid="000000000000002a")
        ioaninna = self.addSwitch("ioaninna", dpid="000000000000002b")
        hersonls = self.addSwitch("hersonls", dpid="000000000000002c")
        heraklio = self.addSwitch("heraklio", dpid="000000000000002d")
        argos = self.addSwitch("argos", dpid="000000000000002e")
        syros = self.addSwitch("syros", dpid="000000000000002f")
        mykonos = self.addSwitch("mykonos", dpid="0000000000000030")
        santorin = self.addSwitch("santorin", dpid="0000000000000031")
        chania = self.addSwitch("chania", dpid="0000000000000032")
        sparta = self.addSwitch("sparta", dpid="0000000000000033")
        kalamata = self.addSwitch("kalamata", dpid="0000000000000034")
        tripoli = self.addSwitch("tripoli", dpid="0000000000000035")
        polygyro = self.addSwitch("polygyro", dpid="0000000000000036")
        drama = self.addSwitch("drama", dpid="0000000000000037")
        serres = self.addSwitch("serres", dpid="0000000000000038")
        thessalo = self.addSwitch("thessalo", dpid="0000000000000039")
        kilkis = self.addSwitch("kilkis", dpid="000000000000003a")
        edessa = self.addSwitch("edessa", dpid="000000000000003b")
        florina = self.addSwitch("florina", dpid="000000000000003c")
        verola = self.addSwitch("verola", dpid="000000000000003d")
        kozani = self.addSwitch("kozani", dpid="000000000000003e")
        katerina = self.addSwitch("katerina", dpid="000000000000003f")

        # Adding Links
        self.addLink(komotini, thessalo)
        self.addLink(alexandr, thessalo)
        self.addLink(xanthi, kavala)
        self.addLink(kavala, drama)
        self.addLink(kavala, thessalo)
        self.addLink(intercon, athens)
        self.addLink(chios, athens)
        self.addLink(lesbos, athens)
        self.addLink(athens, internet)
        self.addLink(athens, patra)
        self.addLink(athens, chalkida)
        self.addLink(athens, ioaninna)
        self.addLink(athens, samos)
        self.addLink(athens, rhodes)
        self.addLink(athens, syros)
        self.addLink(athens, mykonos)
        self.addLink(athens, santorin)
        self.addLink(athens, lamia)
        self.addLink(athens, inofita)
        self.addLink(athens, tripoli)
        self.addLink(athens, heraklio)
        self.addLink(athens, thessalo)
        self.addLink(athens, itea)
        self.addLink(athens, livadia)
        self.addLink(athens, larissa)
        self.addLink(athens, corinth)
        self.addLink(zakyntho, patra)
        self.addLink(pyrgos, patra)
        self.addLink(agrinio, patra)
        self.addLink(mesologg, patra)
        self.addLink(prevezza, ioaninna)
        self.addLink(arta, ioaninna)
        self.addLink(rethymno, heraklio)
        self.addLink(moires, heraklio)
        self.addLink(agnikol, hersonls)
        self.addLink(agnikol, ierapetr)
        self.addLink(agnikol, siteia)
        self.addLink(kastoria, ioaninna)
        self.addLink(larissa, karditsa)
        self.addLink(larissa, volos)
        self.addLink(larissa, karpenis)
        self.addLink(larissa, trikana)
        self.addLink(lefkada, patra)
        self.addLink(grevena, ioaninna)
        self.addLink(igoumeni, ioaninna)
        self.addLink(argostol, patra)
        self.addLink(internet, thessalo)
        self.addLink(sklathos, chalkida)
        self.addLink(corfu, ioaninna)
        self.addLink(hersonls, heraklio)
        self.addLink(heraklio, chania)
        self.addLink(argos, tripoli)
        self.addLink(sparta, tripoli)
        self.addLink(kalamata, tripoli)
        self.addLink(polygyro, thessalo)
        self.addLink(serres, thessalo)
        self.addLink(thessalo, kilkis)
        self.addLink(thessalo, edessa)
        self.addLink(thessalo, florina)
        self.addLink(thessalo, verola)
        self.addLink(thessalo, kozani)
        self.addLink(thessalo, katerina)


topos = {"Forthnet": (lambda: Forthnet())}

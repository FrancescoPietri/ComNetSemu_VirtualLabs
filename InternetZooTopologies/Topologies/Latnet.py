#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Latnet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        iecava = self.addSwitch("iecava", dpid="0000000000000002")
        vircava = self.addSwitch("vircava", dpid="0000000000000003")
        kraslava = self.addSwitch("kraslava", dpid="0000000000000004")
        baldone = self.addSwitch("baldone", dpid="0000000000000005")
        auce = self.addSwitch("auce", dpid="0000000000000006")
        broceni = self.addSwitch("broceni", dpid="0000000000000007")
        platone = self.addSwitch("platone", dpid="0000000000000008")
        dobele = self.addSwitch("dobele", dpid="0000000000000009")
        krimulda = self.addSwitch("krimulda", dpid="000000000000000a")
        vijkene = self.addSwitch("vijkene", dpid="000000000000000b")
        saldus = self.addSwitch("saldus", dpid="000000000000000c")
        kapsede = self.addSwitch("kapsede", dpid="000000000000000d")
        viesite = self.addSwitch("viesite", dpid="000000000000000e")
        aizkrouk = self.addSwitch("aizkrouk", dpid="000000000000000f")
        vilani = self.addSwitch("vilani", dpid="0000000000000010")
        gulbene = self.addSwitch("gulbene", dpid="0000000000000011")
        rujiena = self.addSwitch("rujiena", dpid="0000000000000012")
        salagriv = self.addSwitch("salagriv", dpid="0000000000000013")
        aloja = self.addSwitch("aloja", dpid="0000000000000014")
        mazsalac = self.addSwitch("mazsalac", dpid="0000000000000015")
        strenci = self.addSwitch("strenci", dpid="0000000000000016")
        pociems = self.addSwitch("pociems", dpid="0000000000000017")
        limbazi = self.addSwitch("limbazi", dpid="0000000000000018")
        liepupe = self.addSwitch("liepupe", dpid="0000000000000019")
        skriveri = self.addSwitch("skriveri", dpid="000000000000001a")
        valmiera = self.addSwitch("valmiera", dpid="000000000000001b")
        rezekne = self.addSwitch("rezekne", dpid="000000000000001c")
        carnikav = self.addSwitch("carnikav", dpid="000000000000001d")
        jumprava = self.addSwitch("jumprava", dpid="000000000000001e")
        kegums = self.addSwitch("kegums", dpid="000000000000001f")
        riga = self.addSwitch("riga", dpid="0000000000000020")
        daugapil = self.addSwitch("daugapil", dpid="0000000000000021")
        ventspit = self.addSwitch("ventspit", dpid="0000000000000022")
        grobina = self.addSwitch("grobina", dpid="0000000000000023")
        liepaja = self.addSwitch("liepaja", dpid="0000000000000024")
        ulbroka = self.addSwitch("ulbroka", dpid="0000000000000025")
        olaine = self.addSwitch("olaine", dpid="0000000000000026")
        lielvard = self.addSwitch("lielvard", dpid="0000000000000027")
        ikskile = self.addSwitch("ikskile", dpid="0000000000000028")
        salaspil = self.addSwitch("salaspil", dpid="0000000000000029")
        bauska = self.addSwitch("bauska", dpid="000000000000002a")
        jekabpil = self.addSwitch("jekabpil", dpid="000000000000002b")
        jelgava = self.addSwitch("jelgava", dpid="000000000000002c")
        kalnciem = self.addSwitch("kalnciem", dpid="000000000000002d")
        kekava = self.addSwitch("kekava", dpid="000000000000002e")
        geant2 = self.addSwitch("geant2", dpid="000000000000002f")
        livberze = self.addSwitch("livberze", dpid="0000000000000030")
        ledurga = self.addSwitch("ledurga", dpid="0000000000000031")
        sigulda = self.addSwitch("sigulda", dpid="0000000000000032")
        jurmala = self.addSwitch("jurmala", dpid="0000000000000033")
        tukums = self.addSwitch("tukums", dpid="0000000000000034")
        talsi = self.addSwitch("talsi", dpid="0000000000000035")
        aizpute = self.addSwitch("aizpute", dpid="0000000000000036")
        ragona = self.addSwitch("ragona", dpid="0000000000000037")
        vangazi = self.addSwitch("vangazi", dpid="0000000000000038")
        adazi = self.addSwitch("adazi", dpid="0000000000000039")
        ozolniek = self.addSwitch("ozolniek", dpid="000000000000003a")
        eleja = self.addSwitch("eleja", dpid="000000000000003b")
        ogre = self.addSwitch("ogre", dpid="000000000000003c")
        preili = self.addSwitch("preili", dpid="000000000000003d")
        livani = self.addSwitch("livani", dpid="000000000000003e")
        balvi = self.addSwitch("balvi", dpid="000000000000003f")
        karsava = self.addSwitch("karsava", dpid="0000000000000040")
        malnava = self.addSwitch("malnava", dpid="0000000000000041")
        pusmucov = self.addSwitch("pusmucov", dpid="0000000000000042")
        zvigzden = self.addSwitch("zvigzden", dpid="0000000000000043")
        ludza = self.addSwitch("ludza", dpid="0000000000000044")
        cibla = self.addSwitch("cibla", dpid="0000000000000045")
        zilupe = self.addSwitch("zilupe", dpid="0000000000000046")

        # Adding Links
        self.addLink(iecava, riga)
        self.addLink(vircava, platone)
        self.addLink(kraslava, riga)
        self.addLink(baldone, riga)
        self.addLink(auce, dobele)
        self.addLink(broceni, saldus)
        self.addLink(platone, jelgava)
        self.addLink(platone, eleja)
        self.addLink(dobele, jelgava)
        self.addLink(krimulda, sigulda)
        self.addLink(vijkene, limbazi)
        self.addLink(saldus, riga)
        self.addLink(kapsede, liepaja)
        self.addLink(viesite, jekabpil)
        self.addLink(viesite, aizkrouk)
        self.addLink(aizkrouk, jumprava)
        self.addLink(vilani, riga)
        self.addLink(gulbene, riga)
        self.addLink(rujiena, mazsalac)
        self.addLink(rujiena, riga)
        self.addLink(salagriv, liepupe)
        self.addLink(aloja, mazsalac)
        self.addLink(aloja, pociems)
        self.addLink(aloja, limbazi)
        self.addLink(strenci, valmiera)
        self.addLink(limbazi, riga)
        self.addLink(limbazi, liepupe)
        self.addLink(liepupe, sigulda)
        self.addLink(skriveri, riga)
        self.addLink(valmiera, riga)
        self.addLink(rezekne, ludza)
        self.addLink(rezekne, riga)
        self.addLink(rezekne, daugapil)
        self.addLink(carnikav, riga)
        self.addLink(carnikav, adazi)
        self.addLink(jumprava, lielvard)
        self.addLink(kegums, lielvard)
        self.addLink(kegums, ikskile)
        self.addLink(riga, daugapil)
        self.addLink(riga, liepaja)
        self.addLink(riga, ulbroka)
        self.addLink(riga, olaine)
        self.addLink(riga, salaspil)
        self.addLink(riga, bauska)
        self.addLink(riga, jelgava)
        self.addLink(riga, kekava)
        self.addLink(riga, geant2)
        self.addLink(riga, sigulda)
        self.addLink(riga, jurmala)
        self.addLink(riga, tukums)
        self.addLink(riga, talsi)
        self.addLink(riga, aizpute)
        self.addLink(riga, adazi)
        self.addLink(riga, preili)
        self.addLink(riga, balvi)
        self.addLink(riga, karsava)
        self.addLink(daugapil, preili)
        self.addLink(ventspit, tukums)
        self.addLink(grobina, liepaja)
        self.addLink(olaine, ozolniek)
        self.addLink(ikskile, ogre)
        self.addLink(ikskile, salaspil)
        self.addLink(jekabpil, livani)
        self.addLink(jelgava, kalnciem)
        self.addLink(jelgava, livberze)
        self.addLink(jelgava, ozolniek)
        self.addLink(ledurga, sigulda)
        self.addLink(sigulda, ragona)
        self.addLink(sigulda, vangazi)
        self.addLink(karsava, malnava)
        self.addLink(malnava, pusmucov)
        self.addLink(zvigzden, ludza)
        self.addLink(ludza, cibla)
        self.addLink(ludza, zilupe)


topos = {"Latnet": (lambda: Latnet())}
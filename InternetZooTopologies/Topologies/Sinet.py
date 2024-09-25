#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Sinet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("fukuokad0", dpid="0000000000000002")
        s1 = self.addSwitch("oitau1", dpid="0000000000000003")
        s2 = self.addSwitch("kyushuu22", dpid="0000000000000004")
        s3 = self.addSwitch("kyushuit3", dpid="0000000000000005")
        s4 = self.addSwitch("hiroshim4", dpid="0000000000000006")
        s5 = self.addSwitch("hiroshim5", dpid="0000000000000007")
        s6 = self.addSwitch("ehimeu6", dpid="0000000000000008")
        s7 = self.addSwitch("yamaguch7", dpid="0000000000000009")
        s8 = self.addSwitch("imsutok8", dpid="000000000000000a")
        s9 = self.addSwitch("issputo9", dpid="000000000000000b")
        s10 = self.addSwitch("matsuyam0", dpid="000000000000000c")
        s11 = self.addSwitch("kagawau11", dpid="000000000000000d")
        s12 = self.addSwitch("kamiokao2", dpid="000000000000000e")
        s13 = self.addSwitch("chibau133", dpid="000000000000000f")
        s14 = self.addSwitch("shinshuu4", dpid="0000000000000010")
        s15 = self.addSwitch("nifs15", dpid="0000000000000011")
        s16 = self.addSwitch("kanazawa6", dpid="0000000000000012")
        s17 = self.addSwitch("jaist17", dpid="0000000000000013")
        s18 = self.addSwitch("doshisha8", dpid="0000000000000014")
        s19 = self.addSwitch("icrkyot9", dpid="0000000000000015")
        s20 = self.addSwitch("nagoyadc0", dpid="0000000000000016")
        s21 = self.addSwitch("ninsoka1", dpid="0000000000000017")
        s22 = self.addSwitch("shizuoka2", dpid="0000000000000018")
        s23 = self.addSwitch("nagoyau23", dpid="0000000000000019")
        s24 = self.addSwitch("kanazawa4", dpid="000000000000001a")
        s25 = self.addSwitch("toyamau25", dpid="000000000000001b")
        s26 = self.addSwitch("yamanash6", dpid="000000000000001c")
        s27 = self.addSwitch("utokushi7", dpid="000000000000001d")
        s28 = self.addSwitch("tokyodc38", dpid="000000000000001e")
        s29 = self.addSwitch("nii29", dpid="000000000000001f")
        s30 = self.addSwitch("niichib0", dpid="0000000000000020")
        s31 = self.addSwitch("gsistut1", dpid="0000000000000021")
        s32 = self.addSwitch("uelectro2", dpid="0000000000000022")
        s33 = self.addSwitch("riken33", dpid="0000000000000023")
        s34 = self.addSwitch("tokyodc14", dpid="0000000000000024")
        s35 = self.addSwitch("tokyodc25", dpid="0000000000000025")
        s36 = self.addSwitch("jaxaisa6", dpid="0000000000000026")
        s37 = self.addSwitch("yokohama7", dpid="0000000000000027")
        s38 = self.addSwitch("keiou38", dpid="0000000000000028")
        s39 = self.addSwitch("tokyoit39", dpid="0000000000000029")
        s40 = self.addSwitch("niigatau0", dpid="000000000000002a")
        s41 = self.addSwitch("fukuiu411", dpid="000000000000002b")
        s42 = self.addSwitch("kek42", dpid="000000000000002c")
        s43 = self.addSwitch("jaea43", dpid="000000000000002d")
        s44 = self.addSwitch("tsukubad4", dpid="000000000000002e")
        s45 = self.addSwitch("utsukuba5", dpid="000000000000002f")
        s46 = self.addSwitch("gunmau466", dpid="0000000000000030")
        s47 = self.addSwitch("ism47", dpid="0000000000000031")
        s48 = self.addSwitch("utokyo488", dpid="0000000000000032")
        s49 = self.addSwitch("kyotodc49", dpid="0000000000000033")
        s50 = self.addSwitch("kyotou500", dpid="0000000000000034")
        s51 = self.addSwitch("wasedau51", dpid="0000000000000035")
        s52 = self.addSwitch("kansaiu52", dpid="0000000000000036")
        s53 = self.addSwitch("osakau533", dpid="0000000000000037")
        s54 = self.addSwitch("kobeu54", dpid="0000000000000038")
        s55 = self.addSwitch("jamstec55", dpid="0000000000000039")
        s56 = self.addSwitch("jasri56", dpid="000000000000003a")
        s57 = self.addSwitch("tottoriu7", dpid="000000000000003b")
        s58 = self.addSwitch("okayamau8", dpid="000000000000003c")
        s59 = self.addSwitch("osakadc59", dpid="000000000000003d")
        s60 = self.addSwitch("naoj60", dpid="000000000000003e")
        s61 = self.addSwitch("saitamau1", dpid="000000000000003f")
        s62 = self.addSwitch("jaxaiat2", dpid="0000000000000040")
        s63 = self.addSwitch("tokyouag3", dpid="0000000000000041")
        s64 = self.addSwitch("nagasaki4", dpid="0000000000000042")
        s65 = self.addSwitch("kurnamot5", dpid="0000000000000043")
        s66 = self.addSwitch("sapporod6", dpid="0000000000000044")
        s67 = self.addSwitch("hokkaido7", dpid="0000000000000045")
        s68 = self.addSwitch("kitamiit8", dpid="0000000000000046")
        s69 = self.addSwitch("hirosaki9", dpid="0000000000000047")
        s70 = self.addSwitch("sendaidc0", dpid="0000000000000048")
        s71 = self.addSwitch("tohokuu71", dpid="0000000000000049")
        s72 = self.addSwitch("uofthery2", dpid="000000000000004a")
        s73 = self.addSwitch("kagoshim3", dpid="000000000000004b")

        # Adding Links
        self.addLink(s0, s64)
        self.addLink(s0, s1)
        self.addLink(s0, s2)
        self.addLink(s0, s3)
        self.addLink(s0, s5)
        self.addLink(s0, s65)
        self.addLink(s0, s72)
        self.addLink(s0, s73)
        self.addLink(s0, s10)
        self.addLink(s4, s5)
        self.addLink(s5, s7)
        self.addLink(s5, s49)
        self.addLink(s5, s57)
        self.addLink(s5, s58)
        self.addLink(s6, s10)
        self.addLink(s8, s34)
        self.addLink(s9, s34)
        self.addLink(s10, s27)
        self.addLink(s10, s11)
        self.addLink(s10, s59)
        self.addLink(s12, s20)
        self.addLink(s13, s35)
        self.addLink(s14, s35)
        self.addLink(s15, s20)
        self.addLink(s16, s24)
        self.addLink(s17, s24)
        self.addLink(s18, s49)
        self.addLink(s19, s49)
        self.addLink(s20, s34)
        self.addLink(s20, s21)
        self.addLink(s20, s22)
        self.addLink(s20, s23)
        self.addLink(s20, s59)
        self.addLink(s24, s66)
        self.addLink(s24, s35)
        self.addLink(s24, s40)
        self.addLink(s24, s41)
        self.addLink(s24, s49)
        self.addLink(s24, s25)
        self.addLink(s26, s35)
        self.addLink(s28, s35)
        self.addLink(s29, s34)
        self.addLink(s30, s34)
        self.addLink(s31, s34)
        self.addLink(s32, s35)
        self.addLink(s33, s34)
        self.addLink(s34, s35)
        self.addLink(s34, s36)
        self.addLink(s34, s37)
        self.addLink(s34, s38)
        self.addLink(s34, s39)
        self.addLink(s34, s44)
        self.addLink(s34, s48)
        self.addLink(s34, s51)
        self.addLink(s34, s60)
        self.addLink(s34, s62)
        self.addLink(s35, s46)
        self.addLink(s35, s47)
        self.addLink(s35, s55)
        self.addLink(s35, s61)
        self.addLink(s35, s63)
        self.addLink(s42, s44)
        self.addLink(s43, s44)
        self.addLink(s44, s70)
        self.addLink(s44, s45)
        self.addLink(s49, s50)
        self.addLink(s49, s59)
        self.addLink(s52, s59)
        self.addLink(s53, s59)
        self.addLink(s54, s59)
        self.addLink(s56, s59)
        self.addLink(s66, s67)
        self.addLink(s66, s70)
        self.addLink(s67, s68)
        self.addLink(s69, s70)
        self.addLink(s70, s71)


topos = {"Sinet": (lambda: Sinet())}

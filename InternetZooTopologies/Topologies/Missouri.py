#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Missouri(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("richhill0", dpid="0000000000000002")
        s1 = self.addSwitch("kearney1", dpid="0000000000000003")
        s2 = self.addSwitch("burlingt2", dpid="0000000000000004")
        s3 = self.addSwitch("toomaha33", dpid="0000000000000005")
        s4 = self.addSwitch("warrensb4", dpid="0000000000000006")
        s5 = self.addSwitch("higginsv5", dpid="0000000000000007")
        s6 = self.addSwitch("louisbur6", dpid="0000000000000008")
        s7 = self.addSwitch("peculiar7", dpid="0000000000000009")
        s8 = self.addSwitch("branson8", dpid="000000000000000a")
        s9 = self.addSwitch("saintlou9", dpid="000000000000000b")
        s10 = self.addSwitch("leessumm0", dpid="000000000000000c")
        s11 = self.addSwitch("sedalia11", dpid="000000000000000d")
        s12 = self.addSwitch("sullivan2", dpid="000000000000000e")
        s13 = self.addSwitch("steelvil3", dpid="000000000000000f")
        s14 = self.addSwitch("tipton14", dpid="0000000000000010")
        s15 = self.addSwitch("cuba15", dpid="0000000000000011")
        s16 = self.addSwitch("huntsvil6", dpid="0000000000000012")
        s17 = self.addSwitch("moberly17", dpid="0000000000000013")
        s18 = self.addSwitch("greencit8", dpid="0000000000000014")
        s19 = self.addSwitch("kirksvil9", dpid="0000000000000015")
        s20 = self.addSwitch("hurdland0", dpid="0000000000000016")
        s21 = self.addSwitch("hannibal1", dpid="0000000000000017")
        s22 = self.addSwitch("palmyra22", dpid="0000000000000018")
        s23 = self.addSwitch("newlondo3", dpid="0000000000000019")
        s24 = self.addSwitch("atlanta24", dpid="000000000000001a")
        s25 = self.addSwitch("bevier25", dpid="000000000000001b")
        s26 = self.addSwitch("eastsain6", dpid="000000000000001c")
        s27 = self.addSwitch("tochicag7", dpid="000000000000001d")
        s28 = self.addSwitch("rolla28", dpid="000000000000001e")
        s29 = self.addSwitch("pilotgro9", dpid="000000000000001f")
        s30 = self.addSwitch("jefferso0", dpid="0000000000000020")
        s31 = self.addSwitch("none31", dpid="0000000000000021")
        s32 = self.addSwitch("none32", dpid="0000000000000022")
        s33 = self.addSwitch("none33", dpid="0000000000000023")
        s34 = self.addSwitch("clevelan4", dpid="0000000000000024")
        s35 = self.addSwitch("tulsa35", dpid="0000000000000025")
        s36 = self.addSwitch("joplin36", dpid="0000000000000026")
        s37 = self.addSwitch("shelbina7", dpid="0000000000000027")
        s38 = self.addSwitch("paris38", dpid="0000000000000028")
        s39 = self.addSwitch("farber39", dpid="0000000000000029")
        s40 = self.addSwitch("vandalia0", dpid="000000000000002a")
        s41 = self.addSwitch("columbia1", dpid="000000000000002b")
        s42 = self.addSwitch("mexico42", dpid="000000000000002c")
        s43 = self.addSwitch("mokane43", dpid="000000000000002d")
        s44 = self.addSwitch("auxvasse4", dpid="000000000000002e")
        s45 = self.addSwitch("springfi5", dpid="000000000000002f")
        s46 = self.addSwitch("linneus46", dpid="0000000000000030")
        s47 = self.addSwitch("unionvil7", dpid="0000000000000031")
        s48 = self.addSwitch("alma48", dpid="0000000000000032")
        s49 = self.addSwitch("carrollt9", dpid="0000000000000033")
        s50 = self.addSwitch("tina50", dpid="0000000000000034")
        s51 = self.addSwitch("chillico1", dpid="0000000000000035")
        s52 = self.addSwitch("todesmoi2", dpid="0000000000000036")
        s53 = self.addSwitch("princeto3", dpid="0000000000000037")
        s54 = self.addSwitch("trenton54", dpid="0000000000000038")
        s55 = self.addSwitch("marshall5", dpid="0000000000000039")
        s56 = self.addSwitch("savannah6", dpid="000000000000003a")
        s57 = self.addSwitch("maryvill7", dpid="000000000000003b")
        s58 = self.addSwitch("maitland8", dpid="000000000000003c")
        s59 = self.addSwitch("rockport9", dpid="000000000000003d")
        s60 = self.addSwitch("oregon60", dpid="000000000000003e")
        s61 = self.addSwitch("saintjos1", dpid="000000000000003f")
        s62 = self.addSwitch("kansasci2", dpid="0000000000000040")
        s63 = self.addSwitch("lathrop63", dpid="0000000000000041")
        s64 = self.addSwitch("cameron64", dpid="0000000000000042")
        s65 = self.addSwitch("albany65", dpid="0000000000000043")
        s66 = self.addSwitch("bethany66", dpid="0000000000000044")

        # Adding Links
        self.addLink(s0, s7)
        self.addLink(s1, s62)
        self.addLink(s1, s63)
        self.addLink(s2, s57)
        self.addLink(s2, s58)
        self.addLink(s2, s3)
        self.addLink(s2, s52)
        self.addLink(s2, s59)
        self.addLink(s4, s10)
        self.addLink(s4, s11)
        self.addLink(s4, s5)
        self.addLink(s4, s45)
        self.addLink(s4, s7)
        self.addLink(s5, s48)
        self.addLink(s6, s34)
        self.addLink(s7, s34)
        self.addLink(s8, s45)
        self.addLink(s9, s32)
        self.addLink(s9, s26)
        self.addLink(s9, s12)
        self.addLink(s10, s62)
        self.addLink(s11, s14)
        self.addLink(s11, s55)
        self.addLink(s12, s15)
        self.addLink(s13, s15)
        self.addLink(s14, s29)
        self.addLink(s14, s30)
        self.addLink(s15, s28)
        self.addLink(s16, s17)
        self.addLink(s16, s25)
        self.addLink(s16, s49)
        self.addLink(s17, s41)
        self.addLink(s17, s42)
        self.addLink(s17, s38)
        self.addLink(s18, s19)
        self.addLink(s18, s47)
        self.addLink(s19, s20)
        self.addLink(s20, s24)
        self.addLink(s21, s33)
        self.addLink(s21, s23)
        self.addLink(s22, s33)
        self.addLink(s23, s40)
        self.addLink(s24, s25)
        self.addLink(s26, s27)
        self.addLink(s28, s30)
        self.addLink(s29, s55)
        self.addLink(s30, s41)
        self.addLink(s30, s43)
        self.addLink(s31, s35)
        self.addLink(s31, s36)
        self.addLink(s31, s62)
        self.addLink(s32, s42)
        self.addLink(s32, s44)
        self.addLink(s32, s41)
        self.addLink(s33, s37)
        self.addLink(s34, s35)
        self.addLink(s34, s62)
        self.addLink(s35, s36)
        self.addLink(s36, s45)
        self.addLink(s37, s38)
        self.addLink(s39, s40)
        self.addLink(s39, s42)
        self.addLink(s41, s44)
        self.addLink(s43, s44)
        self.addLink(s46, s51)
        self.addLink(s46, s54)
        self.addLink(s47, s53)
        self.addLink(s48, s55)
        self.addLink(s49, s50)
        self.addLink(s49, s63)
        self.addLink(s50, s51)
        self.addLink(s53, s66)
        self.addLink(s53, s54)
        self.addLink(s56, s58)
        self.addLink(s56, s61)
        self.addLink(s57, s65)
        self.addLink(s58, s65)
        self.addLink(s59, s60)
        self.addLink(s60, s61)
        self.addLink(s61, s62)
        self.addLink(s63, s64)
        self.addLink(s64, s66)
        self.addLink(s65, s66)


topos = {"Missouri": (lambda: Missouri())}

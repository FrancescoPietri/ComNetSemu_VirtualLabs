#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Syringa(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("meridian0", dpid="0000000000000002")
        s1 = self.addSwitch("emmett1", dpid="0000000000000003")
        s2 = self.addSwitch("caldwell2", dpid="0000000000000004")
        s3 = self.addSwitch("nampa3", dpid="0000000000000005")
        s4 = self.addSwitch("tipanuk4", dpid="0000000000000006")
        s5 = self.addSwitch("mountain5", dpid="0000000000000007")
        s6 = self.addSwitch("hiddensp6", dpid="0000000000000008")
        s7 = self.addSwitch("boise7", dpid="0000000000000009")
        s8 = self.addSwitch("rockland8", dpid="000000000000000a")
        s9 = self.addSwitch("arbon9", dpid="000000000000000b")
        s10 = self.addSwitch("fairfiel0", dpid="000000000000000c")
        s11 = self.addSwitch("carey11", dpid="000000000000000d")
        s12 = self.addSwitch("albion12", dpid="000000000000000e")
        s13 = self.addSwitch("malta13", dpid="000000000000000f")
        s14 = self.addSwitch("rupert14", dpid="0000000000000010")
        s15 = self.addSwitch("burley15", dpid="0000000000000011")
        s16 = self.addSwitch("bone16", dpid="0000000000000012")
        s17 = self.addSwitch("iona17", dpid="0000000000000013")
        s18 = self.addSwitch("ashton18", dpid="0000000000000014")
        s19 = self.addSwitch("tetonia19", dpid="0000000000000015")
        s20 = self.addSwitch("driggs20", dpid="0000000000000016")
        s21 = self.addSwitch("victor21", dpid="0000000000000017")
        s22 = self.addSwitch("jackson22", dpid="0000000000000018")
        s23 = self.addSwitch("freedom23", dpid="0000000000000019")
        s24 = self.addSwitch("afton24", dpid="000000000000001a")
        s25 = self.addSwitch("henry25", dpid="000000000000001b")
        s26 = self.addSwitch("gooding26", dpid="000000000000001c")
        s27 = self.addSwitch("hailey27", dpid="000000000000001d")
        s28 = self.addSwitch("coeurda8", dpid="000000000000001e")
        s29 = self.addSwitch("pocatell9", dpid="000000000000001f")
        s30 = self.addSwitch("blackfoo0", dpid="0000000000000020")
        s31 = self.addSwitch("raftrive1", dpid="0000000000000021")
        s32 = self.addSwitch("none32", dpid="0000000000000022")
        s33 = self.addSwitch("twinfall3", dpid="0000000000000023")
        s34 = self.addSwitch("sodaspri4", dpid="0000000000000024")
        s35 = self.addSwitch("paris35", dpid="0000000000000025")
        s36 = self.addSwitch("lavahots6", dpid="0000000000000026")
        s37 = self.addSwitch("downey37", dpid="0000000000000027")
        s38 = self.addSwitch("maladcit8", dpid="0000000000000028")
        s39 = self.addSwitch("mccammon9", dpid="0000000000000029")
        s40 = self.addSwitch("gooding40", dpid="000000000000002a")
        s41 = self.addSwitch("idahofal1", dpid="000000000000002b")
        s42 = self.addSwitch("cheyenne2", dpid="000000000000002c")
        s43 = self.addSwitch("glennsf3", dpid="000000000000002d")
        s44 = self.addSwitch("jackpot44", dpid="000000000000002e")
        s45 = self.addSwitch("saltlake5", dpid="000000000000002f")
        s46 = self.addSwitch("oakley46", dpid="0000000000000030")
        s47 = self.addSwitch("hagerman7", dpid="0000000000000031")
        s48 = self.addSwitch("american8", dpid="0000000000000032")
        s49 = self.addSwitch("stanthon9", dpid="0000000000000033")
        s50 = self.addSwitch("dubois50", dpid="0000000000000034")
        s51 = self.addSwitch("none51", dpid="0000000000000035")
        s52 = self.addSwitch("challis52", dpid="0000000000000036")
        s53 = self.addSwitch("stanley53", dpid="0000000000000037")
        s54 = self.addSwitch("galena54", dpid="0000000000000038")
        s55 = self.addSwitch("missoula5", dpid="0000000000000039")
        s56 = self.addSwitch("terreton6", dpid="000000000000003a")
        s57 = self.addSwitch("howe57", dpid="000000000000003b")
        s58 = self.addSwitch("arco58", dpid="000000000000003c")
        s59 = self.addSwitch("mackay59", dpid="000000000000003d")
        s60 = self.addSwitch("halfway60", dpid="000000000000003e")
        s61 = self.addSwitch("filer61", dpid="000000000000003f")
        s62 = self.addSwitch("spokane62", dpid="0000000000000040")
        s63 = self.addSwitch("preston63", dpid="0000000000000041")
        s64 = self.addSwitch("payette64", dpid="0000000000000042")
        s65 = self.addSwitch("fruitlan5", dpid="0000000000000043")
        s66 = self.addSwitch("salmon66", dpid="0000000000000044")
        s67 = self.addSwitch("council67", dpid="0000000000000045")
        s68 = self.addSwitch("mccall68", dpid="0000000000000046")
        s69 = self.addSwitch("cambridg9", dpid="0000000000000047")
        s70 = self.addSwitch("mesa70", dpid="0000000000000048")
        s71 = self.addSwitch("indianva1", dpid="0000000000000049")
        s72 = self.addSwitch("midvale72", dpid="000000000000004a")
        s73 = self.addSwitch("weiser73", dpid="000000000000004b")

        # Adding Links
        self.addLink(s0, s3)
        self.addLink(s0, s7)
        self.addLink(s1, s6)
        self.addLink(s1, s71)
        self.addLink(s2, s65)
        self.addLink(s2, s3)
        self.addLink(s4, s10)
        self.addLink(s4, s7)
        self.addLink(s5, s43)
        self.addLink(s5, s7)
        self.addLink(s7, s42)
        self.addLink(s7, s45)
        self.addLink(s7, s55)
        self.addLink(s7, s28)
        self.addLink(s7, s62)
        self.addLink(s8, s48)
        self.addLink(s8, s9)
        self.addLink(s9, s29)
        self.addLink(s9, s38)
        self.addLink(s10, s51)
        self.addLink(s11, s51)
        self.addLink(s12, s13)
        self.addLink(s12, s14)
        self.addLink(s13, s31)
        self.addLink(s14, s15)
        self.addLink(s15, s33)
        self.addLink(s15, s46)
        self.addLink(s16, s17)
        self.addLink(s16, s25)
        self.addLink(s17, s41)
        self.addLink(s17, s21)
        self.addLink(s18, s49)
        self.addLink(s19, s20)
        self.addLink(s20, s21)
        self.addLink(s22, s23)
        self.addLink(s23, s24)
        self.addLink(s23, s25)
        self.addLink(s25, s34)
        self.addLink(s26, s33)
        self.addLink(s27, s51)
        self.addLink(s27, s54)
        self.addLink(s29, s30)
        self.addLink(s29, s39)
        self.addLink(s31, s48)
        self.addLink(s32, s36)
        self.addLink(s32, s37)
        self.addLink(s32, s63)
        self.addLink(s33, s40)
        self.addLink(s33, s61)
        self.addLink(s34, s35)
        self.addLink(s34, s36)
        self.addLink(s36, s39)
        self.addLink(s41, s49)
        self.addLink(s43, s47)
        self.addLink(s44, s61)
        self.addLink(s47, s61)
        self.addLink(s49, s50)
        self.addLink(s50, s56)
        self.addLink(s52, s66)
        self.addLink(s52, s59)
        self.addLink(s52, s53)
        self.addLink(s53, s54)
        self.addLink(s56, s57)
        self.addLink(s57, s58)
        self.addLink(s58, s59)
        self.addLink(s60, s69)
        self.addLink(s64, s65)
        self.addLink(s64, s73)
        self.addLink(s67, s68)
        self.addLink(s67, s70)
        self.addLink(s69, s72)
        self.addLink(s69, s70)
        self.addLink(s70, s71)
        self.addLink(s72, s73)


topos = {"Syringa": (lambda: Syringa())}

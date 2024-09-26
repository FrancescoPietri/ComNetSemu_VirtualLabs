#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class AsnetAm(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("00", dpid="0000000000000002")
        s1 = self.addSwitch("11", dpid="0000000000000003")
        s2 = self.addSwitch("22", dpid="0000000000000004")
        s3 = self.addSwitch("33", dpid="0000000000000005")
        s4 = self.addSwitch("44", dpid="0000000000000006")
        s5 = self.addSwitch("55", dpid="0000000000000007")
        s6 = self.addSwitch("66", dpid="0000000000000008")
        s7 = self.addSwitch("77", dpid="0000000000000009")
        s8 = self.addSwitch("88", dpid="000000000000000a")
        s9 = self.addSwitch("99", dpid="000000000000000b")
        s10 = self.addSwitch("1010", dpid="000000000000000c")
        s11 = self.addSwitch("1111", dpid="000000000000000d")
        s12 = self.addSwitch("1212", dpid="000000000000000e")
        s13 = self.addSwitch("1313", dpid="000000000000000f")
        s14 = self.addSwitch("1414", dpid="0000000000000010")
        s15 = self.addSwitch("1515", dpid="0000000000000011")
        s16 = self.addSwitch("1616", dpid="0000000000000012")
        s17 = self.addSwitch("1717", dpid="0000000000000013")
        s18 = self.addSwitch("1818", dpid="0000000000000014")
        s19 = self.addSwitch("1919", dpid="0000000000000015")
        s20 = self.addSwitch("2020", dpid="0000000000000016")
        s21 = self.addSwitch("2121", dpid="0000000000000017")
        s22 = self.addSwitch("2222", dpid="0000000000000018")
        s23 = self.addSwitch("2323", dpid="0000000000000019")
        s24 = self.addSwitch("2424", dpid="000000000000001a")
        s25 = self.addSwitch("2525", dpid="000000000000001b")
        s26 = self.addSwitch("2626", dpid="000000000000001c")
        s27 = self.addSwitch("2727", dpid="000000000000001d")
        s28 = self.addSwitch("2828", dpid="000000000000001e")
        s29 = self.addSwitch("2929", dpid="000000000000001f")
        s30 = self.addSwitch("3030", dpid="0000000000000020")
        s31 = self.addSwitch("3131", dpid="0000000000000021")
        s32 = self.addSwitch("3232", dpid="0000000000000022")
        s33 = self.addSwitch("3333", dpid="0000000000000023")
        s34 = self.addSwitch("3434", dpid="0000000000000024")
        s35 = self.addSwitch("3535", dpid="0000000000000025")
        s36 = self.addSwitch("3636", dpid="0000000000000026")
        s37 = self.addSwitch("3737", dpid="0000000000000027")
        s38 = self.addSwitch("3838", dpid="0000000000000028")
        s39 = self.addSwitch("3939", dpid="0000000000000029")
        s40 = self.addSwitch("4040", dpid="000000000000002a")
        s41 = self.addSwitch("4141", dpid="000000000000002b")
        s42 = self.addSwitch("4242", dpid="000000000000002c")
        s43 = self.addSwitch("4343", dpid="000000000000002d")
        s44 = self.addSwitch("4444", dpid="000000000000002e")
        s45 = self.addSwitch("4545", dpid="000000000000002f")
        s46 = self.addSwitch("4646", dpid="0000000000000030")
        s47 = self.addSwitch("4747", dpid="0000000000000031")
        s48 = self.addSwitch("4848", dpid="0000000000000032")
        s49 = self.addSwitch("4949", dpid="0000000000000033")
        s50 = self.addSwitch("5050", dpid="0000000000000034")
        s51 = self.addSwitch("5151", dpid="0000000000000035")
        s52 = self.addSwitch("5252", dpid="0000000000000036")
        s53 = self.addSwitch("5353", dpid="0000000000000037")
        s54 = self.addSwitch("5454", dpid="0000000000000038")
        s55 = self.addSwitch("5555", dpid="0000000000000039")
        s56 = self.addSwitch("5656", dpid="000000000000003a")
        s57 = self.addSwitch("5757", dpid="000000000000003b")
        s58 = self.addSwitch("5858", dpid="000000000000003c")
        s59 = self.addSwitch("5959", dpid="000000000000003d")
        s60 = self.addSwitch("6060", dpid="000000000000003e")
        s61 = self.addSwitch("6161", dpid="000000000000003f")
        s62 = self.addSwitch("6262", dpid="0000000000000040")
        s63 = self.addSwitch("6363", dpid="0000000000000041")
        s64 = self.addSwitch("6464", dpid="0000000000000042")

        # Adding Links
        self.addLink(s0, s1)
        self.addLink(s0, s2)
        self.addLink(s0, s6)
        self.addLink(s2, s7)
        self.addLink(s2, s55)
        self.addLink(s3, s56)
        self.addLink(s3, s4)
        self.addLink(s3, s7)
        self.addLink(s4, s7)
        self.addLink(s5, s7)
        self.addLink(s7, s8)
        self.addLink(s7, s10)
        self.addLink(s7, s46)
        self.addLink(s7, s47)
        self.addLink(s7, s48)
        self.addLink(s7, s53)
        self.addLink(s7, s22)
        self.addLink(s7, s56)
        self.addLink(s8, s9)
        self.addLink(s8, s25)
        self.addLink(s8, s26)
        self.addLink(s8, s27)
        self.addLink(s8, s28)
        self.addLink(s8, s61)
        self.addLink(s10, s49)
        self.addLink(s10, s11)
        self.addLink(s12, s13)
        self.addLink(s12, s22)
        self.addLink(s14, s36)
        self.addLink(s15, s22)
        self.addLink(s16, s22)
        self.addLink(s17, s22)
        self.addLink(s18, s22)
        self.addLink(s19, s44)
        self.addLink(s19, s20)
        self.addLink(s19, s22)
        self.addLink(s20, s21)
        self.addLink(s20, s22)
        self.addLink(s22, s36)
        self.addLink(s22, s37)
        self.addLink(s22, s44)
        self.addLink(s22, s54)
        self.addLink(s22, s23)
        self.addLink(s22, s25)
        self.addLink(s22, s28)
        self.addLink(s22, s61)
        self.addLink(s22, s62)
        self.addLink(s22, s63)
        self.addLink(s24, s25)
        self.addLink(s27, s31)
        self.addLink(s29, s36)
        self.addLink(s30, s36)
        self.addLink(s31, s32)
        self.addLink(s31, s34)
        self.addLink(s31, s35)
        self.addLink(s31, s33)
        self.addLink(s36, s38)
        self.addLink(s36, s39)
        self.addLink(s36, s40)
        self.addLink(s36, s41)
        self.addLink(s36, s42)
        self.addLink(s36, s43)
        self.addLink(s45, s48)
        self.addLink(s46, s53)
        self.addLink(s46, s47)
        self.addLink(s50, s52)
        self.addLink(s51, s52)
        self.addLink(s52, s53)
        self.addLink(s54, s64)
        self.addLink(s54, s57)
        self.addLink(s54, s62)
        self.addLink(s54, s63)
        self.addLink(s55, s60)
        self.addLink(s56, s60)
        self.addLink(s57, s58)
        self.addLink(s58, s59)
        self.addLink(s59, s60)


topos = {"AsnetAm": (lambda: AsnetAm())}

#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Ulaknet(Topo):
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
        s65 = self.addSwitch("6565", dpid="0000000000000043")
        s66 = self.addSwitch("6666", dpid="0000000000000044")
        s67 = self.addSwitch("6767", dpid="0000000000000045")
        s68 = self.addSwitch("6868", dpid="0000000000000046")
        s69 = self.addSwitch("6969", dpid="0000000000000047")
        s70 = self.addSwitch("7070", dpid="0000000000000048")
        s71 = self.addSwitch("7171", dpid="0000000000000049")
        s72 = self.addSwitch("7272", dpid="000000000000004a")
        s73 = self.addSwitch("7373", dpid="000000000000004b")
        s74 = self.addSwitch("7474", dpid="000000000000004c")
        s75 = self.addSwitch("7575", dpid="000000000000004d")
        s76 = self.addSwitch("7676", dpid="000000000000004e")
        s77 = self.addSwitch("7777", dpid="000000000000004f")
        s78 = self.addSwitch("7878", dpid="0000000000000050")
        s79 = self.addSwitch("7979", dpid="0000000000000051")
        s80 = self.addSwitch("8080", dpid="0000000000000052")
        s81 = self.addSwitch("8181", dpid="0000000000000053")

        # Adding Links
        self.addLink(s0, s75)
        self.addLink(s1, s75)
        self.addLink(s2, s75)
        self.addLink(s3, s75)
        self.addLink(s4, s76)
        self.addLink(s5, s76)
        self.addLink(s6, s75)
        self.addLink(s7, s76)
        self.addLink(s8, s76)
        self.addLink(s9, s76)
        self.addLink(s10, s76)
        self.addLink(s11, s74)
        self.addLink(s12, s76)
        self.addLink(s13, s76)
        self.addLink(s14, s76)
        self.addLink(s15, s76)
        self.addLink(s16, s76)
        self.addLink(s17, s76)
        self.addLink(s18, s76)
        self.addLink(s19, s76)
        self.addLink(s20, s76)
        self.addLink(s21, s76)
        self.addLink(s22, s76)
        self.addLink(s23, s76)
        self.addLink(s24, s76)
        self.addLink(s25, s76)
        self.addLink(s26, s76)
        self.addLink(s27, s76)
        self.addLink(s28, s74)
        self.addLink(s29, s76)
        self.addLink(s30, s76)
        self.addLink(s31, s76)
        self.addLink(s32, s76)
        self.addLink(s33, s76)
        self.addLink(s34, s76)
        self.addLink(s34, s39)
        self.addLink(s35, s76)
        self.addLink(s36, s76)
        self.addLink(s37, s49)
        self.addLink(s38, s72)
        self.addLink(s40, s44)
        self.addLink(s41, s76)
        self.addLink(s42, s76)
        self.addLink(s43, s76)
        self.addLink(s44, s76)
        self.addLink(s45, s76)
        self.addLink(s46, s76)
        self.addLink(s47, s76)
        self.addLink(s48, s76)
        self.addLink(s49, s76)
        self.addLink(s50, s76)
        self.addLink(s51, s74)
        self.addLink(s52, s76)
        self.addLink(s53, s76)
        self.addLink(s54, s76)
        self.addLink(s55, s76)
        self.addLink(s56, s76)
        self.addLink(s57, s74)
        self.addLink(s58, s74)
        self.addLink(s59, s76)
        self.addLink(s60, s74)
        self.addLink(s61, s76)
        self.addLink(s62, s76)
        self.addLink(s63, s76)
        self.addLink(s64, s76)
        self.addLink(s65, s76)
        self.addLink(s66, s76)
        self.addLink(s67, s74)
        self.addLink(s68, s76)
        self.addLink(s69, s76)
        self.addLink(s70, s75)
        self.addLink(s71, s75)
        self.addLink(s72, s76)
        self.addLink(s73, s76)
        self.addLink(s74, s76)
        self.addLink(s74, s77)
        self.addLink(s74, s78)
        self.addLink(s74, s79)
        self.addLink(s74, s80)
        self.addLink(s74, s75)
        self.addLink(s75, s76)
        self.addLink(s75, s81)


topos = {"Ulaknet": (lambda: Ulaknet())}

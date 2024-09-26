#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Ion(Topo):
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
        s82 = self.addSwitch("8282", dpid="0000000000000054")
        s83 = self.addSwitch("8383", dpid="0000000000000055")
        s84 = self.addSwitch("8484", dpid="0000000000000056")
        s85 = self.addSwitch("8585", dpid="0000000000000057")
        s86 = self.addSwitch("8686", dpid="0000000000000058")
        s87 = self.addSwitch("8787", dpid="0000000000000059")
        s88 = self.addSwitch("8888", dpid="000000000000005a")
        s89 = self.addSwitch("8989", dpid="000000000000005b")
        s90 = self.addSwitch("9090", dpid="000000000000005c")
        s91 = self.addSwitch("9191", dpid="000000000000005d")
        s92 = self.addSwitch("9292", dpid="000000000000005e")
        s93 = self.addSwitch("9393", dpid="000000000000005f")
        s94 = self.addSwitch("9494", dpid="0000000000000060")
        s95 = self.addSwitch("9595", dpid="0000000000000061")
        s96 = self.addSwitch("9696", dpid="0000000000000062")
        s97 = self.addSwitch("9797", dpid="0000000000000063")
        s98 = self.addSwitch("9898", dpid="0000000000000064")
        s99 = self.addSwitch("9999", dpid="0000000000000065")
        s100 = self.addSwitch("100100", dpid="0000000000000066")
        s101 = self.addSwitch("101101", dpid="0000000000000067")
        s102 = self.addSwitch("102102", dpid="0000000000000068")
        s103 = self.addSwitch("103103", dpid="0000000000000069")
        s104 = self.addSwitch("104104", dpid="000000000000006a")
        s105 = self.addSwitch("105105", dpid="000000000000006b")
        s106 = self.addSwitch("106106", dpid="000000000000006c")
        s107 = self.addSwitch("107107", dpid="000000000000006d")
        s108 = self.addSwitch("108108", dpid="000000000000006e")
        s109 = self.addSwitch("109109", dpid="000000000000006f")
        s110 = self.addSwitch("110110", dpid="0000000000000070")
        s111 = self.addSwitch("111111", dpid="0000000000000071")
        s112 = self.addSwitch("112112", dpid="0000000000000072")
        s113 = self.addSwitch("113113", dpid="0000000000000073")
        s114 = self.addSwitch("114114", dpid="0000000000000074")
        s115 = self.addSwitch("115115", dpid="0000000000000075")
        s116 = self.addSwitch("116116", dpid="0000000000000076")
        s117 = self.addSwitch("117117", dpid="0000000000000077")
        s118 = self.addSwitch("118118", dpid="0000000000000078")
        s119 = self.addSwitch("119119", dpid="0000000000000079")
        s120 = self.addSwitch("120120", dpid="000000000000007a")
        s121 = self.addSwitch("121121", dpid="000000000000007b")
        s122 = self.addSwitch("122122", dpid="000000000000007c")
        s123 = self.addSwitch("123123", dpid="000000000000007d")
        s124 = self.addSwitch("124124", dpid="000000000000007e")

        # Adding Links
        self.addLink(s0, s25)
        self.addLink(s0, s9)
        self.addLink(s1, s114)
        self.addLink(s1, s70)
        self.addLink(s2, s99)
        self.addLink(s2, s3)
        self.addLink(s3, s4)
        self.addLink(s3, s5)
        self.addLink(s3, s6)
        self.addLink(s3, s7)
        self.addLink(s5, s103)
        self.addLink(s8, s100)
        self.addLink(s8, s92)
        self.addLink(s9, s64)
        self.addLink(s10, s58)
        self.addLink(s10, s11)
        self.addLink(s11, s18)
        self.addLink(s12, s19)
        self.addLink(s13, s18)
        self.addLink(s13, s19)
        self.addLink(s14, s17)
        self.addLink(s14, s111)
        self.addLink(s15, s114)
        self.addLink(s15, s111)
        self.addLink(s16, s112)
        self.addLink(s16, s17)
        self.addLink(s18, s39)
        self.addLink(s19, s59)
        self.addLink(s20, s64)
        self.addLink(s20, s36)
        self.addLink(s21, s80)
        self.addLink(s21, s54)
        self.addLink(s21, s79)
        self.addLink(s22, s80)
        self.addLink(s22, s54)
        self.addLink(s22, s79)
        self.addLink(s23, s26)
        self.addLink(s23, s27)
        self.addLink(s24, s35)
        self.addLink(s24, s36)
        self.addLink(s25, s28)
        self.addLink(s26, s107)
        self.addLink(s26, s87)
        self.addLink(s27, s28)
        self.addLink(s28, s88)
        self.addLink(s29, s32)
        self.addLink(s29, s33)
        self.addLink(s29, s101)
        self.addLink(s29, s105)
        self.addLink(s29, s106)
        self.addLink(s29, s30)
        self.addLink(s30, s31)
        self.addLink(s31, s32)
        self.addLink(s33, s34)
        self.addLink(s34, s104)
        self.addLink(s34, s103)
        self.addLink(s35, s42)
        self.addLink(s37, s40)
        self.addLink(s37, s38)
        self.addLink(s38, s43)
        self.addLink(s39, s40)
        self.addLink(s41, s42)
        self.addLink(s41, s44)
        self.addLink(s43, s44)
        self.addLink(s44, s116)
        self.addLink(s45, s93)
        self.addLink(s45, s54)
        self.addLink(s46, s93)
        self.addLink(s46, s47)
        self.addLink(s47, s48)
        self.addLink(s48, s49)
        self.addLink(s48, s123)
        self.addLink(s48, s78)
        self.addLink(s49, s109)
        self.addLink(s50, s76)
        self.addLink(s51, s76)
        self.addLink(s51, s52)
        self.addLink(s52, s109)
        self.addLink(s53, s123)
        self.addLink(s55, s56)
        self.addLink(s55, s62)
        self.addLink(s56, s57)
        self.addLink(s57, s97)
        self.addLink(s58, s97)
        self.addLink(s58, s92)
        self.addLink(s59, s124)
        self.addLink(s59, s61)
        self.addLink(s60, s124)
        self.addLink(s60, s109)
        self.addLink(s61, s98)
        self.addLink(s62, s98)
        self.addLink(s63, s96)
        self.addLink(s63, s66)
        self.addLink(s64, s116)
        self.addLink(s64, s65)
        self.addLink(s65, s111)
        self.addLink(s66, s87)
        self.addLink(s67, s74)
        self.addLink(s67, s68)
        self.addLink(s67, s86)
        self.addLink(s68, s95)
        self.addLink(s69, s117)
        self.addLink(s69, s70)
        self.addLink(s71, s74)
        self.addLink(s72, s74)
        self.addLink(s72, s117)
        self.addLink(s73, s124)
        self.addLink(s73, s110)
        self.addLink(s74, s112)
        self.addLink(s74, s110)
        self.addLink(s75, s76)
        self.addLink(s75, s95)
        self.addLink(s76, s110)
        self.addLink(s77, s80)
        self.addLink(s77, s78)
        self.addLink(s79, s82)
        self.addLink(s81, s82)
        self.addLink(s81, s94)
        self.addLink(s83, s86)
        self.addLink(s83, s94)
        self.addLink(s84, s94)
        self.addLink(s85, s95)
        self.addLink(s88, s91)
        self.addLink(s89, s90)
        self.addLink(s89, s115)
        self.addLink(s89, s122)
        self.addLink(s90, s96)
        self.addLink(s91, s120)
        self.addLink(s93, s123)
        self.addLink(s96, s121)
        self.addLink(s99, s105)
        self.addLink(s100, s105)
        self.addLink(s100, s107)
        self.addLink(s101, s106)
        self.addLink(s102, s103)
        self.addLink(s106, s108)
        self.addLink(s107, s108)
        self.addLink(s111, s113)
        self.addLink(s112, s113)
        self.addLink(s113, s114)
        self.addLink(s115, s117)
        self.addLink(s117, s118)
        self.addLink(s118, s119)
        self.addLink(s119, s120)
        self.addLink(s120, s121)
        self.addLink(s121, s122)


topos = {"Ion": (lambda: Ion())}

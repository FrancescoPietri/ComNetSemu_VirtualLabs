graph [
  DateObtained "22/10/10"
  GeoLocation "Beijing, China"
  GeoExtent "Metro"
  Network "NSFCNET"
  Provenance "Primary"
  Note "Hard to tell if multiple POS OC-48 links"
  Source "http://www.cn.apan.net/nsfcmap.htm"
  Version "1.0"
  Type "REN"
  DateType "Current"
  Backbone 1
  Commercial 0
  label "Nsfcnet"
  ToolsetVersion "0.3.34dev-20120328"
  Customer 0
  IX 0
  SourceGitVersion "e278b1b"
  DateModifier "="
  DateMonth "10"
  LastAccess "7/10/10"
  Access 0
  Layer "IP"
  Creator "Topology Zoo Toolset"
  Developed 0
  Transit 0
  NetworkDate "2010_10"
  DateYear "2010"
  LastProcessed "2011_09_01"
  Testbed 1
  node [
    id 0
    label "0"
    Internal 1
    type "Router"
  ]
  node [
    id 1
    label "1"
    Internal 0
  ]
  node [
    id 2
    label "2"
    Internal 0
  ]
  node [
    id 3
    label "3"
    Internal 0
  ]
  node [
    id 4
    label "4"
    Internal 1
    type "Router"
  ]
  node [
    id 5
    label "5"
    Internal 1
    type "Router"
  ]
  node [
    id 6
    label "6"
    Internal 1
    type "Router"
  ]
  node [
    id 7
    label "7"
    Internal 1
    type "Router"
  ]
  node [
    id 8
    label "8"
    Internal 1
    type "Router"
  ]
  node [
    id 9
    label "9"
    Internal 0
  ]
  edge [
    source 0
    target 8
    LinkType "OC-48"
    LinkLabel "POS OC-48"
    LinkNote "POS "
  ]
  edge [
    source 0
    target 4
    LinkType "OC-48"
    LinkLabel "POS OC-48"
    LinkNote "POS "
  ]
  edge [
    source 2
    target 4
    id "e0"
  ]
  edge [
    source 3
    target 4
    LinkLabel "GE"
  ]
  edge [
    source 4
    target 5
    LinkLabel "DPT ring"
  ]
  edge [
    source 4
    target 7
    LinkLabel "DPT Ring"
  ]
  edge [
    source 4
    target 8
    LinkType "OC-48"
    LinkLabel "POS OC-48"
    LinkNote "POS "
  ]
  edge [
    source 5
    target 6
    LinkLabel "DPT Ring"
  ]
  edge [
    source 6
    target 7
    LinkLabel "DPT Ring"
  ]
  edge [
    source 8
    target 9
    LinkLabel "GE"
  ]
]

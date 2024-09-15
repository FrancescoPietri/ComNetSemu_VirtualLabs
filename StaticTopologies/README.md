# Network Topologies Overview

This README provides a brief description of the proposed network topologies available in this folder. Each topology is presented with four configuration options:
- **Simple**: No VLAN or link capacity settings.
- **VLAN Only**: VLAN configurations without link capacity adjustments.
- **Link Capacity Only**: Link capacity settings without VLAN configurations.
- **Complete**: Includes both VLAN and link capacity settings.

## Office Topology

![OfficeTopology/OfficeTopologyDiagram.png](OfficeTopology/OfficeTopologyDiagram.png)

This topology represents a typical office environment, featuring three separate offices, a printer room, and a director’s office. Each room is assigned to its own VLAN, and the topology is designed with redundancy in mind, allowing for multiple tests and routing of traffic through alternative paths.

- **Office 1** = VLAN 1
- **Office 2** = VLAN 2
- **Office 3** = VLAN 3
- **Management** = VLAN 4
- **Printer Room** = VLAN 5

## Hybrid Topology

![HybridTopology/HybridTopologyDiagram.png](HybridTopology/HybridTopologyDiagram.png)

This topology integrates three distinct network designs: a tree topology, a linear topology, and a rectangular topology. It allows for testing different network structures within the same configuration.

- **Hosts h1, h3** = VLAN 1
- **Hosts h2, h4** = VLAN 2
- **Hosts h5, h6** = VLAN 3

## Lab Topology

![LabTopology/LabTopologyDiagram.png](LabTopology/LabTopologyDiagram.png)

This topology simulates a lab environment consisting of four separate laboratories, all connected to a central switch (s2). Each lab also has a backup switch (s7, s8) that will be used in case the main switch fails. The backup switches have lower link capacities to simulate an environment where traffic primarily flows through the main switch unless a failure occurs.

- **Lab 1** = VLAN 1
- **Lab 2** = VLAN 2
- **Lab 3** = VLAN 3
- **Lab 4** = VLAN 4

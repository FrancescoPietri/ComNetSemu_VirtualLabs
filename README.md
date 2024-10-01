# ComNetSemu Virtual Labs

This repository contains a collection of various Mininet topologies designed for use in the ComNetSemu environment. A more detailed description of each topology can be found in the `StaticTopologies` folder.
This repository contains also a GMLtoTopology converter and a base dataset of GML files, additional information can be found inside the `GMLtoTopology` folder.

## How to Demo

1. Install the ComNetSemu environment: [https://www.granelli-lab.org/researches/relevant-projects/comnetsemu-labs](https://www.granelli-lab.org/researches/relevant-projects/comnetsemu-labs)

2. Clone the repository:  
   ```bash
   git clone https://github.com/FrancescoPietri/ComNetSemu_VirtualLabs

3. Navigate to the desired topology and execute:
   ```bash
   sudo mn --custom [TOPOLOGY_SCRIPT_NAME] --topo [TOPOLOGY_NAME] --link tc

_(You can find the topology name at the end of each script file.)_
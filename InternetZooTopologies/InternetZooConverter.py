from GMLtoTopology import GMLtoTopology
import os
import random

PATH_DATASET = 'DatasetGML/'
PATH_TOPOLOGIES = 'Topologies/'

if __name__ == "__main__":

    converter = GMLtoTopology()

    while 1:
        print("""Options:\n
    1) Convert a specific GML
    2) Convert a random GML
    3) Convert whole dataset""")
        sel = input()
        if(sel=="1"):
            print("Enter GML file name")
            name = input()
            converter.convert_gml_topo(name, PATH_DATASET, PATH_TOPOLOGIES)
            break
        if(sel=="2"):
            random.seed()
            randFile = random.randrange(0, len(os.listdir(PATH_DATASET))-1)
            randFile = os.listdir(PATH_DATASET)[randFile]
            converter.convert_gml_topo(randFile, PATH_DATASET, PATH_TOPOLOGIES)
            break
        if(sel=="3"):
            for file in os.listdir(PATH_DATASET):
                try:
                    converter.convert_gml_topo(file, PATH_DATASET, PATH_TOPOLOGIES)
                except:
                    print(file + "\n")

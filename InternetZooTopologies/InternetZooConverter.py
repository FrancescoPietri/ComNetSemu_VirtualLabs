from GMLtoTopology import GMLtoTopology

PATH_DATASET = 'DatasetGML/'
PATH_TOPOLOGIES = 'Topologies/'

if __name__ == "__main__":
    topology_converter = GMLtoTopology()
    topology_converter.convert_gml_topo("Aarnet", PATH_DATASET, PATH_TOPOLOGIES)

class FineMotorSCAN:
    def __init__(self):
        self.network = {
            "Left Hemisphere": {
                'Frontal_lobe': [],
                'Parietal_lobe': [],
                'Temporal_lobe': ['Auditory_cortex'],
                'Occipital_lobe': ['Visual_cortex'],
                'Prefrontal_cortex': [],
                'Insular_cortex': [],
                'Cingulate_cortex': [],
                'Striatum': ['Caudate_nucleus', 'Putamen'],
                'Globus_pallidus': ['External_globus_pallidus', 'Internal_globus_pallidus'],
                'Subthalamic_nucleus': [],
                'Substantia_nigra': [],
                'Amygdala': [],
                'Hippocampus': [],
                'Thalamus': [],
                'Hypothalamus': [],
                'Superior_colliculus': [],
                'Inferior_colliculus': [],
                'Periaqueductal_gray': [],
                'Red_nucleus': [],
                'Crus_cerebri': [],
                'Pons': [],
                'Cerebellum': ['Anterior_lobe', 'Posterior_lobe', 'Flocculonodular_lobe'],
                'Medulla_oblongata': ['Pyramids', 'Olive']
            },
            "Right Hemisphere": {
                'Frontal_lobe': [],
                'Parietal_lobe': [],
                'Temporal_lobe': ['Auditory_cortex'],
                'Occipital_lobe': ['Visual_cortex'],
                'Prefrontal_cortex': [],
                'Insular_cortex': [],
                'Cingulate_cortex': [],
                'Striatum': ['Caudate_nucleus', 'Putamen'],
                'Globus_pallidus': ['External_globus_pallidus', 'Internal_globus_pallidus'],
                'Subthalamic_nucleus': [],
                'Substantia_nigra': [],
                'Amygdala': [],
                'Hippocampus': [],
                'Thalamus': [],
                'Hypothalamus': [],
                'Superior_colliculus': [],
                'Inferior_colliculus': [],
                'Periaqueductal_gray': [],
                'Red_nucleus': [],
                'Crus_cerebri': [],
                'Pons': [],
                'Cerebellum': ['Anterior_lobe', 'Posterior_lobe', 'Flocculonodular_lobe'],
                'Medulla_oblongata': ['Pyramids', 'Olive']
            }
        }

    def add_connection(self, hemisphere, region, subregion):
        if subregion not in self.network[hemisphere][region]:
            self.network[hemisphere][region].append(subregion)

    def remove_connection(self, hemisphere, region, subregion):
        if subregion in self.network[hemisphere][region]:
            self.network[hemisphere][region].remove(subregion)

    def connection_exists(self, hemisphere, region, subregion):
        return subregion in self.network[hemisphere][region]

    def get_connections_of_region(self, hemisphere, region):
        return self.network[hemisphere][region]

    def get_regions_connected_to_subregion(self, hemisphere, subregion):
        connected_regions = []
        for region, subregions in self.network[hemisphere].items():
            if subregion in subregions:
                connected_regions.append(region)
        return connected_regions

  
    def get_network(self):
        return self.network

    def add_additional_regions(self, hemisphere, region, subregions):
        """
        This method is used to add additional regions to the network based on the decision made by the frontal cortex.
        The decision is made at a subconscious level when it is identified that the learning rate for coordination and movement needs improvement.
        """
        for subregion in subregions:
            self.add_connection(hemisphere, region, subregion)
    def add_cross_hemisphere_connection(self, region1, subregion1, region2, subregion2):
        """
        This method is used to add a connection between two subregions in different hemispheres.
        """
        self.add_connection("Left Hemisphere", region1, subregion1)
        self.add_connection("Right Hemisphere", region2, subregion2)

    def remove_cross_hemisphere_connection(self, region1, subregion1, region2, subregion2):
        """
        This method is used to remove a connection between two subregions in different hemispheres.
        """
        self.remove_connection("Left Hemisphere", region1, subregion1)
        self.remove_connection("Right Hemisphere", region2, subregion2)

    def cross_hemisphere_connection_exists(self, region1, subregion1, region2, subregion2):
        """
        This method checks if a connection exists between two subregions in different hemispheres.
        """
        return self.connection_exists("Left Hemisphere", region1, subregion1) and self.connection_exists("Right Hemisphere", region2, subregion2)


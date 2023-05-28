class GrossMotorSCAN:
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
                'Cerebellum': ['Anterior_lobe', 'Posterior_lobe', 'Flocculonodular_lobe', 'Dentate_nucleus', 'Interposed_nucleus', 'Fastigial_nucleus'],
                'Medulla_oblongata': ['Pyramids', 'Olive', 'Reticular_formation']
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
                'Cerebellum': ['Anterior_lobe', 'Posterior_lobe', 'Flocculonodular_lobe', 'Dentate_nucleus', 'Interposed_nucleus', 'Fastigial_nucleus'],
                'Medulla_oblongata': ['Pyramids', 'Olive', 'Reticular_formation']
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


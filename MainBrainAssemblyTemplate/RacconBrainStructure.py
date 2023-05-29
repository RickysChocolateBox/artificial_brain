class RaccoonBrainStructure:
    def __init__(self):
        self.brain_structure = {
            "Left Hemisphere": {
                "Forebrain": {
                    "Telencephalon": {
                        "Cerebral_cortex": {
                            "Neocortex": {
                                "Frontal_lobe": {
                                    "Brocas_area": {},  # part of the language center
                                },
                                "Parietal_lobe": {},
                                "Temporal_lobe": {
                                    "Wernickes_area": {},  # part of the language center
                                },
                                "Occipital_lobe": {}
                            },
                            "Paleocortex": {},
                            "Archicortex": {
                                "Hippocampus": {}
                            }
                        },
                        "Basal_ganglia": {
                            "Striatum": {},
                            "Globus_pallidus": {},
                        },
                        "Limbic_system": {
                            "Amygdala": {},
                            "Hippocampus": {},
                        },
                    },
                    "Diencephalon": {
                        "Thalamus": {},
                        "Hypothalamus": {},
                    },
                },
                "Midbrain": {
                    "Tectum": {
                        "Superior_colliculus": {},
                        "Inferior_colliculus": {},
                    },
                    "Tegmentum": {},
                },
                "Hindbrain": {
                    "Metencephalon": {
                        "Pons": {},
                        "Cerebellum": {},
                    },
                    "Myelencephalon": {
                        "Medulla_oblongata": {},
                    },
                },
            },
            "Right Hemisphere": {
                "Forebrain": {
                    "Telencephalon": {
                        "Cerebral_cortex": {
                            "Neocortex": {
                                "Frontal_lobe": {},
                                "Parietal_lobe": {},
                                "Temporal_lobe": {},
                                "Occipital_lobe": {}
                            },
                            "Paleocortex": {},
                            "Archicortex": {
                                "Hippocampus": {}
                            }
                        },
                        "Basal_ganglia": {
                            "Striatum": {},
                            "Globus_pallidus": {},
                        },
                        "Limbic_system": {
                            "Amygdala": {},
                            "Hippocampus": {},
                        },
                    },
                    "Diencephalon": {
                        "Thalamus": {},
                        "Hypothalamus": {},
                    },
                },
                "Midbrain": {
                    "Tectum": {
                        "Superior_colliculus": {},
                        "Inferior_colliculus": {},
                    },
                    "Tegmentum": {},
                },
                "Hindbrain": {
                    "Metencephalon": {
                        "Pons": {},
                        "Cerebellum": {},
                    },
                    "Myelencephalon": {
                        "Medulla_oblongata": {},
                    },
                },
            },
        }

    def get_regions(self, hemisphere, brain_part):
        return self.brain_structure[hemisphere][brain_part]


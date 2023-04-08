from ResNetBlock import ResNetBlock
from DataAugmentation import DataAugmentation
from AdversarialTraining import AdversarialTraining
from BatchNormalization import BatchNormalization
from EnsembleLearning import EnsembleLearning
from EarlyStopping import EarlyStopping
from L1L2Regularization import L1L2Regularization
from DropoutRegularization import DropoutRegularization
from WeightDecay import WeightDecay

class CorrectionMechanisms:
    def __init__(self, mechanism_configurations):
        self.mechanisms = {
            "ResNetBlock": ResNetBlock(**mechanism_configurations.get("ResNetBlock", {})),
            "DataAugmentation": DataAugmentation(**mechanism_configurations.get("DataAugmentation", {})),
            "AdversarialTraining": AdversarialTraining(**mechanism_configurations.get("AdversarialTraining", {})),
            "BatchNormalization": BatchNormalization(**mechanism_configurations.get("BatchNormalization", {})),
            "EnsembleLearning": EnsembleLearning(**mechanism_configurations.get("EnsembleLearning", {})),
            "EarlyStopping": EarlyStopping(**mechanism_configurations.get("EarlyStopping", {})),
            "L1L2Regularization": L1L2Regularization(**mechanism_configurations.get("L1L2Regularization", {})),
            "DropoutRegularization": DropoutRegularization(**mechanism_configurations.get("DropoutRegularization", {})),
            "WeightDecay": WeightDecay(**mechanism_configurations.get("WeightDecay", {}))
        }

    def get_mechanism(self, mechanism_name):
        return self.mechanisms.get(mechanism_name, None)

    # You can add methods to apply and configure specific mechanisms

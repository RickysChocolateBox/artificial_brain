from A3C import A3C
from ActorCritic import ActorCritic
from DeepQNetwork import DeepQNetwork
from DoubleQLearning import DoubleQLearning
from MonteCarlo import MonteCarlo
from PolicyGradient import PolicyGradient
from PPO import PPO
from QLearning import QLearning
from SARSA import SARSA
from TDLearning import TDLearning

class ReinforcementLearningModels:
    def __init__(self, model_configurations):
        self.models = {
            "A3C": A3C(**model_configurations.get("A3C", {})),
            "ActorCritic": ActorCritic(**model_configurations.get("ActorCritic", {})),
            "DeepQNetwork": DeepQNetwork(**model_configurations.get("DeepQNetwork", {})),
            "DoubleQLearning": DoubleQLearning(**model_configurations.get("DoubleQLearning", {})),
            "MonteCarlo": MonteCarlo(**model_configurations.get("MonteCarlo", {})),
            "PolicyGradient": PolicyGradient(**model_configurations.get("PolicyGradient", {})),
            "PPO": PPO(**model_configurations.get("PPO", {})),
            "QLearning": QLearning(**model_configurations.get("QLearning", {})),
            "SARSA": SARSA(**model_configurations.get("SARSA", {})),
            "TDLearning": TDLearning(**model_configurations.get("TDLearning", {}))
        }

    def get_model(self, model_name):
        return self.models.get(model_name, None)

    # You can add methods to train, predict, etc. for specific models


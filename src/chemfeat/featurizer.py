from abc import ABC, abstractmethod


class AbstractFeaturizer(ABC):
    def __init__(self, shared_data):
        self.shared_data = shared_data

    @abstractmethod
    def set_config(self, config):
        pass

    @abstractmethod
    def get_features(self, data):
        pass


class ConcreteFeaturizerA(AbstractFeaturizer):
    def set_config(self, config):
        self.config = config

    def get_features(self, data):
        # Use self.shared_data in some way
        features = f"Features from ConcreteFeaturizerA for {data} with shared data {self.shared_data}"
        return features


class ConcreteFeaturizerB(AbstractFeaturizer):
    def set_config(self, config):
        self.config = config

    def get_features(self, data):
        # Use self.shared_data in some way
        features = f"Features from ConcreteFeaturizerB for {data} with shared data {self.shared_data}"
        return features


class FeaturizerFactory:
    def __init__(self, shared_data):
        self.shared_data = shared_data
        self._featurizers = {
            'ConcreteFeaturizerA': ConcreteFeaturizerA(shared_data),
            'ConcreteFeaturizerB': ConcreteFeaturizerB(shared_data),
        }

    def get_featurizer(self, name):
        return self._featurizers.get(name)

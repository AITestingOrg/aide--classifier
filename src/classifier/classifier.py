from .train import Train
from data.loader import Loader

class Classifier:

    def train_model(self):
        loader = Loader()
        data = loader.load_spaadia()
        trainer = Train()
        trainer.train(data)
        self.model = trainer.get_trained_model()

    def is_question(self, fragment):
        return True if self.model.predict([fragment])[0] == 1 else False

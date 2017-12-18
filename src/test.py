from classifier.classifier import Classifier

classifier = Classifier()
classifier.train_model()
print(classifier.is_question('do you hold a credit card'))

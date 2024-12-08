import json
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier

class ChatbotModel:
    def __init__(self, intents_path="data/intents.json"):
        # Untuk Load data intents
        with open(intents_path, "r") as file:
            self.intents = json.load(file)
        
        self.vectorizer = TfidfVectorizer()
        self.classifier = KNeighborsClassifier(n_neighbors=3)
        self.train_model()

    def train_model(self):
        # Untuk Ekstrak data pelatihan
        sentences = []
        labels = []
        for intent in self.intents["intents"]:
            for pattern in intent["patterns"]:
                sentences.append(pattern)
                labels.append(intent["tag"])
        
        # Fit vectorizer dan classifier
        X = self.vectorizer.fit_transform(sentences)
        self.classifier.fit(X, labels)

    def predict_response(self, user_input):
        # untuk prediksi label berdasarkan input
        X_input = self.vectorizer.transform([user_input])
        tag = self.classifier.predict(X_input)[0]

        # Mengambil respon acak dari intent yang sesuai
        for intent in self.intents["intents"]:
            if intent["tag"] == tag:
                return random.choice(intent["responses"])
        return "Maaf, saya tidak mengerti. Bisa ulangi?"

# Testing Model (opsional)
if __name__ == "__main__":
    chatbot = ChatbotModel()
    print(chatbot.predict_response("Hai!"))

import random

class MarkovChatbot:
    def __init__(self):
        self.model = {}

    def train(self, corpus: list[str]):
        for sentence in corpus:
            words = sentence.strip().split()
            for i in range(len(words)-1):
                key = words[i]
                next_word = words[i+1]
                self.model.setdefault(key, []).append(next_word)

    def respond(self, start_word="안녕, 반가워!") -> str:
        if not self.model:
            return "학습을 하지 못 했어요 🥲"

        word = start_word
        response = [word]
        for _ in range(10):
            next_words = self.model.get(word)
            if not next_words:
                break
            word = random.choice(next_words)
            response.append(word)
        return " ".join(response)

default_corpus = [
    "안녕 만나서 반가워",
]

chatbot = MarkovChatbot()
chatbot.train(default_corpus)
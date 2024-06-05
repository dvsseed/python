import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class SimpleQA:
    def __init__(self, filepath):
        self.qa_pairs = self.load_qa_pairs(filepath)
        self.questions = [q for q, a in self.qa_pairs]
        self.answers = [a for q, a in self.qa_pairs]
        self.vectorizer = TfidfVectorizer().fit(self.questions)

    def load_qa_pairs(self, filepath):
        qa_pairs = []
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                questions, answer = line.strip().split('|')
                for question in questions.split(','):
                    qa_pairs.append((question.strip(), answer))
        return qa_pairs

    def preprocess_text(self, text):
        # 去除標點符號，並將文本轉換為小寫
        text = re.sub(r'[^\w\s]', '', text)
        text = text.lower()
        return text

    def find_best_match(self, question):
        preprocessed_question = self.preprocess_text(question)
        question_vec = self.vectorizer.transform([preprocessed_question])
        question_vecs = self.vectorizer.transform(self.questions)
        similarities = cosine_similarity(question_vec, question_vecs).flatten()
        best_match_index = np.argmax(similarities)
        
        if similarities[best_match_index] > 0.2:  # 設定一個相似度閾值
            return self.answers[best_match_index]
        else:
            return "對不起，我不知道這個問題的答案。"

    def find_answer(self, question):
        return self.find_best_match(question)


if __name__ == "__main__":
    # 示例使用
    qa_system = SimpleQA('qa.txt')
    question = input("請輸入你的問題：")
    answer = qa_system.find_answer(question)
    print(answer)

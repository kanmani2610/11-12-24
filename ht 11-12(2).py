class TextProcessor:
    def __init__(self, text):
        self.text = text
        self.sentences = []

    def split_into_sentences(self):
        special_chars = ['.', '!', '?']
        sentence = ""
        for char in self.text:
            sentence += char
            if char in special_chars:
                self.sentences.append(sentence.strip())
                sentence = ""
        if sentence.strip():  # Append any remaining text as the last sentence
            self.sentences.append(sentence.strip())
        
        for i in self.sentences:
            print(i)
    
    def process_sentence(self):
        text_data = []
        for sentence in self.sentences:
            word_count = len(sentence.split())
            text_data.append({"Sentence": sentence, "Word count": word_count})
        return text_data

# Example Usage
text = "Hello! How are you? I am fine. Let's learn NLP."
tex = TextProcessor(text)
tex.split_into_sentences()
processed_sentences = tex.process_sentence()
for item in processed_sentences:
    print(item)

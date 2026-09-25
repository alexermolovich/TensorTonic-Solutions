import uuid

class SimpleTokenizer:
    def __init__(self):
        self.word_to_id = {"<PAD>": 0, "<UNK>": 1, "<BOS>": 2, "<EOS>": 3}
        self.id_to_word = {0: "<PAD>", 1: "<UNK>", 2: "<BOS>", 3: "<EOS>"}
        self.vocab_size = 4
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def generate_deterministic_id(self, input_string: str) -> str:
        
        unique_id = uuid.uuid5(uuid.NAMESPACE_DNS, input_string)
        return unique_id.hex  
    
    def build_vocab(self, texts: list[str]) -> None:
        # 1. Collect all unique words across all texts
        unique_words = set()
        for text in texts:
            for word in text.lower().split():
                unique_words.add(word)
    
        # 2. Sort the unique words alphabetically
        sorted_words = sorted(unique_words)
    
        # 3. Assign sequential IDs starting at 4
        current_id = 4
        for word in sorted_words:
            if word not in self.word_to_id:
                self.word_to_id[word] = current_id
                self.id_to_word[current_id] = word
                current_id += 1
        
        # 4. Update overall vocabulary size
        self.vocab_size = len(self.word_to_id)   
    
    def encode(self, text: str) -> list[int]:
        """
        Returns token IDs for the input text.
        """
        formatted = text.lower()
        splitted = formatted.split() 
       
        ids = [] 
       
        for word in splitted:
            if word in self.word_to_id:
                ids.append(self.word_to_id[word])
            else:
                ids.append(1)
        
        return ids  
        
    def decode(self, ids: list[int]) -> str:
        """
        Returns the decoded, space-separated text.
        """
        decoded_words = [
            self.id_to_word.get(id, self.unk_token) for id in ids
        ]
        return " ".join(decoded_words)   

        pass
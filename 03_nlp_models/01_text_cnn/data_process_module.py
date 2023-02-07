import torch
import torch.nn as nn
import os
import numpy as np
import pickle as pkl
from tqdm import tqdm
import time
from datetime import timedelta
from torch.utils.data import Dataset, DataLoader


MAX_VOCAB_SZIE = 10000
UNK, PAD = "<UNK>", "<PAD>"

def get_data(config, use_word):
    # tokenizer = lambda x: [y for y in x]
    # use_word = False
    if use_word:
        tokenizer = lambda x: x.split(" ")
    else:
        tokenizer = lambda x: [y for y in x]

    vocab = pkl.load(open(config.vocab_path, "rb"))
    print(f"Vocab size: {len(vocab)}")

    train = load_dataset(config.train_path, config.pad_size, tokenizer, vocab)
    dev = load_dataset(config.dev_path, config.pad_size, tokenizer, vocab)
    test = load_dataset(config.test_path, config.pad_size, tokenizer, vocab)
    return vocab, train, dev, test

def load_dataset(path, pad_size, tokenizer, vocab):
    contents = []
    with open(path, "r+", encoding="UTF-8") as f:
        for line in tqdm(f):
            lin = line.strip()
            if not lin:
                continue
            content, label = lin.split("\t")

            words_line = []
            token = tokenizer(content)
            seq_len = len(token)
            if pad_size:
                if len(token) < pad_size:
                    token.extend([vocab.get(PAD)] * (pad_size - len(token)))
                else:
                    token = token[:pad_size]
                    seq_len = pad_size
            for word in token:
                words_line.append(vocab.get(word, vocab.get(UNK)))
            contents.append((words_line, int(label)))
    return contents

# vocab, train_data, dev_data, test_data = get_data(config)



class TextDataset(Dataset):
    def __init__(self, data, config):
        self.device = config.device
        self.x = torch.LongTensor([x[0] for x in data]).to(self.device)
        self.y = torch.LongTensor([x[1] for x in data]).to(self.device)

    def __getitem__(self, index):
        self.text = self.x[index]
        self.label = self.y[index]
        return self.text, self.label

    def __len__(self):
        return len(self.x)

def get_time_dif(start_time):
    end_time = time.time()
    time_dif = end_time - start_time
    return timedelta(seconds=int(round(time_dif)))
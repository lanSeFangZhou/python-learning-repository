import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

class Config():
    def __init__(self, dataset, embedding):
        self.model_name = "TextRNN"
        self.train_path = dataset + "/data/train.txt"
        self.dev_path = dataset + "/data/dev.txt"
        self.test_path = dataset + "/data/test.txt"
        self.class_list = [x.strip() for x in open(
            dataset + "/data/class.txt").readlines()]
        self.vocab_path = dataset + "/data/vocab.pkl"
        self.save_path = dataset + "/saved_dict/" + self.model_name + ".ckpt"
        self.embedding_pretrained = torch.tensor(
            np.load(dataset + "/data" + embedding)["embeddings"].astype("float32"))
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.droupout = 0.5
        self.require_improvement = 1000
        self.num_classes = len(self.class_list)
        self.num_epochs = 10
        self.batch_size = 128
        self.pad_size = 32
        self.learning_rate = 1e-3
        self.embed = self.embedding_pretrained.size(1)
        self.hidden_size = 128
        self.num_layers = 2


class RNNModel(nn.Module):
    def __init__(self, config):
        super(RNNModel, self).__init__()
        self.embedding = nn.Embedding.from_pretrained(config.embedding_pretrained, freeze=False)
        self.lstm = nn.LSTM(config.embed, config.hidden_size, config.num_layers,
                            bidirectional=True, batch_first=True, dropout=config.droupout)
        self.fc = nn.Linear(config.hidden_size * 2, config.num_classes)

    def forward(self, x):
        out = self.embedding(x)
        out, _ = self.lstm(out)
        out = self.fc(out[:, -1, :])
        return out
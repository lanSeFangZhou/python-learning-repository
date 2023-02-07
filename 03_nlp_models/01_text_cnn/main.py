import numpy as np
import torch
from RNNmodel import *
import time
from data_process_module import *
from torch.utils.data import DataLoader
from train_best_model import *

dataset = "01_text_cnn"
embedding = "/embedding_SougouNews.npz"

np.random.seed(1)
torch.manual_seed(1)
torch.cuda.manual_seed_all(1)
torch.backends.cudnn.deterministic = True

config = Config(dataset, embedding)

start_time = time.time()
print("Loading data...")
vocab, train_data, dev_data, test_data = get_data(config, False)
dataloaders = {
    "train": DataLoader(TextDataset(train_data, config), 128, shuffle=True),
    "dev": DataLoader(TextDataset(dev_data, config), 128, shuffle=True),
    "test": DataLoader(TextDataset(test_data, config), 128, shuffle=True)
}

time_dif = get_time_dif(start_time)
print("Time usage:", time_dif)

config.n_vocab = len(vocab)
model = RNNModel(config).to(config.device)
init_network(model)
print(model.parameters)
train_best(config, model, dataloaders)
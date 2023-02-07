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
model = RNNModel(config).to(config.device)
model.load_state_dict(torch.load(config.save_path))
model.eval()
model.eval()
loss_total = 0
predict_all = np.array([], dtype=int)
labels_all = np.array([], dtype=int)
with torch.no_grad():
    lin = "60年铁树开花形状似玉米芯(组图)	5"

    content, label = lin.split("\t")

    tokenizer = lambda x: [y for y in x]
    vocab = pkl.load(open(config.vocab_path, "rb"))
    print(f"Vocab size: {len(vocab)}")
    pad_size = config.pad_size


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
    # contents.append((words_line, int(label)))
    print(f"words_line:{words_line}")
    words_line = torch.tensor(words_line)


    outputs = model(words_line)
    predic = torch.max(outputs.data, 1)[1].cpu().numpy()
    print(f"predic: {predic}")
    predict_all = np.append(predict_all, predic)
    print(f"predict_all: {predict_all}")

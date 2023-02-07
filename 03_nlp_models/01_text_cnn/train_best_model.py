import torch
import numpy as np
import torch.nn as nn
import time
import torch
import copy
import pandas as pd
import datetime
from sklearn import metrics
import numpy as np

import torch.nn as nn

def init_network(model, method="xavier", exclude="embedding", seed=123):
    for name, w in model.named_parameters():
        if exclude not in name:
            if "weight" in name:
                if method == "xavier":
                    nn.init.xavier_normal_(w)
                elif method == "kaiming":
                    nn.init.kaiming_normal_(w)
                else:
                    nn.init.normal_(w)
            elif "bias" in name:
                nn.init.constant_(w, 0)
            else:
                pass

def train_best(config, model, dataloaders, log_step=100):
    optimizer = torch.optim.Adam(model.parameters(), lr=config.learning_rate)
    loss_function = torch.nn.CrossEntropyLoss()
    best_acc = 0
    best_model = copy.deepcopy(model.state_dict())

    total_step = 0
    dev_best_loss = float("inf")
    last_improve = 0
    flag = False

    dfhistory = pd.DataFrame(columns=["epoch", "train_loss", "train_acc", "dev_loss", "dev_acc"])

    device = config.device

    print("Start Training...\n")
    nowtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("========" * 8 + "%s\n" % nowtime)

    for i in range(config.num_epochs):
        step = 0
        print("Epoch [{}/{}]\n".format(i + 1, config.num_epochs))

        for inputs, labels in dataloaders["train"]:
            model.train()

            inputs = inputs.to(device)
            labels = labels.to(device)
            optimizer.zero_grad()

            outputs = model(inputs)
            loss = loss_function(outputs, labels)
            loss.backward()
            optimizer.step()

            total_step += 1
            step += 1

            if step % log_step == 0:
                true = labels.data.cpu()
                predic = torch.max(outputs.data, 1)[1].cpu()
                train_loss = loss.item()
                train_acc = metrics.accuracy_score(true, predic)

                dev_acc, dev_loss = dev_eval(model, dataloaders["dev"], loss_function)

                dfhistory.loc[i] = (i, train_loss, train_acc, dev_loss, dev_acc)

                if dev_loss < dev_best_loss:
                    dev_best_loss = dev_loss
                    torch.save(model.state_dict(), config.save_path)
                    last_improve = total_step

                print("[step = {} batch] train_loss = {:.3f}, train_acc = {:.2%}, dev_loss = {:.3f},"
                      "dev_acc = {:.2%}".format(step, train_loss, train_acc, dev_loss, dev_acc))

            if total_step - last_improve > config.require_improvement:
                print("No optimization for a long time, auto-stoppping...")
                flag = True
                break
        if flag:
            break

    model.load_state_dict(torch.load(config.save_path))
    model.eval()
    start_time = time.time()
    test_acc, test_loss = dev_eval(model, dataloaders["test"], loss_function)
    print("============")
    print("test_loss: {:.3f}  test_acc:{:.2f}".format(test_loss, test_acc))

    return dfhistory

def dev_eval(model, data, loss_function):
    model.eval()
    loss_total = 0
    predict_all = np.array([], dtype=int)
    labels_all = np.array([], dtype=int)
    with torch.no_grad():
        for texts, labels in data:
            print(f"texts:{texts}")
            break
            outputs = model(texts)
            loss = loss_function(outputs, labels)
            loss_total += loss.item()
            labels = labels.data.cpu().numpy()
            predic = torch.max(outputs.data, 1)[1].cpu().numpy()
            labels_all = np.append(labels_all, labels)
            predict_all = np.append(predict_all, predic)

    acc = metrics.accuracy_score(labels_all, predict_all)
    return acc, loss_total / len(data)

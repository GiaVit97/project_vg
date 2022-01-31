import math
from tabnanny import check
import torch
import logging
import numpy as np
from tqdm import tqdm
import torch.nn as nn
import multiprocessing
from os.path import join
from datetime import datetime
from torch.utils.data.dataloader import DataLoader
from os.path import exists
import h5py
import util
import test
import parser
import commons
import network
import datasets_ws
import os

args = parser.parse_arguments()

model = network.GeoLocalizationNet(args)
model = model.to(args.device)

best_model_state_dict = torch.load(join(args.model_folder, "best_model.pth"))["model_state_dict"]
model.load_state_dict(best_model_state_dict)

# Test on different dataset
for test_dataset in args.test_datasets.split(","):
    test_ds = datasets_ws.BaseDataset(args, args.datasets_folder, test_dataset, "test")
    logging.info(f"Test set: {test_ds}")
    recalls, recalls_str = test.test(args, test_ds, model)
    logging.info(f"Recalls on {test_ds}: {recalls_str}")
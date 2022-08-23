from torch.utils.data import Dataset, DataLoader
from glob import glob
import numpy as np
import time
from typing import Callable
import os
from utils import load_protobuf, load_pickle, load_flatbuffers, load_capnp

class LoadDataset(Dataset):
    def __init__(self, data_dir: str, data_reader: Callable) -> None:
        super().__init__()

        self.data_reader: Callable = data_reader
        self.files: list[str] = glob(os.path.join(data_dir, "*"))
        self.len = len(self.files)
    
    def __len__(self):
        return self.len
    
    def __getitem__(self, index):
        data = self.data_reader(self.files[index])
        return data

def load_np(file_path: str):
    return np.load(file_path)

def main():
    # dataset = LoadDataset("data/np32", load_np)
    # dataset = LoadDataset("data/pkl32", load_pickle)
    # dataset = LoadDataset("data/pb32", load_protobuf)
    # dataset = LoadDataset("data/fb32", load_flatbuffers)
    dataset = LoadDataset("data/capnp32", load_capnp)
        
    dataloader = DataLoader(
        dataset, 
        batch_size=2, 
        shuffle=True,
        num_workers=4, 
        drop_last=True
    )

    start = time.perf_counter()
    for _ in  range(1):
        for _ in dataloader:
            pass
    end = time.perf_counter()
    print(end-start)

if __name__ == "__main__":
    main()
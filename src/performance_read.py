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


def perfomance(data_dir: str, data_loader: Callable):
    dataset = LoadDataset(data_dir, data_loader)
    dataloader = DataLoader(
        dataset,
        batch_size=2,
        shuffle=True,
        num_workers=4,
        drop_last=True
    )

    n_iter = 5
    start = time.perf_counter()
    for _ in range(n_iter):
        for _ in dataloader:
            pass
    end = time.perf_counter()
    mean_val = (end-start) / n_iter
    return data_dir, mean_val


def main():
    base_dir = "data_ssd"
    with open("read_results_ssd.csv", "w") as f:
        data_dir, mean_val = perfomance(f"{base_dir}/np32", load_np)
        f.write(f"{data_dir},{mean_val}\n")
        data_dir, mean_val = perfomance(f"{base_dir}/pkl32", load_pickle)
        f.write(f"{data_dir},{mean_val}\n")
        data_dir, mean_val = perfomance(f"{base_dir}/pb32", load_protobuf)
        f.write(f"{data_dir},{mean_val}\n")
        data_dir, mean_val = perfomance(f"{base_dir}/fb32", load_flatbuffers)
        f.write(f"{data_dir},{mean_val}\n")
        data_dir, mean_val = perfomance(f"{base_dir}/capnp32", load_capnp)
        f.write(f"{data_dir},{mean_val}\n")

    base_dir = "data"
    with open("read_results.csv", "w") as f:
        data_dir, mean_val = perfomance(f"{base_dir}/np32", load_np)
        f.write(f"{data_dir},{mean_val}\n")
        data_dir, mean_val = perfomance(f"{base_dir}/pkl32", load_pickle)
        f.write(f"{data_dir},{mean_val}\n")
        data_dir, mean_val = perfomance(f"{base_dir}/pb32", load_protobuf)
        f.write(f"{data_dir},{mean_val}\n")
        data_dir, mean_val = perfomance(f"{base_dir}/fb32", load_flatbuffers)
        f.write(f"{data_dir},{mean_val}\n")
        data_dir, mean_val = perfomance(f"{base_dir}/capnp32", load_capnp)
        f.write(f"{data_dir},{mean_val}\n")


if __name__ == "__main__":
    main()

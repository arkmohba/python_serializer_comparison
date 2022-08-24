from typing import Callable
import numpy as np
import os
import time
from utils import save_pickle, save_flatbuffers, save_protobuf, save_capnp

def perfomance(data: np.ndarray, path: str, saver: Callable):
    n_iter = 10
    start = time.perf_counter()
    for _ in range(n_iter):
        saver(path, data)
    end = time.perf_counter()
    mean_val = (end-start) / n_iter
    return path, mean_val

def performance_each(data: np.ndarray, root_dir: str, inter_dir: str, ext: str, saver: Callable):
    target_dir = os.path.join(root_dir, inter_dir)
    os.makedirs(target_dir, exist_ok=True)
    path = os.path.join(target_dir, "data" + ext)
    _, latency =  perfomance(data, path, saver)
    return inter_dir, latency


def main():

    # 4Kデータサイズのfloat
    data: np.ndarray = np.random.rand(3840*2160*3)
    data = data.astype(np.float32)

    data_dir = "data"
    with open("write_results.csv", "w") as f:
        inter_dir, mean_val = performance_each(data, data_dir, "np32", ".npy", np.save)
        f.write(f"{inter_dir},{mean_val}\n")
        inter_dir, mean_val = performance_each(data, data_dir, "pkl32", ".pkl", save_pickle)
        f.write(f"{inter_dir},{mean_val}\n")
        inter_dir, mean_val = performance_each(data, data_dir, "fb32", ".fb", save_flatbuffers)
        f.write(f"{inter_dir},{mean_val}\n")
        inter_dir, mean_val = performance_each(data, data_dir, "pb32", ".pb", save_protobuf)
        f.write(f"{inter_dir},{mean_val}\n")
        inter_dir, mean_val = performance_each(data, data_dir, "capnp32", ".capnp", save_capnp)
        f.write(f"{inter_dir},{mean_val}\n")

    data_dir = "data_ssd"
    with open("write_results_ssd.csv", "w") as f:
        inter_dir, mean_val = performance_each(data, data_dir, "np32", ".npy", np.save)
        f.write(f"{inter_dir},{mean_val}\n")
        inter_dir, mean_val = performance_each(data, data_dir, "pkl32", ".pkl", save_pickle)
        f.write(f"{inter_dir},{mean_val}\n")
        inter_dir, mean_val = performance_each(data, data_dir, "fb32", ".fb", save_flatbuffers)
        f.write(f"{inter_dir},{mean_val}\n")
        inter_dir, mean_val = performance_each(data, data_dir, "pb32", ".pb", save_protobuf)
        f.write(f"{inter_dir},{mean_val}\n")
        inter_dir, mean_val = performance_each(data, data_dir, "capnp32", ".capnp", save_capnp)
        f.write(f"{inter_dir},{mean_val}\n")


if __name__ == "__main__":
    main()
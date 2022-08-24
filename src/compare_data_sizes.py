from typing import Callable
import os
import time
from utils import save_pickle, save_flatbuffers, save_protobuf, save_capnp

def check_file_size(root_dir: str, inter_dir: str, ext: str):
    target_file = os.path.join(root_dir, inter_dir, "data" + ext)

    return inter_dir, os.path.getsize(target_file)


def main():

    # 4Kデータサイズのfloat

    data_dir = "data"
    with open("file_size.csv", "w") as f:
        inter_dir, mean_val = check_file_size(data_dir, "np32", ".npy")
        f.write(f"{inter_dir},{mean_val}\n")
        inter_dir, mean_val = check_file_size(data_dir, "pkl32", ".pkl")
        f.write(f"{inter_dir},{mean_val}\n")
        inter_dir, mean_val = check_file_size(data_dir, "fb32", ".fb")
        f.write(f"{inter_dir},{mean_val}\n")
        inter_dir, mean_val = check_file_size(data_dir, "pb32", ".pb")
        f.write(f"{inter_dir},{mean_val}\n")
        inter_dir, mean_val = check_file_size(data_dir, "capnp32", ".capnp")
        f.write(f"{inter_dir},{mean_val}\n")

if __name__ == "__main__":
    main()
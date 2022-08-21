import numpy as np
import os
import shutil
from tqdm import tqdm
import joblib

from utils import save_pickle, save_flatbuffers, save_protobuf

def duplicates(input_file: str, n_duplicate: int):
    prefix, suffix = os.path.splitext(input_file)
    print(prefix)
    new_files = [prefix + f"_{i}" + suffix for i in range(n_duplicate)]
    joblib.Parallel(n_jobs=-1)(joblib.delayed(shutil.copy)(input_file, new_file) for new_file in tqdm(new_files))

def main():
    # 4Kデータサイズのfloatを10個作る
    data_dir = "data"
    np_dir = os.path.join(data_dir, "np32")
    os.makedirs(np_dir, exist_ok=True)
    pkl_dir = os.path.join(data_dir, "pkl32")
    os.makedirs(pkl_dir, exist_ok=True)
    fb_dir = os.path.join(data_dir, "fb32")
    os.makedirs(fb_dir, exist_ok=True)
    pb_dir = os.path.join(data_dir, "pb32")
    os.makedirs(pb_dir, exist_ok=True)

    data: np.ndarray = np.random.rand(3840 * 2048 * 3)
    data_32 = data.astype(np.float32)
    
    # # Numpy
    # f_path = os.path.join(np_dir, "data.npy")
    # np.save(f_path, data_32)
    
    # # Pickle
    # f_path = os.path.join(pkl_dir, "data.pkl")
    # save_pickle(f_path, data_32)

    # # Flatbuffers
    # f_path = os.path.join(fb_dir, "data.fb")
    # save_flatbuffers(f_path, data_32)
    # duplicates(f_path, 100)

    # Protobuf
    f_path = os.path.join(pb_dir, "data.pb")
    save_protobuf(f_path, data_32)
    duplicates(f_path, 100)

if __name__ == "__main__":
    main()
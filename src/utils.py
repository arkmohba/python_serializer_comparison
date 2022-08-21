import numpy as np
import pickle
import flatbuffers
import myflat.Data as Data
import myprotobuf.data_pb2 as data_pb2


def save_pickle(f_path: str, data: np.ndarray):
    with open(f_path, mode="wb") as f:
        pickle.dump(data, f)


def load_pickle(f_path: str, data: np.ndarray):
    with open(f_path, mode="rb") as f:
        data = pickle.load(f)
    return data


def save_flatbuffers(f_path: str, data: np.ndarray):
    with open(f_path, mode="wb") as f:
        float_bytes = 4
        builder = flatbuffers.Builder(len(data) * float_bytes + 1024)
        Data.DataStartDataArrayVector(builder, len(data))
        for i in range(len(data)):
            builder.PrependFloat32(data[i])
        data_array = builder.EndVector()
        Data.DataStart(builder)
        Data.DataAddDataArray(builder, data_array)
        output = Data.DataEnd(builder)
        builder.Finish(output)
        with open(f_path, "wb") as f:
            buf = builder.Output()
            f.write(buf)


def load_flatbuffers(f_path: str):
    with open(f_path, mode="rb") as f:
        data = Data.Data.GetRootAsData(f.read(), 0)
    return data.DataArrayAsNumpy().copy()


def save_protobuf(f_path: str, data: np.ndarray):
    pb_obj = data_pb2.Data()
    pb_obj.data_array.extend(data.tolist())
    with open(f_path, mode="wb") as f:
        f.write(pb_obj.SerializeToString())


def load_protobuf(f_path: str):
    with open(f_path, mode="rb") as f:
        buf = f.read()
    pb_obj = data_pb2.Data()
    pb_obj.ParseFromString(buf)
    return np.array(pb_obj.data_array)

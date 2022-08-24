import numpy as np
import pickle
import flatbuffers
import myflat.Data as Data
import myprotobuf.data_pb2 as data_pb2
import capnp
import mycapnp.data_capnp as data_capnp


def save_pickle(f_path: str, data: np.ndarray):
    with open(f_path, mode="wb") as f:
        pickle.dump(data, f)


def load_pickle(f_path: str):
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


def save_capnp(f_path: str, data: np.ndarray):
    data_cp = data_capnp.Data.new_message()
    data_array_cp = data_cp.init('dataArray', len(data))
    for i in range(len(data)):
        data_array_cp[i] = float(data[i])
    buf = data_cp.to_bytes()
    with open(f_path, "wb") as f:
        f.write(buf)


def load_capnp(f_path: str):
    with open(f_path, "rb") as f:
        # buf = f.read()
        # data = data_capnp.Data.from_bytes(buf)
        data = data_capnp.Data.read(f, traversal_limit_in_words=3840*2160*3)
    return np.array(data.dataArray)

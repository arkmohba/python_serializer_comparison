# python_serializer_comparison
pythonで使えるシリアライザーの比較を行うリポジトリ。

## 比較対象

[こちらのリポジトリ](https://github.com/chronoxor/CppSerialization)も参考にPythonで使えそうな以下を比較する。機械学習のデータを保存することを想定し、floatの配列を保存することを想定する。

* protocol buffers
* CAP’N　PROTO
* FlatBuffers
* numpy.load
* pickle.load
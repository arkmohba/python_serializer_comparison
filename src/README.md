# メモ

## 各種スキーマコンパイル

### flatbuffers

```
cd myflat
flatc --python data.fbs
```

### protocol_buffers

```
cd myprotobuf
protoc --python_out=. data.proto
```

### capnproto

python版では直接スキーマからファイルを読み取るのでコンパイルは不要
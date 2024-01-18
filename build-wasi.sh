#/usr/bin/env bash

export GYP_CROSSCOMPILE=1
export AR_host=ar
export CC_host=clang
export CXX_host=clang++
export AR_target="$WASI_SDK_PATH/bin/ar"
export CC_target="$WASI_SDK_PATH/bin/clang"
export CXX_target="$WASI_SDK_PATH/bin/clang++"

node-gyp rebuild --verbose --nodedir=./wasm -- -f make -Dtarget_os=wasi -Dwasm_threads=1

# node-gyp clean
# node-gyp configure --nodedir=./wasm -- -f make -Dtarget_os=wasi -Dwasm_threads=1
# node-gyp build --verbose

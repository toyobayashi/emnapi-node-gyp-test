#/usr/bin/env bash

GYP_CROSSCOMPILE=1
AR_host=ar
CC_host=clang
CXX_host=clang++
AR_target=emar
CC_target=emcc
CXX_target=em++

emmake node-gyp rebuild --verbose --nodedir=./wasm -- -f make 

# node-gyp clean
# node-gyp configure --nodedir=./wasm -- -f make
# emmake node-gyp build --verbose

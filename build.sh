#/usr/bin/env bash

export GYP_CROSSCOMPILE=1
export AR_host=ar
export CC_host=clang
export CXX_host=clang++
export AR_target=emar
export CC_target=emcc
export CXX_target=em++

emmake node-gyp rebuild --verbose --nodedir=./node_modules/emnapi -- -f make -Dcross_compiling=1

# node-gyp clean
# node-gyp configure --nodedir=./node_modules/emnapi -- -f make -Dcross_compiling=1
# emmake node-gyp build --verbose

#/usr/bin/env bash

__dirname=$(cd `dirname $0`;pwd)

export GYP_CROSSCOMPILE=1
export AR_host=ar
export CC_host=clang
export CXX_host=clang++
export AR_target="$WASI_SDK_PATH/bin/ar"
export CC_target="$WASI_SDK_PATH/bin/clang"
export CXX_target="$WASI_SDK_PATH/bin/clang++"

npx node-gyp rebuild -C $__dirname --verbose --arch=wasm32 --nodedir=$__dirname/node_modules/emnapi -- -f make-linux "$@"

# node-gyp clean -C $__dirname
# node-gyp configure -C $__dirname --nodedir=$__dirname/node_modules/emnapi -- -f make -DOS=wasi -Dwasm_threads=1
# node-gyp build -C $__dirname --verbose

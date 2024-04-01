#/usr/bin/env bash

__dirname=$(cd `dirname $0`;pwd)

export GYP_CROSSCOMPILE=1
export AR_host=ar
export CC_host=clang
export CXX_host=clang++
export AR_target=emar
export CC_target=emcc
export CXX_target=em++

emmake npx node-gyp rebuild -C $__dirname --verbose --arch=wasm32 --nodedir=$__dirname/node_modules/emnapi -- -f make -Demnapi_manual_linking=1 "$@"

# node-gyp clean -C $__dirname
# node-gyp configure -C $__dirname --nodedir=$__dirname/node_modules/emnapi -- -f make -DOS=emscripten
# emmake node-gyp build -C $__dirname --verbose

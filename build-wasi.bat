@echo off

set GYP_CROSSCOMPILE=1
@REM set AR_host=ar
@REM set CC_host=clang
@REM set CXX_host=clang++
set AR_target=%WASI_SDK_PATH%/bin/ar.exe
set CC_target=%WASI_SDK_PATH%/bin/clang.exe
set CXX_target=%WASI_SDK_PATH%/bin/clang++.exe

call npx.cmd node-gyp clean
call npx.cmd node-gyp configure --arch=wasm32 --nodedir=./node_modules/emnapi -- -f make -DOS=wasi -Dwasm_threads=1

node ./scripts/replace-sep.js

call make -C build V=1

@echo off

set GYP_CROSSCOMPILE=1
@REM set AR_host=ar
@REM set CC_host=clang
@REM set CXX_host=clang++
set AR_target=emar.bat
set CC_target=emcc.bat
set CXX_target=em++.bat

call npx.cmd node-gyp clean
call npx.cmd node-gyp configure --nodedir=./wasm -- -f make

node ./scripts/replace-sep.js

call emmake.bat make -C build V=1

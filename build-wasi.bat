@echo off

set GYP_CROSSCOMPILE=1
@REM set AR_host=ar
@REM set CC_host=clang
@REM set CXX_host=clang++
set AR_target=%WASI_SDK_PATH%/bin/ar.exe
set CC_target=%WASI_SDK_PATH%/bin/clang.exe
set CXX_target=%WASI_SDK_PATH%/bin/clang++.exe

call npx.cmd node-gyp rebuild -C %~dp0 --verbose --arch=wasm32 --nodedir=%~dp0node_modules/emnapi -- -f make %*

@REM call npx.cmd node-gyp clean -C %~dp0
@REM call npx.cmd node-gyp configure -C %~dp0 --arch=wasm32 --nodedir=%~dp0node_modules/emnapi -- -f make %*

@REM node %~dp0scripts/replace-sep.js

@REM call make -C %~dp0build V=1

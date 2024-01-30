@echo off

set GYP_CROSSCOMPILE=1
@REM set AR_host=ar
@REM set CC_host=clang
@REM set CXX_host=clang++
set AR_target=emar.bat
set CC_target=emcc.bat
set CXX_target=em++.bat

call emmake.bat npx node-gyp rebuild -C %~dp0 --verbose --arch=wasm32 --nodedir=%~dp0node_modules/emnapi -- -f make-linux %*

@REM call npx.cmd node-gyp clean -C %~dp0
@REM call npx.cmd node-gyp configure -C %~dp0 --arch=wasm32 --nodedir=%~dp0node_modules/emnapi -- -f make %*

@REM node %~dp0scripts/replace-sep.js

@REM call emmake.bat make -C %~dp0build V=1

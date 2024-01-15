## Log

<details>
<summary>⚠ Windows 11 23H2 22631.3007</summary><br />

Make sure `make.exe` is in your `%Path%`, run the commands in Cygwin terminal (POSIX-like environment)

```
$ npm install

> emnapi-node-gyp-test@0.0.0 install
> node-gyp rebuild

gyp info it worked if it ends with ok
gyp info using node-gyp@10.0.1
gyp info using node@20.8.0 | win32 | x64
gyp info find Python using Python version 3.10.6 found at "C:\Users\toyobayashi\AppData\Local\Programs\Python\Python310\python.exe"

gyp info find VS using VS2022 (17.7.34031.279) found at:
gyp info find VS "C:\Program Files\Microsoft Visual Studio\2022\Community"
gyp info find VS run with --verbose for detailed information
gyp info spawn C:\Users\toyobayashi\AppData\Local\Programs\Python\Python310\python.exe
gyp info spawn args [
gyp info spawn args 'C:\\Users\\toyobayashi\\Projects\\emnapi-node-gyp-test\\node_modules\\node-gyp\\gyp\\gyp_main.py',
gyp info spawn args 'binding.gyp',
gyp info spawn args '-f',
gyp info spawn args 'msvs',
gyp info spawn args '-I',
gyp info spawn args 'C:\\Users\\toyobayashi\\Projects\\emnapi-node-gyp-test\\build\\config.gypi',
gyp info spawn args '-I',
gyp info spawn args 'C:\\Users\\toyobayashi\\Projects\\emnapi-node-gyp-test\\node_modules\\node-gyp\\addon.gypi',
gyp info spawn args '-I',
gyp info spawn args 'C:\\Users\\toyobayashi\\AppData\\Local\\node-gyp\\Cache\\20.8.0\\include\\node\\common.gypi',
gyp info spawn args '-Dlibrary=shared_library',
gyp info spawn args '-Dvisibility=default',
gyp info spawn args '-Dnode_root_dir=C:\\Users\\toyobayashi\\AppData\\Local\\node-gyp\\Cache\\20.8.0',
gyp info spawn args '-Dnode_gyp_dir=C:\\Users\\toyobayashi\\Projects\\emnapi-node-gyp-test\\node_modules\\node-gyp',
gyp info spawn args '-Dnode_lib_file=C:\\\\Users\\\\toyobayashi\\\\AppData\\\\Local\\\\node-gyp\\\\Cache\\\\20.8.0\\\\<(target_arch)\\\\node.lib',
gyp info spawn args '-Dmodule_root_dir=C:\\Users\\toyobayashi\\Projects\\emnapi-node-gyp-test',
gyp info spawn args '-Dnode_engine=v8',
gyp info spawn args '--depth=.',
gyp info spawn args '--no-parallel',
gyp info spawn args '--generator-output',
gyp info spawn args 'C:\\Users\\toyobayashi\\Projects\\emnapi-node-gyp-test\\build',
gyp info spawn args '-Goutput_dir=.'
gyp info spawn args ]
gyp info spawn C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Current\Bin\MSBuild.exe
gyp info spawn args [
gyp info spawn args 'build\\binding.sln',
gyp info spawn args '/clp:Verbosity=minimal',
gyp info spawn args '/nologo',
gyp info spawn args '/p:Configuration=Release;Platform=x64'
gyp info spawn args ]

  binding.c
  win_delay_load_hook.cc
    正在创建库 C:\Users\toyobayashi\Projects\emnapi-node-gyp-test\build\Release\bind
  ing.lib 和对象 C:\Users\toyobayashi\Projects\emnapi-node-gyp-test\build\Release\
  binding.exp
  正在生成代码
  Previous IPDB not found, fall back to full compilation.
  All 4 functions were compiled because no usable IPDB/IOBJ from previous compi
  lation was found.
  已完成代码的生成
  binding.vcxproj -> C:\Users\toyobayashi\Projects\emnapi-node-gyp-test\build\R
  elease\\binding.node
gyp info ok

> emnapi-node-gyp-test@0.0.0 postinstall
> patch-package

patch-package 8.0.0
Applying patches...
node-gyp@10.0.1 ✔

added 155 packages, and audited 156 packages in 7s

found 0 vulnerabilities
```

```
$ npm run build:win

> emnapi-node-gyp-test@0.0.0 build:win
> build.bat

gyp info it worked if it ends with ok
gyp info using node-gyp@10.0.1
gyp info using node@20.8.0 | win32 | x64
gyp info ok
gyp info it worked if it ends with ok
gyp info using node-gyp@10.0.1
gyp info using node@20.8.0 | win32 | x64
gyp info find Python using Python version 3.10.6 found at "C:\Users\toyobayashi\AppData\Local\Programs\Python\Python310\python.exe"
gyp info find VS using VS2022 (17.7.34031.279) found at:
gyp info find VS "C:\Program Files\Microsoft Visual Studio\2022\Community"
gyp info find VS run with --verbose for detailed information
gyp WARN read config.gypi ENOENT: no such file or directory, open 'C:\Users\toyobayashi\Projects\emnapi-node-gyp-test\wasm\include\node\config.gypi'
gyp info spawn C:\Users\toyobayashi\AppData\Local\Programs\Python\Python310\python.exe
gyp info spawn args [
gyp info spawn args 'C:\\Users\\toyobayashi\\Projects\\emnapi-node-gyp-test\\node_modules\\node-gyp\\gyp\\gyp_main.py',
gyp info spawn args 'binding.gyp',
gyp info spawn args '-f',
gyp info spawn args 'make',
gyp info spawn args '-I',
gyp info spawn args 'C:\\Users\\toyobayashi\\Projects\\emnapi-node-gyp-test\\build\\config.gypi',
gyp info spawn args '-I',
gyp info spawn args 'C:\\Users\\toyobayashi\\Projects\\emnapi-node-gyp-test\\node_modules\\node-gyp\\addon.gypi',
gyp info spawn args '-I',
gyp info spawn args 'C:\\Users\\toyobayashi\\Projects\\emnapi-node-gyp-test\\wasm\\common.gypi',
gyp info spawn args '-Dlibrary=shared_library',
gyp info spawn args '-Dvisibility=default',
gyp info spawn args '-Dnode_root_dir=./wasm',
gyp info spawn args '-Dnode_gyp_dir=C:\\Users\\toyobayashi\\Projects\\emnapi-node-gyp-test\\node_modules\\node-gyp',
gyp info spawn args '-Dnode_lib_file=wasm\\\\$(Configuration)\\\\node.lib',
gyp info spawn args '-Dmodule_root_dir=C:\\Users\\toyobayashi\\Projects\\emnapi-node-gyp-test',
gyp info spawn args '-Dnode_engine=v8',
gyp info spawn args '--depth=.',
gyp info spawn args '--no-parallel',
gyp info spawn args '--generator-output',
gyp info spawn args 'C:\\Users\\toyobayashi\\Projects\\emnapi-node-gyp-test\\build',
gyp info spawn args '-Goutput_dir=.'
gyp info spawn args ]
gyp info ok
make: C:\Users\toyobayashi\app\make\mingw32-make.EXE -C build V=1
mingw32-make.EXE: Entering directory 'C:/Users/toyobayashi/Projects/emnapi-node-gyp-test/build'
  emcc.bat -o Release/obj.target/binding/node_modules/emnapi/src/js_native_api.o ../node_modules/emnapi/src/js_native_api.c '-DNODE_GYP_MODULE_NAME=binding' '-DUSING_UV_SHARED=1' '-DUSING_V8_SHARED=1' '-DV8_DEPRECATION_WARNINGS=1' '-DBUILDING_NODE_EXTENSION' '-D__STDC_FORMAT_MACROS' '-D_LARGEFILE_SOURCE' '-D_FILE_OFFSET_BITS=64' -I../wasm/include/node -I../wasm/src -I../wasm/deps/openssl/config -I../wasm/deps/openssl/openssl/include -I../wasm/deps/uv/include -I../wasm/deps/zlib -I../wasm/deps/v8/include -IC:/Users/toyobayashi/Projects/emnapi-node-gyp-test/node_modules/emnapi/include  -Wall -Wextra -Wno-unused-parameter -sDEFAULT_TO_CXX=0 -O3  -MMD -MF ./Release/.deps/Release/obj.target/binding/node_modules/emnapi/src/js_native_api.o.d.raw   -c
sed: -e expression #1, char 5: unterminated `s' command
  emcc.bat -o Release/obj.target/binding/node_modules/emnapi/src/node_api.o ../node_modules/emnapi/src/node_api.c '-DNODE_GYP_MODULE_NAME=binding' '-DUSING_UV_SHARED=1' '-DUSING_V8_SHARED=1' '-DV8_DEPRECATION_WARNINGS=1' '-DBUILDING_NODE_EXTENSION' '-D__STDC_FORMAT_MACROS' '-D_LARGEFILE_SOURCE' '-D_FILE_OFFSET_BITS=64' -I../wasm/include/node -I../wasm/src -I../wasm/deps/openssl/config -I../wasm/deps/openssl/openssl/include -I../wasm/deps/uv/include -I../wasm/deps/zlib -I../wasm/deps/v8/include -IC:/Users/toyobayashi/Projects/emnapi-node-gyp-test/node_modules/emnapi/include  -Wall -Wextra -Wno-unused-parameter -sDEFAULT_TO_CXX=0 -O3  -MMD -MF ./Release/.deps/Release/obj.target/binding/node_modules/emnapi/src/node_api.o.d.raw   -c
sed: -e expression #1, char 5: unterminated `s' command
  emcc.bat -o Release/obj.target/binding/node_modules/emnapi/src/async_cleanup_hook.o ../node_modules/emnapi/src/async_cleanup_hook.c '-DNODE_GYP_MODULE_NAME=binding' '-DUSING_UV_SHARED=1' '-DUSING_V8_SHARED=1' '-DV8_DEPRECATION_WARNINGS=1' '-DBUILDING_NODE_EXTENSION' '-D__STDC_FORMAT_MACROS' '-D_LARGEFILE_SOURCE' '-D_FILE_OFFSET_BITS=64' -I../wasm/include/node -I../wasm/src -I../wasm/deps/openssl/config -I../wasm/deps/openssl/openssl/include -I../wasm/deps/uv/include -I../wasm/deps/zlib -I../wasm/deps/v8/include -IC:/Users/toyobayashi/Projects/emnapi-node-gyp-test/node_modules/emnapi/include  -Wall -Wextra -Wno-unused-parameter -sDEFAULT_TO_CXX=0 -O3  -MMD -MF ./Release/.deps/Release/obj.target/binding/node_modules/emnapi/src/async_cleanup_hook.o.d.raw   -c
sed: -e expression #1, char 5: unterminated `s' command
  emcc.bat -o Release/obj.target/binding/node_modules/emnapi/src/async_context.o ../node_modules/emnapi/src/async_context.c '-DNODE_GYP_MODULE_NAME=binding' '-DUSING_UV_SHARED=1' '-DUSING_V8_SHARED=1' '-DV8_DEPRECATION_WARNINGS=1' '-DBUILDING_NODE_EXTENSION' '-D__STDC_FORMAT_MACROS' '-D_LARGEFILE_SOURCE' '-D_FILE_OFFSET_BITS=64' -I../wasm/include/node -I../wasm/src -I../wasm/deps/openssl/config -I../wasm/deps/openssl/openssl/include -I../wasm/deps/uv/include -I../wasm/deps/zlib -I../wasm/deps/v8/include -IC:/Users/toyobayashi/Projects/emnapi-node-gyp-test/node_modules/emnapi/include  -Wall -Wextra -Wno-unused-parameter -sDEFAULT_TO_CXX=0 -O3  -MMD -MF ./Release/.deps/Release/obj.target/binding/node_modules/emnapi/src/async_context.o.d.raw   -c
sed: -e expression #1, char 5: unterminated `s' command
  emcc.bat -o Release/obj.target/binding/node_modules/emnapi/src/async_work.o ../node_modules/emnapi/src/async_work.c '-DNODE_GYP_MODULE_NAME=binding' '-DUSING_UV_SHARED=1' '-DUSING_V8_SHARED=1' '-DV8_DEPRECATION_WARNINGS=1' '-DBUILDING_NODE_EXTENSION' '-D__STDC_FORMAT_MACROS' '-D_LARGEFILE_SOURCE' '-D_FILE_OFFSET_BITS=64' -I../wasm/include/node -I../wasm/src -I../wasm/deps/openssl/config -I../wasm/deps/openssl/openssl/include -I../wasm/deps/uv/include -I../wasm/deps/zlib -I../wasm/deps/v8/include -IC:/Users/toyobayashi/Projects/emnapi-node-gyp-test/node_modules/emnapi/include  -Wall -Wextra -Wno-unused-parameter -sDEFAULT_TO_CXX=0 -O3  -MMD -MF ./Release/.deps/Release/obj.target/binding/node_modules/emnapi/src/async_work.o.d.raw   -c
sed: -e expression #1, char 5: unterminated `s' command
  emcc.bat -o Release/obj.target/binding/node_modules/emnapi/src/threadsafe_function.o ../node_modules/emnapi/src/threadsafe_function.c '-DNODE_GYP_MODULE_NAME=binding' '-DUSING_UV_SHARED=1' '-DUSING_V8_SHARED=1' '-DV8_DEPRECATION_WARNINGS=1' '-DBUILDING_NODE_EXTENSION' '-D__STDC_FORMAT_MACROS' '-D_LARGEFILE_SOURCE' '-D_FILE_OFFSET_BITS=64' -I../wasm/include/node -I../wasm/src -I../wasm/deps/openssl/config -I../wasm/deps/openssl/openssl/include -I../wasm/deps/uv/include -I../wasm/deps/zlib -I../wasm/deps/v8/include -IC:/Users/toyobayashi/Projects/emnapi-node-gyp-test/node_modules/emnapi/include  -Wall -Wextra -Wno-unused-parameter -sDEFAULT_TO_CXX=0 -O3  -MMD -MF ./Release/.deps/Release/obj.target/binding/node_modules/emnapi/src/threadsafe_function.o.d.raw   -c
sed: -e expression #1, char 5: unterminated `s' command
  emcc.bat -o Release/obj.target/binding/node_modules/emnapi/src/uv/uv-common.o ../node_modules/emnapi/src/uv/uv-common.c '-DNODE_GYP_MODULE_NAME=binding' '-DUSING_UV_SHARED=1' '-DUSING_V8_SHARED=1' '-DV8_DEPRECATION_WARNINGS=1' '-DBUILDING_NODE_EXTENSION' '-D__STDC_FORMAT_MACROS' '-D_LARGEFILE_SOURCE' '-D_FILE_OFFSET_BITS=64' -I../wasm/include/node -I../wasm/src -I../wasm/deps/openssl/config -I../wasm/deps/openssl/openssl/include -I../wasm/deps/uv/include -I../wasm/deps/zlib -I../wasm/deps/v8/include -IC:/Users/toyobayashi/Projects/emnapi-node-gyp-test/node_modules/emnapi/include  -Wall -Wextra -Wno-unused-parameter -sDEFAULT_TO_CXX=0 -O3  -MMD -MF ./Release/.deps/Release/obj.target/binding/node_modules/emnapi/src/uv/uv-common.o.d.raw   -c
sed: -e expression #1, char 5: unterminated `s' command
  emcc.bat -o Release/obj.target/binding/node_modules/emnapi/src/uv/threadpool.o ../node_modules/emnapi/src/uv/threadpool.c '-DNODE_GYP_MODULE_NAME=binding' '-DUSING_UV_SHARED=1' '-DUSING_V8_SHARED=1' '-DV8_DEPRECATION_WARNINGS=1' '-DBUILDING_NODE_EXTENSION' '-D__STDC_FORMAT_MACROS' '-D_LARGEFILE_SOURCE' '-D_FILE_OFFSET_BITS=64' -I../wasm/include/node -I../wasm/src -I../wasm/deps/openssl/config -I../wasm/deps/openssl/openssl/include -I../wasm/deps/uv/include -I../wasm/deps/zlib -I../wasm/deps/v8/include -IC:/Users/toyobayashi/Projects/emnapi-node-gyp-test/node_modules/emnapi/include  -Wall -Wextra -Wno-unused-parameter -sDEFAULT_TO_CXX=0 -O3  -MMD -MF ./Release/.deps/Release/obj.target/binding/node_modules/emnapi/src/uv/threadpool.o.d.raw   -c
sed: -e expression #1, char 5: unterminated `s' command
  emcc.bat -o Release/obj.target/binding/node_modules/emnapi/src/uv/unix/loop.o ../node_modules/emnapi/src/uv/unix/loop.c '-DNODE_GYP_MODULE_NAME=binding' '-DUSING_UV_SHARED=1' '-DUSING_V8_SHARED=1' '-DV8_DEPRECATION_WARNINGS=1' '-DBUILDING_NODE_EXTENSION' '-D__STDC_FORMAT_MACROS' '-D_LARGEFILE_SOURCE' '-D_FILE_OFFSET_BITS=64' -I../wasm/include/node -I../wasm/src -I../wasm/deps/openssl/config -I../wasm/deps/openssl/openssl/include -I../wasm/deps/uv/include -I../wasm/deps/zlib -I../wasm/deps/v8/include -IC:/Users/toyobayashi/Projects/emnapi-node-gyp-test/node_modules/emnapi/include  -Wall -Wextra -Wno-unused-parameter -sDEFAULT_TO_CXX=0 -O3  -MMD -MF ./Release/.deps/Release/obj.target/binding/node_modules/emnapi/src/uv/unix/loop.o.d.raw   -c
sed: -e expression #1, char 5: unterminated `s' command
  emcc.bat -o Release/obj.target/binding/node_modules/emnapi/src/uv/unix/thread.o ../node_modules/emnapi/src/uv/unix/thread.c '-DNODE_GYP_MODULE_NAME=binding' '-DUSING_UV_SHARED=1' '-DUSING_V8_SHARED=1' '-DV8_DEPRECATION_WARNINGS=1' '-DBUILDING_NODE_EXTENSION' '-D__STDC_FORMAT_MACROS' '-D_LARGEFILE_SOURCE' '-D_FILE_OFFSET_BITS=64' -I../wasm/include/node -I../wasm/src -I../wasm/deps/openssl/config -I../wasm/deps/openssl/openssl/include -I../wasm/deps/uv/include -I../wasm/deps/zlib -I../wasm/deps/v8/include -IC:/Users/toyobayashi/Projects/emnapi-node-gyp-test/node_modules/emnapi/include  -Wall -Wextra -Wno-unused-parameter -sDEFAULT_TO_CXX=0 -O3  -MMD -MF ./Release/.deps/Release/obj.target/binding/node_modules/emnapi/src/uv/unix/thread.o.d.raw   -c
sed: -e expression #1, char 5: unterminated `s' command
  emcc.bat -o Release/obj.target/binding/node_modules/emnapi/src/uv/unix/async.o ../node_modules/emnapi/src/uv/unix/async.c '-DNODE_GYP_MODULE_NAME=binding' '-DUSING_UV_SHARED=1' '-DUSING_V8_SHARED=1' '-DV8_DEPRECATION_WARNINGS=1' '-DBUILDING_NODE_EXTENSION' '-D__STDC_FORMAT_MACROS' '-D_LARGEFILE_SOURCE' '-D_FILE_OFFSET_BITS=64' -I../wasm/include/node -I../wasm/src -I../wasm/deps/openssl/config -I../wasm/deps/openssl/openssl/include -I../wasm/deps/uv/include -I../wasm/deps/zlib -I../wasm/deps/v8/include -IC:/Users/toyobayashi/Projects/emnapi-node-gyp-test/node_modules/emnapi/include  -Wall -Wextra -Wno-unused-parameter -sDEFAULT_TO_CXX=0 -O3  -MMD -MF ./Release/.deps/Release/obj.target/binding/node_modules/emnapi/src/uv/unix/async.o.d.raw   -c
sed: -e expression #1, char 5: unterminated `s' command
  emcc.bat -o Release/obj.target/binding/node_modules/emnapi/src/uv/unix/core.o ../node_modules/emnapi/src/uv/unix/core.c '-DNODE_GYP_MODULE_NAME=binding' '-DUSING_UV_SHARED=1' '-DUSING_V8_SHARED=1' '-DV8_DEPRECATION_WARNINGS=1' '-DBUILDING_NODE_EXTENSION' '-D__STDC_FORMAT_MACROS' '-D_LARGEFILE_SOURCE' '-D_FILE_OFFSET_BITS=64' -I../wasm/include/node -I../wasm/src -I../wasm/deps/openssl/config -I../wasm/deps/openssl/openssl/include -I../wasm/deps/uv/include -I../wasm/deps/zlib -I../wasm/deps/v8/include -IC:/Users/toyobayashi/Projects/emnapi-node-gyp-test/node_modules/emnapi/include  -Wall -Wextra -Wno-unused-parameter -sDEFAULT_TO_CXX=0 -O3  -MMD -MF ./Release/.deps/Release/obj.target/binding/node_modules/emnapi/src/uv/unix/core.o.d.raw   -c
sed: -e expression #1, char 5: unterminated `s' command
  emcc.bat -o Release/obj.target/binding/src/binding.o ../src/binding.c '-DNODE_GYP_MODULE_NAME=binding' '-DUSING_UV_SHARED=1' '-DUSING_V8_SHARED=1' '-DV8_DEPRECATION_WARNINGS=1' '-DBUILDING_NODE_EXTENSION' '-D__STDC_FORMAT_MACROS' '-D_LARGEFILE_SOURCE' '-D_FILE_OFFSET_BITS=64' -I../wasm/include/node -I../wasm/src -I../wasm/deps/openssl/config -I../wasm/deps/openssl/openssl/include -I../wasm/deps/uv/include -I../wasm/deps/zlib -I../wasm/deps/v8/include -IC:/Users/toyobayashi/Projects/emnapi-node-gyp-test/node_modules/emnapi/include  -Wall -Wextra -Wno-unused-parameter -sDEFAULT_TO_CXX=0 -O3  -MMD -MF ./Release/.deps/Release/obj.target/binding/src/binding.o.d.raw   -c
sed: -e expression #1, char 5: unterminated `s' command
  em++.bat -o Release/binding.node.js --js-library=C:/Users/toyobayashi/Projects/emnapi-node-gyp-test/node_modules/emnapi/dist/library_napi.js -sALLOW_MEMORY_GROWTH=1 -sEXPORTED_FUNCTIONS=['_malloc','_free','_napi_register_wasm_v1','_node_api_module_get_api_version_v1'] -sNODEJS_CATCH_EXIT=0 -sNODEJS_CATCH_REJECTION=0 -sAUTO_JS_LIBRARIES=0 -sAUTO_NATIVE_LIBRARIES=0 -sWASM_BIGINT=1 -sMIN_CHROME_VERSION=84 -sSTACK_SIZE=2MB -sDEFAULT_PTHREAD_STACK_SIZE=2MB -sMODULARIZE=1 -sEXPORT_NAME=binding -O3  -Wl,--start-group ./Release/obj.target/binding/node_modules/emnapi/src/js_native_api.o ./Release/obj.target/binding/node_modules/emnapi/src/node_api.o ./Release/obj.target/binding/node_modules/emnapi/src/async_cleanup_hook.o ./Release/obj.target/binding/node_modules/emnapi/src/async_context.o ./Release/obj.target/binding/node_modules/emnapi/src/async_work.o ./Release/obj.target/binding/node_modules/emnapi/src/threadsafe_function.o ./Release/obj.target/binding/node_modules/emnapi/src/uv/uv-common.o ./Release/obj.target/binding/node_modules/emnapi/src/uv/threadpool.o ./Release/obj.target/binding/node_modules/emnapi/src/uv/unix/loop.o ./Release/obj.target/binding/node_modules/emnapi/src/uv/unix/thread.o ./Release/obj.target/binding/node_modules/emnapi/src/uv/unix/async.o ./Release/obj.target/binding/node_modules/emnapi/src/uv/unix/core.o ./Release/obj.target/binding/src/binding.o  -Wl,--end-group
mingw32-make.EXE: Leaving directory 'C:/Users/toyobayashi/Projects/emnapi-node-gyp-test/build'
```

</details>

<details>
<summary>✅ WSL 2 Ubuntu 20.04</summary><br />

```
$ npm install --ignore-scripts

added 3 packages in 418ms

$ node-gyp clean
gyp info it worked if it ends with ok
gyp info using node-gyp@9.3.1
gyp info using node@18.14.0 | linux | x64
gyp info ok

$ node-gyp configure --nodedir=./wasm -- -f make
gyp info it worked if it ends with ok
gyp info using node-gyp@9.3.1
gyp info using node@18.14.0 | linux | x64
gyp info find Python using Python version 3.8.10 found at "/usr/bin/python3"
gyp WARN read config.gypi ENOENT: no such file or directory, open '/home/toyobayashi/Projects/emnapi-node-gyp-test/wasm/include/node/config.gypi'
gyp info spawn /usr/bin/python3
gyp info spawn args [
gyp info spawn args   '/home/toyobayashi/.nvm/versions/node/v18.14.0/lib/node_modules/node-gyp/gyp/gyp_main.py',
gyp info spawn args   'binding.gyp',
gyp info spawn args   '-f',
gyp info spawn args   'make',
gyp info spawn args   '-I',
gyp info spawn args   '/home/toyobayashi/Projects/emnapi-node-gyp-test/build/config.gypi',
gyp info spawn args   '-I',
gyp info spawn args   '/home/toyobayashi/.nvm/versions/node/v18.14.0/lib/node_modules/node-gyp/addon.gypi',
gyp info spawn args   '-I',
gyp info spawn args   '/home/toyobayashi/Projects/emnapi-node-gyp-test/wasm/common.gypi',
gyp info spawn args   '-Dlibrary=shared_library',
gyp info spawn args   '-Dvisibility=default',
gyp info spawn args   '-Dnode_root_dir=./wasm',
gyp info spawn args   '-Dnode_gyp_dir=/home/toyobayashi/.nvm/versions/node/v18.14.0/lib/node_modules/node-gyp',
gyp info spawn args   '-Dnode_lib_file=wasm/$(Configuration)/node.lib',
gyp info spawn args   '-Dmodule_root_dir=/home/toyobayashi/Projects/emnapi-node-gyp-test',
gyp info spawn args   '-Dnode_engine=v8',
gyp info spawn args   '--depth=.',
gyp info spawn args   '--no-parallel',
gyp info spawn args   '--generator-output',
gyp info spawn args   'build',
gyp info spawn args   '-Goutput_dir=.'
gyp info spawn args ]
gyp info ok

$ emmake make -C build
make: make -C build
make: Entering directory '/home/toyobayashi/Projects/emnapi-node-gyp-test/build'
  CC(target) Release/obj.target/binding/node_modules/emnapi/src/js_native_api.o
  CC(target) Release/obj.target/binding/node_modules/emnapi/src/node_api.o
  CC(target) Release/obj.target/binding/node_modules/emnapi/src/emnapi.o
  CC(target) Release/obj.target/binding/node_modules/emnapi/src/async_cleanup_hook.o
  CC(target) Release/obj.target/binding/node_modules/emnapi/src/async_context.o
  CC(target) Release/obj.target/binding/node_modules/emnapi/src/async_work.o
  CC(target) Release/obj.target/binding/node_modules/emnapi/src/threadsafe_function.o
  CC(target) Release/obj.target/binding/node_modules/emnapi/src/uv/uv-common.o
  CC(target) Release/obj.target/binding/node_modules/emnapi/src/uv/threadpool.o
  CC(target) Release/obj.target/binding/node_modules/emnapi/src/uv/unix/loop.o
  CC(target) Release/obj.target/binding/node_modules/emnapi/src/uv/unix/thread.o
  CC(target) Release/obj.target/binding/node_modules/emnapi/src/uv/unix/async.o
  CC(target) Release/obj.target/binding/node_modules/emnapi/src/uv/unix/core.o
  CC(target) Release/obj.target/binding/src/binding.o
  LINK(target) Release/binding.js
em++: warning: USE_PTHREADS + ALLOW_MEMORY_GROWTH may run non-wasm code slowly, see https://github.com/WebAssembly/design/issues/1271 [-Wpthreads-mem-growth]
cache:INFO: generating system asset: symbol_lists/7f16a0cf42f34d504060010d577a8705337deb0d.txt... (this will be cached in "/home/toyobayashi/Projects/emsdk/upstream/emscripten/cache/symbol_lists/7f16a0cf42f34d504060010d577a8705337deb0d.txt" for subsequent builds)
cache:INFO:  - ok
make: Leaving directory '/home/toyobayashi/Projects/emnapi-node-gyp-test/build'
```

</details>

<details>
<summary>✅ macOS 14.1.2</summary><br />

Add the following environment variables:

```bash
GYP_CROSSCOMPILE=1
AR_host=ar
CC_host=clang
CXX_host=clang++
AR_target=emar
CC_target=emcc
CXX_target=em++
```

```
$ npm install --ignore-scripts

added 3 packages in 593ms

$ node-gyp clean
gyp info it worked if it ends with ok
gyp info using node-gyp@10.0.1
gyp info using node@20.10.0 | darwin | arm64
gyp info ok 

$ node-gyp configure --nodedir=./wasm -- -f make
gyp info it worked if it ends with ok
gyp info using node-gyp@10.0.1
gyp info using node@20.10.0 | darwin | arm64
gyp info find Python using Python version 3.9.6 found at "/Applications/Xcode.app/Contents/Developer/usr/bin/python3"
gyp WARN read config.gypi ENOENT: no such file or directory, open '/Users/toyobayashi/code/github/emnapi-node-gyp-test/wasm/include/node/config.gypi'
gyp info spawn /Applications/Xcode.app/Contents/Developer/usr/bin/python3
gyp info spawn args [
gyp info spawn args '/Users/toyobayashi/.nvm/versions/node/v20.10.0/lib/node_modules/node-gyp/gyp/gyp_main.py',
gyp info spawn args 'binding.gyp',
gyp info spawn args '-f',
gyp info spawn args 'make',
gyp info spawn args '-I',
gyp info spawn args '/Users/toyobayashi/code/github/emnapi-node-gyp-test/build/config.gypi',
gyp info spawn args '-I',
gyp info spawn args '/Users/toyobayashi/.nvm/versions/node/v20.10.0/lib/node_modules/node-gyp/addon.gypi',
gyp info spawn args '-I',
gyp info spawn args '/Users/toyobayashi/code/github/emnapi-node-gyp-test/wasm/common.gypi',
gyp info spawn args '-Dlibrary=shared_library',
gyp info spawn args '-Dvisibility=default',
gyp info spawn args '-Dnode_root_dir=./wasm',
gyp info spawn args '-Dnode_gyp_dir=/Users/toyobayashi/.nvm/versions/node/v20.10.0/lib/node_modules/node-gyp',
gyp info spawn args '-Dnode_lib_file=wasm/$(Configuration)/node.lib',
gyp info spawn args '-Dmodule_root_dir=/Users/toyobayashi/code/github/emnapi-node-gyp-test',
gyp info spawn args '-Dnode_engine=v8',
gyp info spawn args '--depth=.',
gyp info spawn args '--no-parallel',
gyp info spawn args '--generator-output',
gyp info spawn args 'build',
gyp info spawn args '-Goutput_dir=.'
gyp info spawn args ]
gyp info ok 

$ emmake make -C build
make: node-gyp build
gyp info it worked if it ends with ok
gyp info using node-gyp@10.0.1
gyp info using node@20.10.0 | darwin | arm64
gyp info spawn make
gyp info spawn args [ 'BUILDTYPE=Release', '-C', 'build' ]
  CC(target) Release/obj.target/binding/node_modules/emnapi/src/js_native_api.o
  CC(target) Release/obj.target/binding/node_modules/emnapi/src/node_api.o
  CC(target) Release/obj.target/binding/node_modules/emnapi/src/async_cleanup_hook.o
  CC(target) Release/obj.target/binding/node_modules/emnapi/src/async_context.o
  CC(target) Release/obj.target/binding/node_modules/emnapi/src/async_work.o
  CC(target) Release/obj.target/binding/node_modules/emnapi/src/threadsafe_function.o
  CC(target) Release/obj.target/binding/node_modules/emnapi/src/uv/uv-common.o
  CC(target) Release/obj.target/binding/node_modules/emnapi/src/uv/threadpool.o
  CC(target) Release/obj.target/binding/node_modules/emnapi/src/uv/unix/loop.o
  CC(target) Release/obj.target/binding/node_modules/emnapi/src/uv/unix/thread.o
  CC(target) Release/obj.target/binding/node_modules/emnapi/src/uv/unix/async.o
  CC(target) Release/obj.target/binding/node_modules/emnapi/src/uv/unix/core.o
  CC(target) Release/obj.target/binding/src/binding.o
  LINK(target) Release/binding.js
gyp info ok 
```

</details>

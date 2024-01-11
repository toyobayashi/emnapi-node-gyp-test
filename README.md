```bash
npm install --ignore-scripts
node-gyp clean
node-gyp configure --nodedir=./wasm -- -f make
emmake make -C build
```

## Log

<details>
<summary>❌ Windows 11 22H2 22621.1413</summary><br />

Failed due to the generated Makefile still use unix tools, even if execute make under WSL 2 then failed due to `\\` path seperator.

```
> npm install --ignore-scripts

add 3 packages, and audited 4 packages in 8s

found 0 vulnerabilities

> node-gyp clean
gyp info it worked if it ends with ok
gyp info using node-gyp@9.3.1
gyp info using node@18.12.1 | win32 | x64
gyp info ok

> node-gyp configure --nodedir=./wasm -- -f make
gyp info it worked if it ends with ok
gyp info using node-gyp@9.3.1
gyp info using node@18.12.1 | win32 | x64
gyp info find Python using Python version 3.9.7 found at "C:\Users\toyobayashi\AppData\Local\Programs\Python\Python39\python.exe"
gyp info find VS using VS2022 (17.2.32516.85) found at:
gyp info find VS "C:\Program Files\Microsoft Visual Studio\2022\Community"
gyp info find VS run with --verbose for detailed information
gyp WARN read config.gypi ENOENT: no such file or directory, open 'C:\Users\toyobayashi\Projects\emnapi-node-gyp-test\wasm\include\node\config.gypi'
gyp info spawn C:\Users\toyobayashi\AppData\Local\Programs\Python\Python39\python.exe
gyp info spawn args [
gyp info spawn args   'C:\\Users\\toyobayashi\\app\\nvm\\v18.12.1\\node_modules\\node-gyp\\gyp\\gyp_main.py',
gyp info spawn args   'binding.gyp',
gyp info spawn args   '-f',
gyp info spawn args   'make',
gyp info spawn args   '-I',
gyp info spawn args   'C:\\Users\\toyobayashi\\Projects\\emnapi-node-gyp-test\\build\\config.gypi',
gyp info spawn args   '-I',
gyp info spawn args   'C:\\Users\\toyobayashi\\app\\nvm\\v18.12.1\\node_modules\\node-gyp\\addon.gypi',
gyp info spawn args   '-I',
gyp info spawn args   'C:\\Users\\toyobayashi\\Projects\\emnapi-node-gyp-test\\wasm\\common.gypi',
gyp info spawn args   '-Dlibrary=shared_library',
gyp info spawn args   '-Dvisibility=default',
gyp info spawn args   '-Dnode_root_dir=./wasm',
gyp info spawn args   '-Dnode_gyp_dir=C:\\Users\\toyobayashi\\app\\nvm\\v18.12.1\\node_modules\\node-gyp',
gyp info spawn args   '-Dnode_lib_file=wasm\\\\$(Configuration)\\\\node.lib',
gyp info spawn args   '-Dmodule_root_dir=C:\\Users\\toyobayashi\\Projects\\emnapi-node-gyp-test',
gyp info spawn args   '-Dnode_engine=v8',
gyp info spawn args   '--depth=.',
gyp info spawn args   '--no-parallel',
gyp info spawn args   '--generator-output',
gyp info spawn args   'C:\\Users\\toyobayashi\\Projects\\emnapi-node-gyp-test\\build',
gyp info spawn args   '-Goutput_dir=.'
gyp info spawn args ]
gyp info ok

> emmake make -C build
make: C:\Users\toyobayashi\app\make\mingw32-make.exe -C build
mingw32-make: Entering directory 'C:/Users/toyobayashi/Projects/emnapi-node-gyp-test/build'
process_begin: CreateProcess(NULL, printf %s\n "  CC(target) Release/obj.target/binding/node_modules\emnapi\src\js_native_api.o", ...) failed.
make (e=2): 系统找不到指定的文件。
mingw32-make: *** [binding.target.mk:110: Release/obj.target/binding/node_modules\emnapi\src\js_native_api.o] Error 2
mingw32-make: Leaving directory 'C:/Users/toyobayashi/Projects/emnapi-node-gyp-test/build'
emmake: error: 'C:\Users\toyobayashi\app\make\mingw32-make.exe -C build' failed (returned 2)

> wsl
$ emmake make -C build
make: make -C build
make: Entering directory '/mnt/c/Users/toyobayashi/Projects/emnapi-node-gyp-test/build'
make: *** No rule to make target '../wasm\common.gypi', needed by 'Makefile'.  Stop.
make: Leaving directory '/mnt/c/Users/toyobayashi/Projects/emnapi-node-gyp-test/build'
emmake: error: 'make -C build' failed (returned 2)
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

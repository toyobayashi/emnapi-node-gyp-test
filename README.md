```bash
node-gyp clean
node-gyp configure --nodedir=./wasm -- -f make
emmake make -C build
```

## Log

<details>
<summary>Windows</summary><br />

```
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

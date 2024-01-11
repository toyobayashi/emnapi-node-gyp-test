# This file is originally created by [RReverser](https://github.com/RReverser)
# in https://github.com/lovell/sharp/pull/3522
{
  'variables': {
    'OS': 'emscripten',
    'napi_build_version%': '8',
    'clang': 1,
    'target_arch%': 'wasm32',
    'wasm_threads%': 0,
    'pthread_pool_size%': 4,
    'product_extension%': 'js',
  },

  'target_defaults': {
    'type': 'executable',
    'product_extension': '<(product_extension)',

    'cflags': [
      '-Wall',
      '-Wextra',
      '-Wno-unused-parameter',
      '-sDEFAULT_TO_CXX=0',
    ],
    'cflags_cc': [
      '-fno-rtti',
      '-fno-exceptions',
      '-std=gnu++17'
    ],
    'ldflags': [
      '--js-library=<!(node -p "require(\'emnapi\').js_library")',
      "-sALLOW_MEMORY_GROWTH=1",
      "-sEXPORTED_FUNCTIONS=['_malloc','_free','_napi_register_wasm_v1','_node_api_module_get_api_version_v1']",
      '-sNODEJS_CATCH_EXIT=0',
      '-sNODEJS_CATCH_REJECTION=0',
      '-sAUTO_JS_LIBRARIES=0',
      '-sAUTO_NATIVE_LIBRARIES=0',
      '-sWASM_BIGINT=1',
      '-sMIN_CHROME_VERSION=84',
      '-sSTACK_SIZE=2MB',
      '-sDEFAULT_PTHREAD_STACK_SIZE=2MB',
    ],
    'xcode_settings': {
      # WARNING_CFLAGS == cflags
      # OTHER_CFLAGS == cflags_c
      # OTHER_CPLUSPLUSFLAGS == cflags_cc
      # OTHER_LDFLAGS == ldflags

      'CLANG_CXX_LANGUAGE_STANDARD': 'gnu++17',
      'GCC_ENABLE_CPP_RTTI': 'NO',
      'GCC_ENABLE_CPP_EXCEPTIONS': 'NO',
      'WARNING_CFLAGS': [
        '-Wall',
        '-Wextra',
        '-Wno-unused-parameter',
        '-sDEFAULT_TO_CXX=0',
      ],
      'OTHER_LDFLAGS': [
        '--js-library=<!(node -p "require(\'emnapi\').js_library")',
        "-sALLOW_MEMORY_GROWTH=1",
        "-sEXPORTED_FUNCTIONS=['_malloc','_free','_napi_register_wasm_v1','_node_api_module_get_api_version_v1']",
        '-sNODEJS_CATCH_EXIT=0',
        '-sNODEJS_CATCH_REJECTION=0',
        '-sAUTO_JS_LIBRARIES=0',
        '-sAUTO_NATIVE_LIBRARIES=0',
        '-sWASM_BIGINT=1',
        '-sMIN_CHROME_VERSION=84',
        '-sSTACK_SIZE=2MB',
        '-sDEFAULT_PTHREAD_STACK_SIZE=2MB',
      ],
    },
    'defines': [
      'BUILDING_NODE_EXTENSION',
      '__STDC_FORMAT_MACROS',
    ],
    'include_dirs': [
      '<!(node -p "require(\'emnapi\').include")',
    ],
    'sources': [
      '<!@(node -p "require(\'emnapi\').sources.map(x => JSON.stringify(path.relative(process.cwd(), x))).join(\' \')")'
    ],

    'default_configuration': 'Release',
    'configurations': {
      'Debug': {
        'defines': [ 'DEBUG', '_DEBUG' ],
        'cflags': [ '-g', '-O0' ],
        'ldflags': [ '-g', '-O0', '-sSAFE_HEAP=1' ],
        'xcode_settings': {
          'WARNING_CFLAGS': [ '-g', '-O0' ],
          'OTHER_LDFLAGS': [ '-g', '-O0', '-sSAFE_HEAP=1' ],
        },
      },
      'Release': {
        'cflags': [ '-O3' ],
        'ldflags': [ '-O3' ],
        'xcode_settings': {
          'WARNING_CFLAGS': [ '-O3' ],
          'OTHER_LDFLAGS': [ '-O3' ],
        },
      }
    },

    'conditions': [
      ['target_arch == "wasm64"', {
        'cflags': [ '-sMEMORY64=1' ],
        'ldflags': [ '-sMEMORY64=1' ],
        'xcode_settings': {
          'WARNING_CFLAGS': [ '-sMEMORY64=1' ],
          'OTHER_LDFLAGS': [ '-sMEMORY64=1' ],
        },
      }],
      ['wasm_threads != 0', {
        'cflags': [ '-pthread' ],
        'ldflags': [
          '-pthread',
          '-sPTHREAD_POOL_SIZE=<(pthread_pool_size)',
        ],
        'xcode_settings': {
          'WARNING_CFLAGS': [ '-pthread' ],
          'OTHER_LDFLAGS': [
            '-pthread',
            '-sPTHREAD_POOL_SIZE=<(pthread_pool_size)',
          ],
        },
      }],
    ],
  }
}

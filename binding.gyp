{
  "targets": [
    {
      "target_name": "binding",
      "sources": [
        "src/binding.c",
        "src/hello.cpp",
      ],
      'dependencies': [
        "<!(node -p \"require('node-addon-api').targets\"):node_addon_api",
      ],
      "conditions": [
        [
          "OS == 'emscripten'",
          {
            "product_extension": "node.js",
            "ldflags": [
              '-sMODULARIZE=1',
              '-sEXPORT_NAME=binding'
            ],
            'xcode_settings': {
              'OTHER_LDFLAGS': [
                '-sMODULARIZE=1',
                '-sEXPORT_NAME=binding'
              ]
            },
            'conditions': [
              ['emnapi_manual_linking != 0', {
                'dependencies': [
                  '<!(node -p "require(\'emnapi\').targets"):emnapi'
                ]
              }]
            ]
          },
        ],
        ["OS in ' unknown'", {
          'conditions': [
            ['emnapi_manual_linking != 0', {
              'dependencies': [
                '<!(node -p "require(\'emnapi\').targets"):dlmalloc',
                '<!(node -p "require(\'emnapi\').targets"):emnapi_basic'
              ],
            }]
          ]
        }],
        ["OS == 'wasi'", {
          'conditions': [
            ['emnapi_manual_linking != 0', {
              'conditions': [
                ['wasm_threads != 0', {
                  'dependencies': [
                    '<!(node -p "require(\'emnapi\').targets"):emnapi'
                  ],
                }, {
                  'dependencies': [
                    '<!(node -p "require(\'emnapi\').targets"):emnapi_basic'
                  ],
                }]
              ]
            }]
          ]
        }]
      ]
    }
  ]
}

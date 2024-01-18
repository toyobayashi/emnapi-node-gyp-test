{
  "variables": {
    "cross_compiling%": 0,
  },
  "targets": [
    {
      "target_name": "binding",
      "sources": [
        "src/binding.c"
      ],
      "conditions": [
        ["cross_compiling != 0", {
          'conditions': [
            [
              "target_os == 'emscripten'",
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
                }
              },
              # {
              #   'conditions': [
              #     ["target_os == 'wasi'", {}, {
              #       'dependencies': [
              #         '<!(node -p "require(\'emnapi\').targets"):dlmalloc'
              #       ]
              #     }]
              #   ]
              # }
            ]
          ]
        }]
      ]
    }
  ]
}

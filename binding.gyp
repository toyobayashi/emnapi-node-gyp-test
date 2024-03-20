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
            }
          },
          # {
          #   'conditions': [
          #     ["OS == 'unknown'", {
          #       'dependencies': [
          #         '<!(node -p "require(\'emnapi\').targets"):dlmalloc'
          #       ]
          #     }]
          #   ]
          # }
        ]
      ]
    }
  ]
}

{
  "targets": [
    {
      "target_name": "binding",
      "sources": [
        "src/binding.c"
      ],
      "conditions": [
        [
          "OS == 'emscripten'",
          {
            "target_name": "binding.node",
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

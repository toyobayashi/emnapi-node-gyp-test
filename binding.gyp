{
  "targets": [
    {
      "target_name": "binding",
      "sources": [
        "src/binding.c"
      ],
      "conditions": [
        ["OS == 'emscripten'", {
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
        }]
      ]
    }
  ]
}

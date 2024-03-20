(function () {
  let fs, WASI, emnapiCore

  const nodeWorkerThreads = require('worker_threads')

  const parentPort = nodeWorkerThreads.parentPort

  parentPort.on('message', (data) => {
    globalThis.onmessage({ data })
  })

  fs = require('fs')

  Object.assign(globalThis, {
    self: globalThis,
    require,
    Worker: nodeWorkerThreads.Worker,
    importScripts: function (f) {
      (0, eval)(fs.readFileSync(f, 'utf8') + '//# sourceURL=' + f)
    },
    postMessage: function (msg) {
      parentPort.postMessage(msg)
    }
  })

  WASI = require('wasi').WASI
  emnapiCore = require('@emnapi/core')

  const { instantiateNapiModuleSync, MessageHandler } = emnapiCore

  const handler = new MessageHandler({
    onLoad ({ wasmModule, wasmMemory }) {
      const wasi = new WASI({ version: 'preview1' })

      return instantiateNapiModuleSync(wasmModule, {
        childThread: true,
        wasi,
        overwriteImports (importObject) {
          importObject.env.memory = wasmMemory
        }
      })
    }
  })

  globalThis.onmessage = function (e) {
    handler.handle(e)
  }
})()

const path = require('path')
const fs = require('fs')
const emnapi = require('@emnapi/runtime')

const entry = (() => {
  try {
    return require.resolve('./build/Release/binding.node')
  } catch (_) {
    return require.resolve('./build/Release/binding.wasm')
  }
})()

const ext = path.extname(entry)

module.exports = function () {
  if (ext === '.js') {
    return require(entry)().then(Module => {
      return Module.emnapiInit({ context: emnapi.getDefaultContext() })
    })
  }
  if (ext === '.node') {
    return Promise.resolve().then(() => require(entry))
  }
  if (ext === '.wasm') {
    const { instantiateNapiModule } = require('@emnapi/core')
    return instantiateNapiModule(fs.readFileSync(entry), {
      context: emnapi.getDefaultContext(),
      wasi: new (require('wasi').WASI)({ version: 'preview1' }),
      overwriteImports (imports) {
        imports.env.memory = new WebAssembly.Memory({
          initial: 16777216 / 65536,
          maximum: 2147483648 / 65536,
          shared: true
        })
      },
      onCreateWorker () {
        return new (require('worker_threads').Worker)(path.join(__dirname, './worker.js'), {
          env: process.env,
          execArgv: ['--experimental-wasi-unstable-preview1']
        })
      }
    }).then(({ napiModule }) => napiModule.exports)
  }
}

const path = require('path')
const emnapi = require('@emnapi/runtime')

const ext = path.extname(require.resolve('./build/Release/binding.node'))
const init = require('./build/Release/binding.node')

module.exports = function () {
  if (ext === '.js') {
    return init().then(Module => {
      return Module.emnapiInit({ context: emnapi.getDefaultContext() })
    })
  }
  return Promise.resolve().then(() => init)
}

const init = require('.')

init().then(binding => {
  console.log(binding.hello())
})

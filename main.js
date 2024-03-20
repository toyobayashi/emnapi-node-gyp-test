const init = require('.')
const assert = require('assert')

init().then(binding => {
  const input = 'input'
  const result = binding.echoSync(input)
  console.log(`binding.echoSync('${input}') ==> '${result}'`)
  assert.strictEqual(binding.echoSync(input), input)

  if (typeof binding.echo === 'function') {
    const testAsyncEcho = (input) => {
      return new Promise((resolve, reject) => {
        const progress = []
        binding.echo(
          input,
          function okCallback (err, result) {
            if (err) {
              reject(err)
            } else {
              if (progress.length !== 6) {
                reject(new Error('Must call progress callback'))
              } else {
                resolve(result)
              }
            }
          },
          function progressCallback (i) {
            console.log(`binding.echo() progress: ${i}`)
            progress.push(i)
          }
        )
      })
    }
    return testAsyncEcho(input).then(result => {
      console.log(`await binding.echo('${input}') ==> '${result}'`)
      assert.strictEqual(result, input)
    })
  }
}).catch(err => {
  console.error(err)
  process.exitCode = 1
})

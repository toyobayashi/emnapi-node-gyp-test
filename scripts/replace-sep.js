const path = require('path')
const fs = require('fs')

const buildDir = path.join(__dirname, '../build')

fs.readdirSync(buildDir)
  .filter(p => p.endsWith('.target.mk'))
  .map((p) => path.join(buildDir, p))
  .map((p) => {
    const content = fs.readFileSync(p, 'utf8').replace(/\\|\\\\/g, '/').replace(/\/(\r?\n)/g, '\\$1')
    fs.writeFileSync(p, content, 'utf8')
  })

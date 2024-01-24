const { join } = require('path')
const { spawnSync } = require('child_process')

spawnSync('patch', ['-p1', '-i', join(__dirname, '../patches/node-gyp.patch')], {
  cwd: join(__dirname, '../node_modules/node-gyp/gyp'),
  stdio: 'inherit'
})

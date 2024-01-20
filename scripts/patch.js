const { join } = require('path')
const { spawnSync } = require('child_process')

spawnSync('patch', ['-p3', '-i', join(__dirname, '../patches/emnapi.patch')], {
  cwd: join(__dirname, '../node_modules/emnapi'),
  stdio: 'inherit'
})

spawnSync('patch', ['-p1', '-i', join(__dirname, '../patches/node-gyp.patch')], {
  cwd: join(__dirname, '../node_modules/node-gyp/gyp'),
  stdio: 'inherit'
})
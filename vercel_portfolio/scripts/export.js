const { exportApp } = require('next/dist/export')
const { join } = require('path')

const exportPathMap = async () => {
  return {
    '/': { page: '/' },
    '/workflow': { page: '/workflow' },
    '/documentation': { page: '/documentation' },
  }
}

exportApp({
  distDir: join(__dirname, '.next'),
  exportPathMap,
  outDir: join(__dirname, 'out'),
}).catch(err => {
  console.error(err)
  process.exit(1)
})

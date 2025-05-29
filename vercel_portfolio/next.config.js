const path = require('path')

module.exports = {
  reactStrictMode: true,
  images: {
    domains: ['localhost'],
  },
  webpack: (config) => {
    config.resolve.alias['@'] = path.join(__dirname, 'src')
    return config
  },
  output: 'export',
  trailingSlash: true,
  basePath: '/',
  assetPrefix: process.env.VERCEL_URL ? `https://${process.env.VERCEL_URL}` : ''
}

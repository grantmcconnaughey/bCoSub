var BundleTracker = require('webpack-bundle-tracker')
var WriteFilePlugin = require('write-file-webpack-plugin')
var path = require('path')

module.exports = {
  configureWebpack: {
    // Merged into the final Webpack config
    plugins: [
      new BundleTracker({filename: './webpack-stats.json'}),
      new WriteFilePlugin()
    ],
    entry: './src/main.js',
    output: {
      filename: 'bundle.js'
    },
  },
  // Local deployment
  // baseUrl: '/static'

  // Zappa deployment
  baseUrl: 'https://zappa-bcobucket1.s3.amazonaws.com'

}
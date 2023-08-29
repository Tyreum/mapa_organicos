const path = require('path');

module.exports = {
  entry: {
    accounts : "./accounts/static/js/src/index.js",
    home : "./accounts/static/js/src/index.js"
  },
  output: {
    path: path.resolve(__dirname, 'apps', 'static', 'assets', 'js'),
    filename: '[name]/static/js/build/bundle.js',
  },
};
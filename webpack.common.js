const path = require('path');

module.exports = {
  entry: {
    accounts : "./accounts/static/js/src/index.js",
    home : "./home/static/js/src/index.js"
  },
  output: {
    path: path.resolve(__dirname),
    filename: '[name]/static/js/build/[name].bundle.js',
  },
};
const path = require('path');
module.exports = {
    mode: "production",
    entry: "./src/main.js",
    output: {
        filename: "main.js",
        path: path.resolve(__dirname, "Dist")
    },
    module:{
        rules:[{
            test: /\.m?js$/,
            exclude: /(node_modules|bower_components)/,
            use:{
                loader:"babel-loader",
                options: {
                    presets: ['@babel/preset-env','@babel/preset-react']
                }
            }
        }]
    },
};
module.exports = {
  "transpileDependencies": [
    "vuetify"
  ],

  devServer: {
    proxy: {
       "^/api": {
       target: "http://127.0.0.1:5001",
        changeOrigin: true,
        logLevel: "debug",
         pathRewrite: { "^/api": "/api" }
    }
    },
    port: 80
  }

}
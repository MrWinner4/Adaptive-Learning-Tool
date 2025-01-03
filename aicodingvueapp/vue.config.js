const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    host: 'localhost', // Use the current IP address or 'localhost' if needed
    port: 8080, // Port for the development server
    hot: true, // Enable Hot Module Replacement
    liveReload: true, // Enable live reload
  },
});

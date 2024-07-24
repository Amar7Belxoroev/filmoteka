// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },

  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  vite: {
    server: {
        hmr: {
            clientPort: 3000
        }
    }
},
  sourcemap: {
    server: true,
    client: true
  },
  modules: ["@nuxtjs/tailwindcss", "nuxt-quasar-ui"],
  runtimeConfig: {
    public: {
      baseURL: 'https://api.kinopoisk.dev/v1.4/',
      apiKey: '15J7J4N-MRP4G4J-QKJ99FP-TGR00BT'
    },
  },
  
})
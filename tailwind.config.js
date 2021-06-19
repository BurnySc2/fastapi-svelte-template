module.exports = {
    // mode: 'jit',
    purge: [],
    purge: {
      content: [
        "./src/**/*.svelte",
        ],
        enabled: process.env.DEVELOPMENT !== "true" // disable purge in dev
    },
    theme: {
      extend: {},
    },
    variants: {},
    plugins: [],
  };
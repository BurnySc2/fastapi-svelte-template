module.exports = {
    // mode: 'jit',
    purge: [],
    purge: {
      content: [
        "./src/**/*.{html,svelte}",
        ],
        enabled: process.env.DEVELOPMENT !== "true" // disable purge in dev
    },
    theme: {
      extend: {},
    },
    variants: {},
    plugins: [],
  };
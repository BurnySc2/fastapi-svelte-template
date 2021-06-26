module.exports = {
    purge: {
        content: ["./src/**/*.svelte"],
        enabled: process.env.DEVELOPMENT !== "true", // disable purge in dev
    },
    theme: {
        extend: {},
    },
    variants: {},
    plugins: [],
}

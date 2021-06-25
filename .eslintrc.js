module.exports = {
    env: {
        browser: true,
        es2021: true,
        node: true,
    },
    extends: [
        "eslint:recommended",
        "plugin:@typescript-eslint/recommended",
    ],
    parser: "@typescript-eslint/parser",
    parserOptions: {
        ecmaFeatures: {
            jsx: true,
        },
        ecmaVersion: 12,
        sourceType: "module",
    },
    plugins: ['svelte3', "@typescript-eslint"],
    overrides: [
      {
        files: ['**/*.svelte'],
        processor: 'svelte3/svelte3'
      }
    ],
    rules: {
        "@typescript-eslint/ban-ts-comment": 0,
    },
    settings: {
      'svelte3/typescript': () => require('typescript'), // pass the TypeScript package to the Svelte plugin
      // OR
      'svelte3/typescript': true, // load TypeScript as peer dependency
      // ...
    }
}

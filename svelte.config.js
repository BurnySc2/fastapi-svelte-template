import preprocess from 'svelte-preprocess'
import adapter from '@sveltejs/adapter-static'
const dev = process.env.NODE_ENV === 'development'

/** @type {import('@sveltejs/kit').Config} */
const config = {
    // Consult https://github.com/sveltejs/svelte-preprocess
    // for more information about preprocessors
    preprocess: preprocess(),

    kit: {
        // hydrate the <div id="svelte"> element in src/app.html
        target: '#svelte',
        adapter: adapter({
            // default options are shown
            pages: 'build',
            assets: 'build',
            fallback: null
        }),
        paths: {
            base: dev ? '' : '/fastapi-svelte-template'
        },
        appDir: 'internal'
    }
}

export default config

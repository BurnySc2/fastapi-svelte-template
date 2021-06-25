<script>
    let searchTerm = ""
</script>

<svelte:head>
    <title>My Svelte Test</title>
</svelte:head>

<h1>Welcome to SvelteKit</h1>
<p class="bg-red-200">
    Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation
</p>
<a href="/about">My about page</a>
<input
    class="w-full rounded-md text-lg p-4 border-2 border-gray-200"
    bind:value={searchTerm}
    placeholder="Search Pokemon"
/>

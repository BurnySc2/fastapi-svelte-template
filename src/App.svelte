<script lang="ts">
    import TodoPage from "./components/TodoPage.svelte"

    let name = "world"
</script>

<main>
    <h1 class="text-center my-2">Hello {name}!</h1>
    <p class="text-center my-2">
        Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte
        apps.
    </p>
    <TodoPage defaultText="My other text" />
</main>

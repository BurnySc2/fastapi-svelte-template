<script lang="ts">
    import TodoPage from "./components/TodoPage.svelte"

    let name: string = "world"
</script>

<main>
    <h1>Hello {name}!</h1>
    <p>
        Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte
        apps.
    </p>
    <TodoPage defaultText="My other text" />
</main>

<style lang="scss">
    main {
        text-align: center;
        padding: 1em;
        max-width: 240px;
        margin: 0 auto;

        h1 {
            color: #ff3e00;
            text-transform: uppercase;
            font-size: 4em;
            font-weight: 100;
        }

        @media (min-width: 640px) {
            max-width: none;
        }
    }
</style>

<script lang="ts">
    import TodoPage from "./components/TodoPage.svelte"
    import Home from "./components/Home.svelte"
    import About from "./components/About.svelte"

    let url = "/"

    const setUrl = (newUrl: string) => {
        url = newUrl
    }
</script>

<main>
    <div class="my-2 flex flex-container justify-center">
        <button class="mx-2 p-1 border-2" on:click={() => setUrl("/")}>Home</button>
        <button class="mx-2 p-1 border-2" on:click={() => setUrl("/about")}>About</button>
        <button class="mx-2 p-1 border-2" on:click={() => setUrl("/todo")}>Todo</button>
    </div>
    {#if url === "/"}
        <Home />
    {:else if url === "/about"}
        <About />
    {:else if url === "/todo"}
        <TodoPage defaultText="My other text" />
    {/if}
</main>

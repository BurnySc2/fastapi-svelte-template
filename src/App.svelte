<script lang="ts">
    import TodoPage from "./components/TodoPage.svelte"
    import Home from "./components/Home.svelte"
    import About from "./components/About.svelte"
    import NormalChat from "./components/NormalChat.svelte"

    let url = "/"
    url = "/chat"

    const setUrl = (newUrl: string) => {
        url = newUrl
    }
</script>

<main>
    <div class="my-2 flex flex-container justify-center">
        <button class="mx-2 p-1 border-2" id="home" on:click={() => setUrl("/")}>Home</button>
        <button class="mx-2 p-1 border-2" id="about" on:click={() => setUrl("/about")}>About</button
        >
        <button class="mx-2 p-1 border-2" id="chat" on:click={() => setUrl("/chat")}>Chat</button>
        <button class="mx-2 p-1 border-2" id="todo" on:click={() => setUrl("/todo")}>Todo</button>
    </div>
    {#if url === "/"}
        <Home />
    {:else if url === "/about"}
        <About defaultText="My other text" />
    {:else if url === "/chat"}
        <NormalChat />
    {:else if url === "/todo"}
        <TodoPage />
    {/if}
</main>

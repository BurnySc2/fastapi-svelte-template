<script lang="ts">
    import Card from "./Card.svelte"

    export let defaultText: string = "this text"
    let someText = defaultText
    let newTodoText = ""
    let cards: { text: string }[] = [{ text: "some todo text" }]

    let addTodo = () => {
        cards = [
            ...cards,
            {
                text: newTodoText,
            },
        ]
    }

    let removeTodo = (index: number) => {
        cards = [...cards.slice(undefined, index), ...cards.slice(index + 1)]
    }
</script>

<main class="flex flex-col items-center">
    <button
        on:click={() => {
            someText = someText === defaultText ? "is changing" : defaultText
        }}
    >
        Click me: {someText}
    </button>
    <div class="flex">
        <input
            class="border-2 my-2 mx-1"
            type="text"
            bind:value={newTodoText}
            placeholder="My new todo item"
        />
        <button class="border-2 my-2 mx-1" on:click={addTodo}>Submit</button>
        <button class="border-2 my-2 mx-1">SubmitBody</button>
        <button class="border-2 my-2 mx-1">SubmitModel</button>
    </div>
    {#each cards as { text }, i}
        <Card cardText={text} index={i} {removeTodo} />
    {/each}
    <!-- Same as above -->
    <!-- {#each cards as card, i}
        <Card cardText={card.text} index={i} />
    {/each} -->
</main>

<style lang="scss">
</style>

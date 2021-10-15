<script lang="ts">
	import TodoPage from '../pages/TodoPage.svelte';
	import Home from '../pages/Home.svelte';
	import About from '../pages/About.svelte';
	import NormalChat from '../pages/NormalChat.svelte';

	let url = '/';

	const setUrl = (newUrl: string) => {
		url = newUrl;
	};
</script>

<main>
	<div class="my2 flex justify-center">
		<button class="m1 p1 rounded" id="home" on:click={() => setUrl('/')}>Home</button>
		<button class="m1 p1 rounded" id="about" on:click={() => setUrl('/about')}>About</button>
		<button class="m1 p1 rounded" id="chat" on:click={() => setUrl('/chat')}>Chat</button>
		<button class="m1 p1 rounded" id="todo" on:click={() => setUrl('/todo')}>Todo</button>
	</div>
	{#if url === '/'}
		<Home />
	{:else if url === '/about'}
		<About defaultText="My other text" />
	{:else if url === '/chat'}
		<NormalChat />
	{:else if url === '/todo'}
		<TodoPage />
	{/if}
</main>

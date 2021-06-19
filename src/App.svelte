<script>
	import Something from "./Something.svelte"
	import Intro from "./Intro.svelte"
</script>

<main>
	<Intro name={"test"} />
	<Something />
</main>

<style global lang="postcss">
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
</style>

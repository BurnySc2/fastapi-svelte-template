<script lang="ts">
    import { Router, Link, Route } from "svelte-routing"

    import TodoPage from "./components/TodoPage.svelte"
    import Home from "./components/Home.svelte"
    import About from "./components/About.svelte"

    export let url = ""
</script>

<main>
    <Router {url}>
        <nav class="text-center">
            <Link to="/">Home</Link>
            <Link to="about">About</Link>
            <Link to="todo">Todo</Link>
        </nav>
        <div>
            <Route path="/"><Home /></Route>
            <Route path="about" component={About} />
            <Route path="todo">
                <TodoPage defaultText="My other text" />
            </Route>
        </div>
    </Router>
</main>

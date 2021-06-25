<script>
  // @ts-ignore
import { Router, Link, Route } from "svelte-routing";
</script>

<Router>
    <nav class="flex justify-center w-full">
        <a class="mx-4 text-lg" href="/">Home</a>
        <Link class="mx-4 text-lg" to="about">About</Link>
        <Route class="mx-4 text-lg" path="todo">Todo</Route>
        <a class="mx-4 text-lg" href="todo">Todo</a>
    </nav>
</Router>
<script>
  import svelteLogo from './assets/svelte.svg';
  import Counter from './lib/Counter.svelte';
  import Numeros from './lib/numeros.svelte';
  import Binding from './lib/Binding.svelte';
  
  const cursos = ['html', 'css', 'js']

</script>
<main class='container'>

<div class="card">
  <Binding/>
</div>
<!-- Lista de cursos-->
  <div class="card"> 
<h3> Cursos</h3>
<ul>
  {#each cursos as item, index}
     <li> {index + 1} - {item} </li>
  {/each}
</ul>
  </div>
  
  <div class="card">
    <h3> Number list</h3>
  <Numeros/>
  </div>

  <div class="card">
    <Counter />
  </div>

  
</main>

<style>
 
</style>

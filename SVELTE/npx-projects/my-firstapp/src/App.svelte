<script>
  import svelteLogo from './assets/svelte.svg'
  import Counter from './lib/Counter.svelte'
  import Numeros from './lib/Numeros.svelte'
  
  const cursos = ['html', 'css', 'js']

</script>
<main class='container'>
<!-- Lista de cursos-->
  <div> 
<h1> Cursos</h1>
<ul>
  {#each cursos as item, index}
     <li> {index + 1} - {item} </li>
  {/each}
</ul>
  </div>
  <Numeros/>
  <div class="card">
    <Counter />
  </div>

  
</main>

<style>
 
</style>

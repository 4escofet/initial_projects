<script>

import Aumentar from './lib/Aumentar.svelte';
import Contador from './lib/Contador.svelte';
import Reset from './lib/Reset.svelte';
import Restar from './lib/Restar.svelte';
import {contador, maximo} from './stores.js'

</script>

<main>
  <!-- H1 toma variable contador inicializada desde Store.Js-->
  <h4> Contador de Store: {$maximo}</h4>
<!-- H1 toma variable contador inicializada desde Store.Js-->
  <h1> Contador de Store: {$contador}</h1>
<!-- Incluye Contador como Componente (que toma la variable contador desde Store.Js)-->
  <Contador/>
<!-- Botón para incrementar contador, lo importa desde Store y lo aumenta al presional -->
  <Aumentar/> <Restar/> <Reset/>


</main>

<style>
  
</style>

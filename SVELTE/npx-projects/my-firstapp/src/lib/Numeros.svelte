 <!-- Lista de numeros-->
 <script>

 // number list

  let numeros = [ 1,5,4] // inicial list
  const agregarNumero = () => {
    let num = Math.floor(Math.random()*(100 - 1)) + 1;
    console.log(num);
    numeros = [...numeros,num];
  };
 </script>
 
 <div>
    <ul>
      {#each numeros as item}
         <li> {item} </li>
      {/each}
    
      {#if numeros.length>5}
         <h3> Se agregaron 5 números</h3>
      {:else}
      <button on:click={agregarNumero} class= "btn btn-primary"> Agregar número </button>
      {/if}
    </ul> 
</div>
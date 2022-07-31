<script>
  let count = 0
  let textcolor = 'text-primary';

  const increment = () => {
    count += 1
  }
  const subtract = () => {
    count = count - 1
  }
  $: if(count >5) {
      textcolor= 'text-danger';
      }
      else {
        textcolor = 'text-primary';
      }

  $:double= count *2;
  $:square= count * count;
  $:message= count>5 ? 'Its greater than five' : 'its lower than five';
</script>

<h1 class={textcolor}> {count} </h1>
<h2 class={textcolor}> {message} </h2> 

<button on:click={increment}>
  Add 
</button>

<button on:click={subtract}>
  subtract
</button>

<h3> Double: {double} </h3>
<h3> square: {square} </h3>

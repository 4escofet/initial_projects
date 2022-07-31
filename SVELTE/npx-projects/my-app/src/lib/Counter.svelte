<script>
  let resta = 0
  let count = 0

  const decrement = () => {
    resta --
  }
  const increment = () => {
    count ++
  }
</script>

<button on:click={decrement}>
  subtracter is on:  {resta}
</button>

<button on:click={increment}>
  counter is on:  {count}
</button>

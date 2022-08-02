<script>
    let texto = ''
    let numero = 0
    let rango = 0
    let check = false

    let fruits = ['tomato', 'avocado', 'strawberry']
    let radio = ''
</script>

<div>
    {#each fruits as item}
        <input type='radio' value={item} bind:group={radio}>
        {item}
    {/each}
    <p>Fruit: {radio} </p>
<br><br>


    <h3> Binding</h3>
    <input type='text' bind:value={texto}>
    <p>Texto: {texto} </p>

    <input type='number' bind:value={numero}>
    <p>Number: {numero} </p>

    <input type='range' bind:value={rango} min='0' max='10'>
    <p>Range: {rango} </p>

    <input type='checkbox' bind:checked={check}>
    <!--<p>Checkbox: {check} </p>-->
    Accept company policies
    <button disabled={!check}> Enviar </button>

</div>
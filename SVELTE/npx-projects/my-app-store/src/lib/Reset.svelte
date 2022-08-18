<script>
    import { contador } from '../stores.js';

    const resetear = () => {
        contador.reiniciar()
    }

</script>

<button on:click={resetear}>Reset</button>
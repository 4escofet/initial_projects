<script>
    import { contador } from '../stores.js';

    const aumentar = () => {
        contador.sumar()
    }

</script>

<button on:click={aumentar}>Aumentar</button>
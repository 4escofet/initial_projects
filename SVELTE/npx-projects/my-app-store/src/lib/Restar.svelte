<script>
    import { contador } from '../stores.js';

    const restar = () => {
        contador.restar()
    }

</script>

<button on:click={restar}>Restar</button>
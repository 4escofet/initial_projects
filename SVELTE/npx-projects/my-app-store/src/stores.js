import { writable } from 'svelte/store'
import { derived } from 'svelte/store'

const createCount = () => {
    const { subscribe, set, update } = writable(0)
    
    return {
        subscribe,
        sumar: () => {
            update(n => n + 1)
        },
        restar: () => {
            update(n => n - 1)
        },
        reiniciar: () => {
            set(0)
        }
    }
    
}

export const contador = createCount()


export const maximo = derived(
    contador,
    $contador => {
        if ($contador === 5) {
            return 'Llegaste al máximo'
        } else if ($contador > 5) {
            contador.reiniciar()
        } else {
            return 'Aun falta...'
        }
    }
)
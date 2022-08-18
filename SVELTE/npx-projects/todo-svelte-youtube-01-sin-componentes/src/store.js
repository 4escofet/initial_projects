import {writable} from 'svelte.store'

const CreateTodos = () => 
        {
    const {suscribe, set, update} = writable([])

    return  {
        suscribe, 
            local: (todos) => {
                set(todos)
                                },
                
        add: (todos) => {
            update(todos => todos = [...todos,todo])
        },
        delete: (id) => {
            update(todos => todos = todos.filter((item)=> item.id !== id))
        },
        put: (id) => {
            update(todos => todos.map((item) => {
                if (item.id === id) {
                  return {
                    ...item,
                    estado: !item.estado,
                  };
                } else {
                  return item;
                }
                }))
        }
    }  
} 

export const todos = CreateTodos()

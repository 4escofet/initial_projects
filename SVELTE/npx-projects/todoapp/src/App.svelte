<script>
import { Toast } from "bootstrap";

let toastEl;
let opc = { text: "", color: "" };

function mostrarMensaje(text, color) {
  opc = {
    text: text,
    color: color,
  };
  return new Toast(toastEl).show();
}

let todos = [];
let todo = { id: 0, texto: "", estado: false };

if (localStorage.getItem("todos")) {
  todos = JSON.parse(localStorage.getItem("todos"));
}

$: localStorage.setItem("todos", JSON.stringify(todos));

 const addTodo = () => {
    if (!todo.texto.trim()) {
      console.log("texto vacio");
      todo.texto = "";
      return;
    }
    todo.id = Date.now();
    todos = [...todos, todo];
    todo = { id: 0, texto: "", estado: false };
    console.log(todos);
  };

$: classEstado = (valor) =>
  valor ? "btn btn-sm btn-success" : "btn btn-sm btn-warning";

$: classIcono = (valor) => (valor ? "bi bi-arrow-clockwise" : "bi bi-check2");

const delTodos = (id) => {
  todos = todos.filter((item) => item.id !== id);
  mostrarMensaje("Todo eliminado", "danger");
};

const updateTodos = (id) => {
  todos = todos.map((item) =>
    item.id === id ? { ...item, estado: !item.estado } : item
  );
};
</script>

<div class="container"> 

  <h1 >CRUD</h1>

  <form on:submit|preventDefault={addTodo}>
    <input  
      type="text"
      placeholder="Enter a task" 
      class= "form-control"
      bind:value={todo.texto}

      >
  </form>

  {#each todos as item}
	<div class="shadow my-3 p-3 lead">
		<p class={item.estado ? "text-decoration-line-through" : ""}>
			{item.texto}
		</p>
		
    <button class={classEstado(item.estado)} on:click={() => updateTodos(item.id)}>
			<i class={classIcono(item.estado)} />
		</button>
		
    <button class="btn btn-sm btn-danger" on:click={() => delTodos(item.id)}>
			<i class="bi bi-trash" />
		</button>
	</div>
  {/each}

<div class="toast-container position-absolute top-0 end-0 p-3">
  <div
    bind:this="{toastEl}"
    class="toast align-items-center text-white bg-{opc.color}"
    role="alert"
    aria-live="assertive"
    aria-atomic="true">

    <div class="d-flex">
      <div class="toast-body">{opc.text}</div>
        <button
          type="button"
          class="btn-close me-2 m-auto"
          data-bs-dismiss="toast"
          aria-label="Close">
        </button>
      </div>

    </div>

  </div>


</div>

<style>
 
</style>

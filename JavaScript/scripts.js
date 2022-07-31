let counter = 0;

document.addEventListener('DOMContentLoaded', function() // () =>
{
    document.querySelector('form').onsubmit = function() 
    {
        const name = document.querySelector('#name').value;
        alert(`Hello, ${name}`);       
    };
    /* Check if there is already a vlaue in local storage
    if (!localStorage.getItem('counter')) {

        // If not, set the counter to 0 in local storage
        localStorage.setItem('counter', 0);
    }
    else {
        let counter = localStorage.getItem('counter');
    } */
    counter = localStorage.getItem('counter');
    document.querySelector('h2').innerHTML = 'Counter pressed' +' '+ counter + ' '+'times';
    document.querySelector('button').onclick = count;
});

    // .setInterval(count, 1000);


/*document.querySelectorAll('button').forEach(function(button) { // (button =>
    button.onclick = function() {
        document.querySelector("#swaap").style.color = button.dataset.color;
    }
});*/

/* Hello function*/
function hello() {
    const heading = document.querySelector('h2');
    console.error(heading)
    if (heading.innerHTML === 'Hello!') {
        heading.innerHTML = 'Goodbye';
    }
    else {
        heading.innerHTML = 'Hello!1';
        }
    }

/* Counter function*/
// Check if there is already a vlaue in local storage
if (!localStorage.getItem('counter')) {

    // If not, set the counter to 0 in local storage
    localStorage.setItem('counter', 0);
}
            
function count() {
    // Retrieve counter value from local storage
    let counter = localStorage.getItem('counter');

    // update counter
    counter++;
    document.querySelector('h2').innerHTML = 'Counter pressed' +' '+ counter + ' '+'times';

    // Store counter in local storage
    localStorage.setItem('counter', counter);
}




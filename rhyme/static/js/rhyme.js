// spinner

var submit = document.getElementById("input_button_rhyme")
var spinner = document.getElementById('spinner')
console.log('submit', submit)
console.log('spinner', spinner)
submit.addEventListener('click', function() {
        spinner.style.display = 'block';
        submit.style.display = 'none'
    }
)

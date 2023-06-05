// arrows

var arrow = document.querySelectorAll(".bi-arrow-down")[0];
arrow.addEventListener('click', function() {
    window.scrollTo({
        top: document.documentElement.scrollHeight,
        behavior: "smooth"
    });
});

var arrow = document.querySelectorAll(".bi-arrow-down-up")[0];
arrow.addEventListener('click', function() {
    window.scrollTo({
        top: document.documentElement.scrollHeight/2,
        behavior: "smooth"
    });
});

var arrow = document.querySelectorAll(".bi-arrow-up")[0];
arrow.addEventListener('click', function() {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
});

// {#    open a word's card#}
var buttons = document.querySelectorAll('.bi-list')
buttons.forEach(function(button) {
    button.addEventListener('click', function() {
        var parent = this.parentNode;
        var card = parent.querySelector('.card_parent');
        if (card.style.display === 'none') {
            card.style.display = 'block';
        }
        else {
            card.style.display = 'none';}
    })
})


// select score
var button = document.getElementById('select_button')

var selectScore = document.getElementById('select_score');
var allScores = document.querySelectorAll('.score');

var marker_score_class = 'selected_by_score'
var marker_assonance_class = 'selected_by_assonance'
function setScores() {
    allScores.forEach(function (score) {
        let parent = score.parentNode;
        parent = parent.parentNode;
        parent.classList.add(marker_score_class)
    })
}

// select assonance
var selectAssonance = document.getElementById('select_assonance');
var allAssonances = document.querySelectorAll('.assonance');
function setAssonances() {
    allAssonances.forEach(function(assonance) {
        let parent = assonance.parentNode;
        parent = parent.parentNode;
        parent.classList.add(marker_assonance_class)
    })
}

button.addEventListener('click', function() { // process score
    setScores()
    setAssonances()

// process score
    let  selected_value_score = selectScore.value;
    allScores.forEach(function(score) {
        let current_value = score.classList;
        current_value = current_value.item(1)
        let parent = score.parentNode;
        parent = parent.parentNode;

        if (parent.classList.contains(marker_assonance_class) === true) {
            if (selected_value_score === 'all') {
                parent.style.display = 'block';
            } else if (current_value !== selected_value_score) {
                parent.style.display = 'none';
                parent.classList.remove(marker_score_class)
            } else {
                parent.style.display = 'block';
            }
        }
    })
// process assonance
    let  selected_value_assonance = selectAssonance.value;
    allAssonances.forEach(function(assonance) {
        let current_value = assonance.classList;
        current_value = current_value.item(1)
        let parent = assonance.parentNode;
        parent = parent.parentNode;

        if (parent.classList.contains(marker_score_class) === true) {
            if (selected_value_assonance === 'all') {
                parent.style.display = 'block';
            } else if (current_value !== selected_value_assonance) {
                parent.style.display = 'none';
                parent.classList.remove(marker_assonance_class)
            } else {
                parent.style.display = 'block';
            }
        }
    })
})


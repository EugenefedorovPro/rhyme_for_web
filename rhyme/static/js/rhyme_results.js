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

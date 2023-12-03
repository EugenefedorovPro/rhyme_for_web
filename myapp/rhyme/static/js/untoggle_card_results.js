// {#    open a word's card#}
let buttons = document.querySelectorAll('.bi-list')
buttons.forEach(function(button) {
    button.addEventListener('click', function() {
        let parent = this.parentNode;
        let card = parent.querySelector('.card_parent');
        if (card.style.display === 'none') {
            card.style.display = 'block';
        }
        else {
            card.style.display = 'none';}
    })
})

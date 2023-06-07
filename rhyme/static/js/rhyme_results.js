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

// -------------
class Select {
    constructor() {
        this.marker_of_being_selected = 'being_selected';
        this.select_button = document.getElementById('select_button');
        this.selectScore = document.getElementById('select_score');
        this.allScores = document.querySelectorAll('.score');
        this.score_select_options = this.selectScore.querySelectorAll('option')
        this.selectAssonance = document.getElementById('select_assonance');
        this.assonance_select_options = this.selectAssonance.querySelectorAll('option')
        this.allAssonances = document.querySelectorAll('.assonance');
        this.allCardParents = document.querySelectorAll('.card_parent');
        this.reset_button = document.getElementById('reset_button');
        this.rhymes = document.querySelectorAll('.rhyme')
    }

    set_option_default(selectSelector, default_value) {
       for (let i=0; i < selectSelector.options.length; i++) {
          let option = selectSelector.options[i];
          if (option.text === default_value) {
              option.selected = true;
              break;
          }
       }
    }
    reset() {
        this.reset_button.addEventListener('click', () => {

            this.setScores();
            this.setAssonances();

            this.rhymes.forEach((rhyme) => {
                rhyme.style.display = 'block';
            })

            this.score_select_options.forEach((option) => {
                option.removeAttribute('disabled', 'false');
                option.removeAttribute('hidden', 'false');
            })

            this.assonance_select_options.forEach((option) => {
                option.removeAttribute('disabled', 'false');
                option.removeAttribute('hidden', 'false');
            })

            this.set_option_default(this.selectScore, 'Штраф')
            this.set_option_default(this.selectAssonance, 'Созвучие')

        } )
    }

    getValuesAssonanceSelectFrom(block_remove) {
        let values_assonance_select_from = new Set();
        let elms_assonance_select_from = block_remove.querySelectorAll('option');
        elms_assonance_select_from.forEach((elm) => {
            values_assonance_select_from.add(elm.value)
        })
        return values_assonance_select_from
    }

    getDiffElmSets(set_1, set_2) {
        let dif_elms = []
        set_1.forEach((elm) => {
            if (!set_2.has(elm)) {
                dif_elms.push(elm)
            }
        })
        return dif_elms
    }

    change(selectChoose, selectRemove, select_remove_options, class_choose, class_remove) {
        selectChoose.addEventListener('change', () => {
            select_remove_options.forEach((option) => {
                option.removeAttribute('disabled', 'false');
                option.removeAttribute('hidden', 'false');
            })
            let selected_score_value = selectChoose.value;
            let assonance_values_to_retain = new Set();

            this.allCardParents.forEach((card_parent) => {
                let current_score_elm = card_parent.querySelector(class_choose);
                let current_score_value = current_score_elm.classList.item(1);
                let current_assonance_elm = card_parent.querySelector(class_remove);
                let current_assonance_value = current_assonance_elm.classList.item(1);

                if (selected_score_value === 'all') {
                    assonance_values_to_retain.add(current_assonance_value);
                    assonance_values_to_retain.add('all');
                }
                else if (selected_score_value === current_score_value) {
                    assonance_values_to_retain.add(current_assonance_value);
                }
            })
            let values_assonance_select_from = this.getValuesAssonanceSelectFrom(selectRemove);
            let values_remove_from_assonance = this.getDiffElmSets(values_assonance_select_from, assonance_values_to_retain);

            select_remove_options.forEach((option) => {
                if (values_remove_from_assonance.includes(option.value) === true) {
                    option.setAttribute('disabled', 'true');
                    option.setAttribute('hidden', 'true');
                }
            })
        })
    }

    setAssonances() {
        this.allAssonances.forEach((assonance) => {
            let parent = assonance.parentNode;
            parent = parent.parentNode;
            parent.classList.add(this.marker_of_being_selected)
        })
    }
    setScores() {
        this.allScores.forEach((score) => {
            let parent = score.parentNode;
            parent = parent.parentNode;
            parent.classList.add(this.marker_of_being_selected)
        })
    }

    assign_selections(selector, all_children_selector, marker_class) {
        let  selected_value_score = selector.value;
        all_children_selector.forEach(function(child) {
            let current_value = child.classList;
            current_value = current_value.item(1)
            let parent = child.parentNode;
            parent = parent.parentNode;
            if (parent.classList.contains(marker_class) === true) {
                if (selected_value_score === 'all') {
                    parent.style.display = 'block';
                } else if (current_value !== selected_value_score) {
                    parent.style.display = 'none';
                    parent.classList.remove(marker_class)
                } else {
                    parent.style.display = 'block';
                }
            }
        })
    }


    select() {
        // if a value in one select is selected, irrelevant values from another select disappear
        this.change(
            this.selectScore,
            this.selectAssonance,
            this.assonance_select_options,
            '.score',
            '.assonance',
        )

        this.change(
            this.selectAssonance,
            this.selectScore,
            this.score_select_options,
            '.assonance',
            '.score',
        )

        this.reset()

        // execute selection
        this.select_button.addEventListener('click', () => { // process score
            // add marker 'being_selected'
            this.setScores();
            this.setAssonances();

            this.assign_selections(
                this.selectScore,
                this.allScores,
                this.marker_of_being_selected,
            )

            this.assign_selections(
                this.selectAssonance,
                this.allAssonances,
                this.marker_of_being_selected,
            )

        })
    }
}


// change(selectChoose, selectRemove, select_remove_options, class_choose, class_remove) {

const select = new Select()
select.select()

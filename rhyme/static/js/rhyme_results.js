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


// select
let number = 4;
console.log(data_assonances_by_score[number])
console.log(data_scores_by_assonance)

class Select {
    constructor(data_assonances_by_score, data_scores_by_assonance, all_score_values, all_assonance_values) {
        this.data_assonances_by_score = data_assonances_by_score;
        this.data_scores_by_assonance = data_scores_by_assonance;
        this.selectScore = document.getElementById('select_score');
        this.selectScoreVariants = this.selectScore.querySelectorAll('option');
        this.allScoreValues = all_score_values;
        this.selectAssonance = document.getElementById('select_assonance');
        this.selectAssonanceVariants = this.selectAssonance.querySelectorAll('option');
        this.allAssonanceValues = all_assonance_values;
        this.rhymes = document.querySelectorAll('.rhyme');

    }

    select_score() {

        this.selectScore.addEventListener('change', () => {
            let selected_assonance_value = this.selectAssonance.value

            // reset rhymes
            // this.rhymes.forEach((rhyme) => {
            //     let rhyme_assonance_value = rhyme.getAttribute('data-assonance')
            //     if (selected_assonance_value === 'all') {
            //         rhyme.style.display = 'block';
            //     }
            //     else if (rhyme_assonance_value !== selected_assonance_value) {
            //         rhyme.style.display = 'block';
            //     }
            // })

            // reset assonance select options
            // this.selectAssonanceVariants.forEach((variant) => {
            //     variant.style.display = 'block';
            // })

            // get selected score value
            let selected_score_value = this.selectScore.value;


            // hide unselected score select options
            this.selectScoreVariants.forEach((variant) => {
                let score_variant_value = variant.value
                if (selected_score_value === 'all') {
                    variant.style.display = 'block'
                    this.rhymes.forEach((rhyme) => {
                        rhyme.style.display = 'block';
                    })
                    this.selectAssonanceVariants.forEach((variant) => {
                        variant.style.display = 'block';
                    })
                    this.selectAssonance.value = 'all';
                }
                else if (score_variant_value !== selected_score_value && score_variant_value !== 'all') {
                    variant.style.display = 'none'
                }
            })

            // hide all rhymes, but selected by score selector
            this.rhymes.forEach((rhyme) => {
                let rhyme_score_value = rhyme.getAttribute('data-score');
                let rhyme_assonance_value = rhyme.getAttribute('assonance-score');
                if (selected_score_value === 'all' && selected_assonance_value !== rhyme_assonance_value) {
                    rhyme.style.display = 'block';
                }
                else if (rhyme_score_value !== selected_score_value && rhyme_score_value !== selected_score_value) {
                    rhyme.style.display = 'none';
                }
            })

            // hide select assonance values with no rhyme
            let assonance_values_to_hide = this.data_assonances_by_score[parseInt(selected_score_value)]
            this.selectAssonanceVariants.forEach((variant) => {
                let variant_value = parseInt(variant.value);
                if (selected_score_value === 'all') {
                    variant.style.display = 'block';
                }
                else if (assonance_values_to_hide.includes(variant_value) === true) {
                    variant.style.display = 'none';
                }
            })

        })
    }


    select_assonance() {

        this.selectAssonance.addEventListener('change', () => {
            // get selected_score_value
            let selected_score_value = this.selectScore.value

            // reset all assonances, but those hidden by score select
            // this.rhymes.forEach((rhyme) => {
            //     let rhyme_score_value = rhyme.getAttribute('data-score');
            //     if (selected_score_value === 'all') {
            //         rhyme.style.display = 'block';
            //     }
            //     else if (rhyme_score_value !== selected_score_value) {
            //         rhyme.style.display = 'block';
            //     }
            // })

            let selected_assonance_value = this.selectAssonance.value;

            // hide unselected assonance select options
            this.selectAssonanceVariants.forEach((variant) => {
                let assonance_variant_value = variant.value
                if (selected_assonance_value === 'all') {
                    variant.style.display = 'block';
                    this.rhymes.forEach((rhyme) => {
                        rhyme.style.display = 'block';
                    })
                    this.selectScoreVariants.forEach((variant) => {
                        variant.style.display = 'block';
                    })
                    this.selectScore.value = 'all';
                }
                else if (assonance_variant_value !== selected_assonance_value && assonance_variant_value !== 'all') {
                    variant.style.display = 'none'
                }
            })

            // hide all rhymes, which do not comply with assonance select
            this.rhymes.forEach((rhyme) => {
                let rhyme_assonance_value = rhyme.getAttribute('data-assonance');
                let rhyme_score_value = rhyme.getAttribute('data-assonance');
                if (selected_assonance_value === 'all' && rhyme_score_value !== selected_score_value) {
                        rhyme.style.display = 'block';
                } else if (selected_assonance_value !== rhyme_assonance_value && rhyme_score_value !== selected_score_value) {
                    rhyme.style.display = 'none';
                }
            })

            // hide all score options/variants from select group
            let score_values_to_hide = this.data_scores_by_assonance[parseInt(selected_assonance_value)];
            this.selectScoreVariants.forEach((variant) => {
                let variant_value = parseInt(variant.value);
                if (selected_assonance_value === 'all') {
                    variant.style.display = 'block';
                } else if (score_values_to_hide.includes(variant_value)) {
                    variant.style.display = 'none';
                }
            })

        })
    }
}

let select = new Select(
    data_assonances_by_score,
    data_scores_by_assonance,
    all_score_values,
    all_assonance_values
)
select.select_score()
select.select_assonance()
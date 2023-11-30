// spinner


function progress() {
    console.log('progress() called')
    let submit = document.getElementById("button_find_rhyme_on_rhyme")
    let bar = document.getElementById('progressbar_rhyme')
    let submit_parent = submit.parentNode;
    let counter = 0;
    if (submit) {
        submit.addEventListener('click', function() {
            submit_parent.replaceChild(bar, submit)
            bar.style.display = 'block';
            submit.style.display = 'none'
            let interval = setInterval( function() {
                counter++;
                console.log(counter);
                bar.style.width = counter + 'px';
                if (counter > 230) {
                    clearInterval(interval)
                }
            }, 23)
            }
        )
    }

}

progress()

const filter = function () {
	var scoreAll = document.getElementById("scoreall");
	scoreAll.checked = true;

	var assonanceAll = document.getElementById("assonanceall");
	assonanceAll.checked = true;

	var allCards = document.getElementsByClassName("rhyme");
	allCards = Array.from(allCards);

	var scoreCheckBoxes = document.getElementsByClassName("score_check_box");
	scoreCheckBoxes = Array.from(scoreCheckBoxes);

	var assonanceCheckBoxes = document.getElementsByClassName(
		"assonance_check_box"
	);
	assonanceCheckBoxes = Array.from(assonanceCheckBoxes);

	// Array to store clicked values
	const clickedValuesScore = [];
	const clickedValuesAssonance = [];

	scoreCheckBoxes.forEach((checkbox) => {
		checkbox.addEventListener("click", handleClick);
	});

	assonanceCheckBoxes.forEach((checkbox) => {
		checkbox.addEventListener("click", handleClick);
	});

	function handleClick(event) {
		// management of checkbox value = all
		var eventElement = event.target;
		var classesEventElement = eventElement.classList;
		var eventValue = eventElement.value;
		classesEventElement = Array.from(classesEventElement);

		if (
			classesEventElement.includes("score_check_box") &&
			eventValue !== "all"
		) {
			scoreAll.checked = false;
		} else if (
			classesEventElement.includes("assonance_check_box") &&
			eventValue !== "all"
		) {
			assonanceAll.checked = false;
		} else if (
			classesEventElement.includes("score_check_box") &&
			eventValue === "all"
		) {
			allCards.forEach((element) => {
				element.style.display = "block";
			});
			scoreCheckBoxes.forEach((checkbox) => {
				if (checkbox.value !== "all") {
					checkbox.checked = false;
				}
			});
		} else if (
			classesEventElement.includes("assonance_check_box") &&
			eventValue === "all"
		) {
			allCards.forEach((element) => {
				element.style.display = "block";
			});
			assonanceCheckBoxes.forEach((checkbox) => {
				if (checkbox.value !== "all") {
					checkbox.checked = false;
				}
			});
		}

		// Clear the clickedValuesScore array for each click
		clickedValuesScore.length = 0;
		clickedValuesAssonance.length = 0;

		scoreCheckBoxes.forEach((checkbox) => {
			if (checkbox.checked) {
				clickedValuesScore.push(checkbox.value);
			}
		});

		assonanceCheckBoxes.forEach((checkbox) => {
			if (checkbox.checked) {
				clickedValuesAssonance.push(checkbox.value);
			}
		});

		allCards.forEach((element) => {
			const dataScore = element.getAttribute("data-score");
			const dataAssonance = element.getAttribute("data-assonance");

			if (
				(clickedValuesScore.includes(dataScore) &&
					clickedValuesAssonance.includes(dataAssonance)) ||
				(clickedValuesScore.includes("all") &&
					clickedValuesAssonance.includes(dataAssonance)) ||
				(clickedValuesScore.includes(dataScore) &&
					clickedValuesAssonance.includes("all")) ||
				(clickedValuesScore.includes("all") &&
					clickedValuesAssonance.includes("all"))
			) {
				element.style.display = "block";
			} else {
				element.style.display = "none"; // Change to "none" to hide
			}
		});
	}
};

filter();

// Initialize scores for the dichotomies (I/E, N/S, T/F, J/P)
let score = {
    I: 0,
    E: 0,
    N: 0,
    S: 0,
    F: 0,
    T: 0,
    J: 0,
    P: 0
  };
  
  // Example function to calculate scores based on user choice
  function calculateScore(questionID, userChoice) {
    // Make sure each option corresponds to a balanced score system
    switch (questionID) {
      case 1: // Question 1 - I/E
        if (userChoice === "I") {
          score.I += 1;
        } else if (userChoice === "E") {
          score.E += 1;
        }
        break;
  
      case 2: // Question 2 - N/S
        if (userChoice === "N") {
          score.N += 1;
        } else if (userChoice === "S") {
          score.S += 1;
        }
        break;
  
      case 3: // Question 3 - F/T
        if (userChoice === "F") {
          score.F += 1;
        } else if (userChoice === "T") {
          score.T += 1;
        }
        break;
  
      case 4: // Question 4 - J/P
        if (userChoice === "J") {
          score.J += 1;
        } else if (userChoice === "P") {
          score.P += 1;
        }
        break;
  
      // Add more questions here as needed, following the same pattern
    }
  }
  
  // Function to calculate the final personality type based on scores
  function calculatePersonality() {
    let personalityType = "";
  
    personalityType += (score.I > score.E) ? "I" : "E";
    personalityType += (score.N > score.S) ? "N" : "S";
    personalityType += (score.F > score.T) ? "F" : "T";
    personalityType += (score.J > score.P) ? "J" : "P";
  
    // Display the result
    document.querySelector(".result").textContent = `Your MBTI type is: ${personalityType}`;
  }
  
  // Example of handling a choice selection
  function handleOptionSelection(questionID, choice) {
    // Add the selected option's score to the result
    calculateScore(questionID, choice);
  
    // Update the UI for the selected option
    let options = document.querySelectorAll(`.question-${questionID} .option`);
    options.forEach(option => {
      option.classList.remove('selected'); // Remove previous selection
    });
    
    // Add selected class to the clicked option
    let selectedOption = document.querySelector(`.question-${questionID} .option[data-choice="${choice}"]`);
    selectedOption.classList.add('selected');
  }
  
  // Example of initializing questions (question IDs can be randomized for balance)
  document.addEventListener("DOMContentLoaded", function () {
    const questions = document.querySelectorAll('.question');
    questions.forEach((question, index) => {
      question.addEventListener('click', function (event) {
        // Get the selected choice and pass it along with the question ID
        let selectedChoice = event.target.getAttribute('data-choice');
        if (selectedChoice) {
          handleOptionSelection(index + 1, selectedChoice); // index+1 for question ID
        }
      });
    });
  });
  
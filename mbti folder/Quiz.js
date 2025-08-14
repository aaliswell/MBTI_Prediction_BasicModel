// quiz.js

const typeCounts = { E: 0, I: 0, S: 0, N: 0, T: 0, F: 0, J: 0, P: 0 };
const allQuestions = [
  // include your 20 question objects here
];

const descriptions = {
  ISTJ: "ISTJ: Responsible, serious, and traditional. Loyal and detail-oriented.",
  ISFJ: "ISFJ: Nurturing, responsible, and reserved. Devoted to helping others.",
  INFJ: "INFJ: Idealistic, insightful, and compassionate. Deep thinkers and planners.",
  INTJ: "INTJ: Independent, strategic, and logical. Visionary and analytical.",
  ISTP: "ISTP: Action-oriented and pragmatic. Analytical and independent.",
  ISFP: "ISFP: Gentle, sensitive, and quiet. Artistic and adaptable.",
  INFP: "INFP: Idealistic and loyal. Driven by their values.",
  INTP: "INTP: Theoretical, curious, and analytical. Loves abstract ideas.",
  ESTP: "ESTP: Energetic and perceptive. Lives in the moment.",
  ESFP: "ESFP: Fun-loving and spontaneous. Values excitement and connection.",
  ENFP: "ENFP: Enthusiastic and imaginative. Values inspiration and relationships.",
  ENTP: "ENTP: Inventive and energetic. Enjoys intellectual debates.",
  ESTJ: "ESTJ: Organized, assertive, and realistic. Strong leadership skills.",
  ESFJ: "ESFJ: Caring and sociable. Enjoys helping and supporting others.",
  ENFJ: "ENFJ: Charismatic and altruistic. Inspires and supports others.",
  ENTJ: "ENTJ: Confident and strategic. Strong leadership and execution skills."
};

let selectedQuestions = [];
let currentQuestion = 0;

function shuffleAndPick() {
  selectedQuestions = [...allQuestions].sort(() => Math.random() - 0.5).slice(0, 10);
}

function showQuestion() {
  if (currentQuestion >= selectedQuestions.length) return showResults();
  const q = selectedQuestions[currentQuestion];
  document.getElementById("questionContainer").innerHTML = `<div class="question">${q.question}</div>`;
  const oContainer = document.getElementById("answerOptions");
  oContainer.innerHTML = "";

  q.options.forEach(opt => {
    const btn = document.createElement("button");
    btn.className = "answer-button";
    btn.textContent = opt.text;
    btn.onclick = () => {
      typeCounts[opt.trait]++;
      currentQuestion++;
      showQuestion();
    };
    oContainer.appendChild(btn);
  });
}

function calculateMBTI() {
  return [
    typeCounts.E >= typeCounts.I ? 'E' : 'I',
    typeCounts.S >= typeCounts.N ? 'S' : 'N',
    typeCounts.T >= typeCounts.F ? 'T' : 'F',
    typeCounts.J >= typeCounts.P ? 'J' : 'P'
  ].join('');
}

function getMBTIDescription(type) {
  return descriptions[type] || "Description not available.";
}

function showResults() {
  const type = calculateMBTI();
  document.getElementById("mbtiType").innerHTML = `Your MBTI Type: <strong>${type}</strong>`;
  document.getElementById("mbtiDesc").innerHTML = getMBTIDescription(type);
  document.getElementById("resultBox").style.display = "block";
  
  // Save results to localStorage
  localStorage.setItem("mbtiType", type);
  localStorage.setItem("mbtiDesc", getMBTIDescription(type));
  localStorage.setItem("mbtiCounts", JSON.stringify(typeCounts));
}

function retakeQuiz() {
  currentQuestion = 0;
  for (let t in typeCounts) typeCounts[t] = 0;
  document.getElementById("resultBox").style.display = "none";
  shuffleAndPick();
  showQuestion();
}

function goToResultPage() {
  window.location.href = "result.html";
}

// Attach to Know More button
document.querySelector(".continue-btn[onclick*='16personalities']").onclick = goToResultPage;

shuffleAndPick();
showQuestion();

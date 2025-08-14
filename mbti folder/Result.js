// result.js

const mbtiData = {
    ISTJ: {
      about: "You are dependable and detail-oriented, with a strong sense of duty. Your structured nature helps you follow through on commitments and uphold traditions.",
      traits: ["Responsible", "Organized", "Logical", "Stubborn"],
      famous: ["Angela Merkel", "George Washington"],
      jobs: ["Accountant", "Project Manager"]
    },
    ISFJ: {
      about: "You are a nurturing protector who values harmony and loyalty. You find fulfillment in helping others in practical and meaningful ways.",
      traits: ["Caring", "Meticulous", "Loyal", "Avoids conflict"],
      famous: ["Mother Teresa", "Kate Middleton"],
      jobs: ["Nurse", "Social Worker"]
    },
    INFJ: {
      about: "You are an insightful idealist with a deep sense of purpose. You care deeply for others and often strive to make a lasting positive impact.",
      traits: ["Visionary", "Compassionate", "Insightful", "Overly idealistic"],
      famous: ["Carl Jung", "Nicole Kidman"],
      jobs: ["Writer", "Psychologist"]
    },
    INTJ: {
      about: "You are a strategic thinker and planner, driven by curiosity and innovation. You excel in turning complex ideas into structured solutions.",
      traits: ["Strategic", "Independent", "High standards", "Insensitive"],
      famous: ["Elon Musk", "Mark Zuckerberg"],
      jobs: ["Scientist", "Software Architect"]
    },
    ISTP: {
      about: "You are analytical and hands-on, preferring to explore the world through practical experience. You're adaptable and thrive in the moment.",
      traits: ["Analytical", "Independent", "Adaptable", "Insensitive"],
      famous: ["Clint Eastwood", "Bear Grylls"],
      jobs: ["Engineer", "Mechanic"]
    },
    ISFP: {
      about: "You are a quiet, artistic soul who values self-expression and authentic experiences. You appreciate beauty and live life on your own terms.",
      traits: ["Artistic", "Sensitive", "Easygoing", "Avoids conflict"],
      famous: ["Britney Spears", "Michael Jackson"],
      jobs: ["Designer", "Artist"]
    },
    INFP: {
      about: "You are imaginative and driven by strong values. You care deeply about people and ideas, and often seek deeper meaning in everything.",
      traits: ["Empathetic", "Idealistic", "Reserved", "Can be overly idealistic"],
      famous: ["William Shakespeare", "J.K. Rowling"],
      jobs: ["Writer", "Counselor", "Psychologist"]
    },
    INTP: {
      about: "You are a logical problem-solver who thrives on understanding complex ideas. Independence and intellectual exploration guide you.",
      traits: ["Analytical", "Inventive", "Independent", "Absent-minded"],
      famous: ["Albert Einstein", "Bill Gates"],
      jobs: ["Philosopher", "Developer"]
    },
    ESTP: {
      about: "You are energetic and action-oriented, always ready for adventure. You make decisions quickly and live life in the fast lane.",
      traits: ["Energetic", "Spontaneous", "Sociable", "Impulsive"],
      famous: ["Madonna", "Ernest Hemingway"],
      jobs: ["Sales", "Entrepreneur"]
    },
    ESFP: {
      about: "You are fun-loving and spontaneous, bringing life and energy to any room. You live in the moment and seek excitement in your surroundings.",
      traits: ["Lively", "Sociable", "Curious", "Easily bored"],
      famous: ["Elton John", "Miley Cyrus"],
      jobs: ["Performer", "Event Planner"]
    },
    ENFP: {
      about: "You are a passionate and enthusiastic explorer of possibilities. You enjoy connecting with people and sharing imaginative ideas.",
      traits: ["Optimistic", "Enthusiastic", "Friendly", "Easily distracted"],
      famous: ["Robin Williams", "Ellen DeGeneres"],
      jobs: ["Actor", "Marketer"]
    },
    ENTP: {
      about: "You are intellectually curious and quick-witted, constantly seeking new challenges and perspectives.",
      traits: ["Curious", "Quick-witted", "Energetic", "Argumentative"],
      famous: ["Tom Hanks", "Robert Downey Jr."],
      jobs: ["Consultant", "Strategist"]
    },
    ESTJ: {
      about: "You are a natural leader who values order and efficiency. You prefer structure and tradition when managing people or projects.",
      traits: ["Organized", "Practical", "Decisive", "Inflexible"],
      famous: ["Judge Judy", "Michelle Obama"],
      jobs: ["Manager", "Police Officer"]
    },
    ESFJ: {
      about: "You are sociable and warm, thriving in environments where you can support and uplift others. You value connection and cooperation.",
      traits: ["Loyal", "Supportive", "Social", "Need validation"],
      famous: ["Taylor Swift", "Jennifer Garner"],
      jobs: ["Teacher", "Nurse"]
    },
    ENFJ: {
      about: "You are charismatic and empathetic, often stepping into leadership roles with a vision of creating a better future.",
      traits: ["Charismatic", "Altruistic", "Inspiring", "Overly idealistic"],
      famous: ["Barack Obama", "Oprah Winfrey"],
      jobs: ["Coach", "Public Relations"]
    },
    ENTJ: {
      about: "You are bold and assertive, with a natural drive to organize and lead. You thrive on achieving goals and solving complex problems.",
      traits: ["Ambitious", "Efficient", "Strategic", "Stubborn"],
      famous: ["Steve Jobs", "Gordon Ramsay"],
      jobs: ["Executive", "Lawyer"]
    }
  };
  
  document.addEventListener("DOMContentLoaded", () => {
    const mbtiType = localStorage.getItem("mbtiType");
    const mbtiDesc = localStorage.getItem("mbtiDesc");
    const mbtiCounts = JSON.parse(localStorage.getItem("mbtiCounts") || '{}');
  
    document.getElementById("typeOutput").innerText = mbtiType ? `Your MBTI is ${mbtiType}` : "No result";
    document.getElementById("descOutput").innerText = mbtiDesc || "No description available.";
  
    const traits = [['E', 'I'], ['S', 'N'], ['T', 'F'], ['J', 'P']];
    const values = traits.map(([a, b]) => (mbtiCounts[a] || 0) + (mbtiCounts[b] || 0));
  
    new Chart(document.getElementById("mbtiChart"), {
      type: 'bar',
      data: {
        labels: ['E vs I', 'S vs N', 'T vs F', 'J vs P'],
        datasets: [{
          label: 'Trait Dominance',
          backgroundColor: ['#f0c987', '#e5b68b', '#cf967b', '#ba7f65'],
          data: values
        }]
      },
      options: {
        responsive: true,
        plugins: { legend: { display: false } },
        scales: {
          y: {
            beginAtZero: true,
            ticks: {
              callback: val => Math.abs(val)
            }
          },
          x: {
            grid: { display: false },
            ticks: { font: { size: 14 } }
          }
        }
      }
    });
  
    const closeness = traits.reduce((count, [a, b], i) => {
      const expected = mbtiType?.[i];
      const dominant = (mbtiCounts[a] || 0) >= (mbtiCounts[b] || 0) ? a : b;
      return dominant === expected ? count + 1 : count;
    }, 0);
  
    const percent = Math.round((closeness / 4) * 100);
    const closenessNote = document.createElement("div");
    closenessNote.style.textAlign = "center";
    closenessNote.style.marginTop = "20px";
    closenessNote.style.fontSize = "18px";
    closenessNote.innerText = `Your result is a ${percent}% match with your MBTI traits.`;
    document.querySelector(".chart-box").appendChild(closenessNote);
  
    function calculateSimilarity(type) {
      return traits.reduce((score, [a, b], i) => {
        const expected = type[i];
        const dominant = (mbtiCounts[a] || 0) >= (mbtiCounts[b] || 0) ? a : b;
        return dominant === expected ? score + 1 : score;
      }, 0) / 4;
    }
  
    const similarityList = Object.keys(mbtiData)
      .map(type => ({
        type,
        percent: Math.round(calculateSimilarity(type) * 100)
      }))
      .sort((a, b) => b.percent - a.percent)
      .filter(item => item.type !== mbtiType)
      .slice(0, 3);
  
    const similarBox = document.createElement("div");
  similarBox.style.textAlign = "center";
  similarBox.style.marginTop = "30px";
  similarBox.style.paddingTop = "10px";
  similarBox.style.background = "#f5efe5";
  similarBox.style.color = "#3e2e20";
  similarBox.style.borderRadius = "10px";
  similarBox.style.padding = "16px";
  similarBox.innerHTML = `<h3 style='margin-bottom:10px;'>Other Close MBTI Matches</h3><ul style="list-style:none; padding:0; font-size:16px;">${similarityList
    .map(item => `<li style='margin-bottom:6px;'>${item.type} — <strong>${item.percent}%</strong> match</li>`) 
    .join('')}</ul>`;
  document.querySelector(".chart-box").appendChild(similarBox);
  
    const info = mbtiData[mbtiType] || {
      about: "Information not available for this type yet.",
      traits: [],
      famous: [],
      jobs: []
    };
  
    document.getElementById("aboutBox").innerText = info.about;
    document.getElementById("traitsBox").innerHTML = info.traits.map(t => `<li>${t}</li>`).join('');
    document.getElementById("famousBox").innerHTML = info.famous.map(p => `<li>${p}</li>`).join('');
    document.getElementById("jobBox").innerHTML = info.jobs.map(j => `<li>${j}</li>`).join('');
  });
  
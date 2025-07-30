document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("mentalForm");
  const popup = document.getElementById("resultPopup");
  const resultText = document.getElementById("resultText");
  const closeBtn = document.getElementById("closePopup");

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const formData = new FormData(form);
    const values = Object.fromEntries(formData.entries());

    const phq = parseInt(values.phq9);
    const gad = parseInt(values.gad7);
    const mood = parseInt(values.mood_score);
    const stress = parseInt(values.stress);
    const anxiety = parseInt(values.anxiety);
    const depression = parseInt(values.depression);

    let result = "You are doing well. Maintain healthy habits.";
    
    if (phq >= 3 || gad >= 3 || depression >= 3 || anxiety >= 3 || stress >= 3 || mood <= 3) {
      result = "You may be experiencing high emotional distress. Please consider reaching out to a mental health professional.";
    } else if (phq >= 2 || gad >= 2 || depression >= 2 || anxiety >= 2) {
      result = "Mild symptoms detected. Regular mindfulness and self-care is recommended.";
    }

    resultText.innerText = result;
    popup.style.display = "flex";
  });

  closeBtn.addEventListener("click", function () {
    popup.style.display = "none";
  });
});
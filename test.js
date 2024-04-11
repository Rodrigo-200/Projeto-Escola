alert('Script Loaded');
alert("Script Loaded");
document.addEventListener('DOMContentLoaded', () => {
  // Existing code...
});
setInterval(() => {
  fetchDataAndUpdateUI();
}, 10000); // Adjust the interval as needed

function fetchDataAndUpdateUI() {
  console.log("Fetching data...");
  const jsonUrl = 'https://rodrigo-200.github.io/Projeto-Escola/data.json';

  fetch(jsonUrl)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      console.log("Data received:", data); // This should log the fetched data
      document.getElementById('valor-temperatura-ar').textContent = data.temperatura_ar;
      document.getElementById('valor-humidade-ar').textContent = data.humidade_ar;
      document.getElementById('valor-humidade-solo').textContent = data.humidade_solo;
      document.getElementById('necessidade-rega').textContent = data.necessidade_rega;
      document.getElementById('estado-da-conexão').textContent = data.estado_conexao;
    })
    .catch(error => {
      console.error('Fetch error:', error);
    });
}


    // Show loading dots with a delay
    document.addEventListener('DOMContentLoaded', () => {
      const loadingContainer = document.getElementById('carregar');
      loadingContainer.innerHTML = '<div class="loading-dot"></div><div class="loading-dot"></div><div class="loading-dot"></div>';

      setTimeout(() => {
        loadingContainer.style.display = 'none';
        
        const dataContainer = document.getElementById('data-container');
        dataContainer.style.display = 'block';

        const elementos_a_animar = document.querySelectorAll('.animação-inicial span');
        elementos_a_animar.forEach(element => {
          element.classList.add('animacao', 'fadeIn');
        });
      }, 2000); // Set the delay in milliseconds (2 seconds in this case)
    });

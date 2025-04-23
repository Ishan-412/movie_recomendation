document.getElementById('recommendationForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the default form submit behavior

    const genre = document.getElementById('genre').value;

    fetch('/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ genre: genre })
    })
    .then(response => response.json())
    .then(data => {
        const recommendationsDiv = document.getElementById('movieRecommendations');
        recommendationsDiv.innerHTML = "<h2>Recommended Movies:</h2>";
        
        if (data.length > 0) {
            data.forEach(movie => {
                const p = document.createElement('p');
                p.textContent = "🎥 " + movie;
                recommendationsDiv.appendChild(p);
            });
        } else {
            recommendationsDiv.innerHTML += "<p>No recommendations found for this genre.</p>";
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert("Something went wrong. Please try again later.");
    });
});

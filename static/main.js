document.getElementById('quoteForm').onsubmit = function(e) {
    var scottCode = document.getElementById('scottCode').value;
    var newQuote = document.getElementById('newQuote').value;
    var errorMessageElement = document.getElementById('errorMessage');
    
    // Reset error message
    errorMessageElement.style.display = 'none';
    errorMessageElement.textContent = '';

    if (!scottCode.trim() || !newQuote.trim()) {
        // Prevent form submission if any field is empty
        e.preventDefault();
        errorMessageElement.textContent = 'Both fields are required.';
        errorMessageElement.style.display = 'block';
    }
};
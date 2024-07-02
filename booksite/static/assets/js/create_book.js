document.getElementById('bookForm').addEventListener('submit', function(e) {
    e.preventDefault();

    // Get form values
    const title = document.getElementById('title').value;
    const author = document.getElementById('author').value;
    const coverImage = document.getElementById('coverImage').files[0];
    const description = document.getElementById('description').value;

    // Create FileReader to convert image file to Data URL
    const reader = new FileReader();

    reader.onload = function(e) {
        // Create book element
        const bookList = document.getElementById('bookList');
        const bookDiv = document.createElement('div');
        bookDiv.classList.add('book');

        bookDiv.innerHTML =
            <img src="${e.target.result}" alt="${title}">
            <div>
                <h3>${title}</h3>
                <p><strong>Author:</strong> ${author}</p>
                <p>${description}</p>
            </div>
            <button class="delete-btn">Delete</button>
        ;

        bookList.appendChild(bookDiv);

        // Add delete functionality
        bookDiv.querySelector('.delete-btn').addEventListener('click', function() {
            bookList.removeChild(bookDiv);
        });

        // Clear form
        document.getElementById('bookForm').reset();
    }

    reader.readAsDataURL(coverImage);
});
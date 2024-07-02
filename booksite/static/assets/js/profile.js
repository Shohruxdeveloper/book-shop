document.addEventListener("DOMContentLoaded", function() {
    const body = document.body;

    // Background color animation
    setInterval(changeBackgroundColor, 2000); // Change color every 2 seconds

    // Background image animation
    let backgroundImageIndex = 0;
    const backgroundImages = [
        'url(image1.jpg)',
        'url(image2.jpg)',
        'url(image3.jpg)'
    ];

    setInterval(changeBackgroundImage, 5000); // Change image every 5 seconds

    // Function to change background color
    function changeBackgroundColor() {
        const randomColor = getRandomColor();
        body.style.backgroundColor = randomColor;
    }

    // Function to change background image
    function changeBackgroundImage() {
        body.style.backgroundImage = backgroundImages[backgroundImageIndex];
        backgroundImageIndex = (backgroundImageIndex + 1) % backgroundImages.length;
    }

    // Function to generate random color
    function getRandomColor() {
        const letters = '0123456789ABCDEF';
        let color = '#';
        for (let i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    }
});

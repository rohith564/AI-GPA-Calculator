
document.addEventListener("DOMContentLoaded", function () {
    // 1. Grab all the HTML elements by their exact IDs
    const imageInput = document.getElementById('imageInput');
    const previewContainer = document.getElementById('previewContainer');
    const previewImage = document.getElementById('previewImage');
    const removeImageBtn = document.getElementById('removeImage');

    const form = document.querySelector('form');
    const calculateBtn = document.getElementById('calculateBtn');
    const btnText = document.getElementById('btnText');
    const progressContainer = document.getElementById('progressContainer');
    const progressText = document.getElementById('progressText');

    // ==========================================
    // ACTION 1: Show preview when image is chosen
    // ==========================================
    imageInput.addEventListener('change', function (event) {
        if (event.target.files.length > 0) {
            // 1. Un-hide the preview container
            previewContainer.style.display = 'block';

            // 2. Generate a preview URL and put it in the <img> tag
            const file = event.target.files[0];
            previewImage.src = URL.createObjectURL(file);
        }
    });

    // ==========================================
    // ACTION 2: Make the "X" remove button work
    // ==========================================
    removeImageBtn.addEventListener('click', function () {
        imageInput.value = ""; // Clear the file from the input
        previewContainer.style.display = 'none'; // Hide the preview box again
        previewImage.src = ""; // Clear the image data
    });

    // ==========================================
    // ACTION 3: Show "Processing" when Submit is clicked
    // ==========================================
    form.addEventListener('submit', function () {
        // 1. Change button text to show it is working
        btnText.innerText = 'Processing...';

        // 2. Make the progress container visible
        progressContainer.style.display = 'block';
        progressText.innerText = 'Extracting data from marksheet. Please wait...';
    });
});


document.addEventListener("DOMContentLoaded", function() {
    
    // Grab the pop-up elements
    const modal = document.getElementById("gpaModal");
    const openBtn = document.getElementById("openGpaBtn");
    const closeBtn = document.getElementById("closeModalBtn");

    // SAFETY CHECK: Only attach clicks if the elements exist on the page
    if (modal && openBtn && closeBtn) {
        
        // Open the modal
        openBtn.onclick = function() {
            modal.style.display = "flex";
        }

        // Close the modal with 'X'
        closeBtn.onclick = function() {
            modal.style.display = "none";
        }

        // Close the modal by clicking outside the box
        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }
    }
});
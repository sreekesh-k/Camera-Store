document.addEventListener('DOMContentLoaded', function () {
    const cameraInput = document.getElementById('customer_camera');
    const cameraSuggestions = document.getElementById('cameraSuggestions');

    // Function to fetch cameras data via AJAX
    function fetchCameras() {
        fetch('get_cameras/')  // Adjust the URL as per your Django URL pattern
            .then(response => response.json())
            .then(data => {
                initializeCameraSuggestions(data);
            })
            .catch(error => {
                console.error('Error fetching cameras:', error);
            });
    }

    // Initialize camera suggestions after fetching data
    function initializeCameraSuggestions(cameras) {
        // Store cameras data for future reference
        window.cameraData = cameras;

        // Event listener for input changes
        cameraInput.addEventListener('input', function () {
            const query = cameraInput.value.trim();
            if (query.length > 2) {
                const filteredCameras = filterCameraSuggestions(query);
                displayCameraSuggestions(filteredCameras);
            } else {
                hideCameraSuggestions();
            }
        });
    }

    // Function to filter camera suggestions based on user input
    function filterCameraSuggestions(query) {
        return window.cameraData.filter(camera => {
            const model = `${camera.brand} - ${camera.model_name}`;
            return model.toLowerCase().includes(query.toLowerCase());
        });
    }

    // Function to display camera suggestions
    function displayCameraSuggestions(cameras) {
        cameraSuggestions.innerHTML = '';
        cameras.slice(0, 6).forEach(camera => {
            const listItem = document.createElement('a');
            listItem.className = 'list-group-item list-group-item-action';
            listItem.href = '#';
            listItem.textContent = `${camera.brand} - ${camera.model_name}`;
            listItem.addEventListener('click', function (event) {
                event.preventDefault();
                cameraInput.value = `${camera.brand} - ${camera.model_name}`;
                hideCameraSuggestions();
            });
            cameraSuggestions.appendChild(listItem);
        });
        cameraSuggestions.style.display = 'block';
    }

    // Function to hide camera suggestions
    function hideCameraSuggestions() {
        cameraSuggestions.innerHTML = '';
        cameraSuggestions.style.display = 'none';
    }

    // Hide suggestions when clicking outside of input or suggestions box
    document.addEventListener('click', function (event) {
        if (!cameraInput.contains(event.target) && !cameraSuggestions.contains(event.target)) {
            hideCameraSuggestions();
        }
    });

    // Fetch cameras data when the page loads
    fetchCameras();
});

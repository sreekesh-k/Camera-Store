document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    const suggestionsList = document.getElementById('suggestions');
    
    searchInput.addEventListener('input', function() {
      const query = searchInput.value;
      
      if (query.length > 2) {  // Start showing suggestions after 3 characters
        fetch(`/sales/search-suggestions/?term=${query}`)
          .then(response => response.json())
          .then(data => {
            suggestionsList.innerHTML = '';
            data.forEach(item => {
              const listItem = document.createElement('li');
              listItem.className = 'list-group-item list-group-item-action';
              listItem.textContent = item.label;
              listItem.addEventListener('click', function() {
                searchInput.value = item.model;
                suggestionsList.innerHTML = '';
              });
              suggestionsList.appendChild(listItem);
            });
          });
      } else {
        suggestionsList.innerHTML = '';
      }
    });

    document.addEventListener('click', function(event) {
      if (!searchInput.contains(event.target)) {
        suggestionsList.innerHTML = '';
      }
    });
  });
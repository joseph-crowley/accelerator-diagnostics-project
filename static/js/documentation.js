// documentation.js
document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    const typeFilter = document.getElementById('typeFilter');
    const docsList = document.getElementById('docsList');
    
    const searchDocs = () => {
      const filter = searchInput.value.toUpperCase();
      const typeFilterValue = typeFilter.value;
      const items = docsList.getElementsByTagName('a');
    
      for (let i = 0; i < items.length; i++) {
        const item = items[i];
        const dataTitle = item.getAttribute('data-title').toUpperCase();
        const dataContent = item.getAttribute('data-content').toUpperCase();
        const dataType = item.getAttribute('data-type').toUpperCase();
    
        if ((dataTitle.includes(filter) || dataContent.includes(filter)) &&
            (typeFilterValue === "" || dataType === typeFilterValue)) {
          items[i].style.display = "";
        } else {
          items[i].style.display = "none";
        }
      }
    };
  
    searchInput.addEventListener('keyup', searchDocs);
    typeFilter.addEventListener('change', searchDocs);
  });
  

window.onload = function() {
    // Select all elements that have an ID starting with 'parent-' or 'button-'
    let elements = document.querySelectorAll("[id^='sin-']");
    
    // Apply sine offset to each element's x position
    elements.forEach((element, index) => {
        let offsetX = Math.sin(index * 180 / Math.PI) * 150;  // Adjust the multiplier to control amplitude
        //element.style.backgroundColor = 'red';
        element.style.width = 'auto';
        element.style.position = 'relative';  // Set the element's position to relative
        element.style.margin = '3% 0px';
        element.style.left = offsetX + 'px';  // Apply the sine-based offset to the x (left) position
    });
};

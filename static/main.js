
const toggles = document.querySelectorAll('.faq-toggle');

toggles.forEach(toggle => {
	toggle.addEventListener('click', () => {
		toggle.parentNode.classList.toggle('active');
	});
});




//AIzaSyAeN8gQV1EYpdneoq0h0PyfmpjAL_e1Z_0
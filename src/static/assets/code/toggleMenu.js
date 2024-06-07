// Maneja el evento del click en el boton de menú, para mostrar o ocultar el menu en version mobil.

document.addEventListener('click', (e) => {
  if(e.target.matches('.toggleMenu')){
    document.querySelector('.nav-menu').classList.toggle('active');
  }
  if(e.target.matches('.closeMenu')){
    document.querySelector('.nav-menu').classList.toggle('active');
  }
})
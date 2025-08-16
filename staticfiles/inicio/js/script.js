/**
 * BACHKATOV DETAILING - SCRIPT PRINCIPAL
 * 
 * Funcionalidades:
 * 1. Lazy loading para imágenes
 * 2. Botón flotante de WhatsApp animado
 * 3. Validación básica de formulario
 */

// ==================================
// 1. LAZY LOADING PARA IMÁGENES
// ==================================
function initLazyLoading() {
    // Busca todas las imágenes con clase 'lazy-img'
    const lazyImages = document.querySelectorAll('.lazy-img');
    
    // Si el navegador soporta IntersectionObserver (modernos)
    if ('IntersectionObserver' in window) {
        // Crea un observador para las imágenes
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                // Cuando la imagen entra en la pantalla
                if (entry.isIntersecting) {
                    const img = entry.target;
                    // Carga la imagen real
                    img.src = img.dataset.src;
                    // Añade clase para efectos de transición
                    img.classList.add('loaded');
                    // Deja de observar esta imagen
                    observer.unobserve(img);
                }
            });
        }, {
            rootMargin: '0px 0px 100px 0px' // Carga 100px antes de que sea visible
        });
        
        // Observa cada imagen
        lazyImages.forEach(img => observer.observe(img));
    } 
    // Fallback para navegadores antiguos
    else {
        lazyImages.forEach(img => {
            img.src = img.dataset.src;
            img.classList.add('loaded');
        });
    }
}

// ==================================
// 2. BOTÓN FLOTANTE DE WHATSAPP
// ==================================
function initWhatsAppButton() {
    const whatsappBtn = document.getElementById('whatsappFloat');
    
    if (whatsappBtn) {
        // Efecto de pulso (animación)
        function pulseAnimation() {
            whatsappBtn.style.boxShadow = '0 0 0 0 rgba(37, 211, 102, 0.7)';
            setTimeout(() => {
                whatsappBtn.style.boxShadow = '0 0 0 10px rgba(37, 211, 102, 0)';
            }, 500);
        }
        
        // Inicia la animación cada 2 segundos
        setInterval(pulseAnimation, 2000);
        pulseAnimation(); // Primera ejecución
        
        // Efectos al pasar el mouse
        whatsappBtn.addEventListener('mouseenter', () => {
            whatsappBtn.style.transform = 'scale(1.1)';
            whatsappBtn.style.boxShadow = '0 8px 25px rgba(37, 211, 102, 0.6)';
        });
        
        whatsappBtn.addEventListener('mouseleave', () => {
            whatsappBtn.style.transform = 'scale(1)';
            whatsappBtn.style.boxShadow = '0 5px 15px rgba(37, 211, 102, 0.4)';
        });
    }
}

// ==================================
// 3. VALIDACIÓN DE FORMULARIO
// ==================================
function initFormValidation() {
    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            // Detener envío para validar primero
            e.preventDefault();
            
            // Obtener valores de los campos
            const getValue = id => document.getElementById(id).value.trim();
            const name = getValue('name');
            const email = getValue('email');
            const phone = getValue('phone');
            const service = document.getElementById('service').value;
            const message = getValue('message');
            
            // Validar campos vacíos
            if (!name || !email || !phone || !service || !message) {
                alert('Por favor complete todos los campos requeridos.');
                return;
            }
            
            // Validar formato de email
            if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                alert('Por favor ingrese un correo electrónico válido.');
                return;
            }
            
            // Validar teléfono (mínimo 8 caracteres)
            if (phone.length < 8) {
                alert('Por favor ingrese un número de teléfono válido.');
                return;
            }
            
            // Si todo está correcto, enviar formulario
            this.submit();
        });
    }
}

// ==================================
// INICIALIZACIÓN AL CARGAR LA PÁGINA
// ==================================
document.addEventListener('DOMContentLoaded', function() {
    initLazyLoading();      // Para todas las páginas con imágenes lazy
    initWhatsAppButton();   // Para todas las páginas con el botón
    initFormValidation();   // Solo para la página de contacto
    
    console.log('Funciones inicializadas correctamente');
});
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
    console.log('🔄 Iniciando lazy loading...');
    
    // CORRECTO: Buscar por clase solamente
    const lazyImages = document.querySelectorAll('.lazy-img');
    
    console.log(`📸 ${lazyImages.length} imágenes encontradas`);
    
    if (lazyImages.length === 0) {
        console.warn('⚠️ No hay elementos con class="lazy-img"');
        return;
    }

    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    
                    // Verificación de seguridad extra
                    if (img && img.tagName === 'IMG' && img.dataset.src) {
                        console.log('🚀 Cargando imagen:', img.dataset.src);
                        img.src = img.dataset.src;
                        img.classList.add('loaded');
                        observer.unobserve(img);
                    } else {
                        console.warn('⚠️ Elemento no es una imagen válida:', img);
                    }
                }
            });
        }, { rootMargin: '0px 0px 200px 0px' });
        
        lazyImages.forEach(img => {
            if (img && img.tagName === 'IMG') {
                observer.observe(img);
            } else {
                console.warn('⚠️ Elemento con clase lazy-img no es una imagen:', img);
            }
        });
    } else {
        // Fallback para navegadores antiguos
        lazyImages.forEach(img => {
            if (img && img.tagName === 'IMG' && img.dataset.src) {
                img.src = img.dataset.src;
                img.classList.add('loaded');
            }
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
// INICIALIZACIÓN SEGURA
// ==================================
function initializeAll() {
    console.log('🎯 Inicializando todas las funciones');
    initLazyLoading();
    initWhatsAppButton();
    initFormValidation();
}

// EJECUCIÓN PRINCIPAL - MÁXIMA SEGURIDAD
if (document.readyState === 'complete') {
    console.log('✅ Página ya cargada, iniciando...');
    initializeAll();
} else {
    console.log('⏳ Esperando carga de la página...');
    window.addEventListener('load', initializeAll);
    document.addEventListener('DOMContentLoaded', initializeAll);
}

// Backup por si acaso
setTimeout(initializeAll, 1000);
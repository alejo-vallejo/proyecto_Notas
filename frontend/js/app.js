const API_URL = '';

async function apiRequest(endpoint, options = {}) {
    const url = `${API_URL}${endpoint}`;
    const config = {
        headers: { 'Content-Type': 'application/json' },
        ...options,
    };
    const response = await fetch(url, config);
    const data = await response.json();
    if (!response.ok) {
        throw new Error(data.detail || 'Error en la solicitud');
    }
    return data;
}

function showAlert(message, type = 'success', containerId = 'alertContainer') {
    const container = document.getElementById(containerId);
    if (!container) return;
    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.textContent = message;
    container.appendChild(alert);
    setTimeout(() => alert.remove(), 4000);
}

function getUsuario() {
    const data = localStorage.getItem('usuario');
    return data ? JSON.parse(data) : null;
}

function setUsuario(usuario) {
    localStorage.setItem('usuario', JSON.stringify(usuario));
}

function logout() {
    localStorage.removeItem('usuario');
    window.location.href = '/login';
}

function redirectIfNotLogged() {
    if (!getUsuario()) {
        window.location.href = '/login';
    }
}

function escaparHTML(texto) {
    const div = document.createElement('div');
    div.textContent = texto;
    return div.innerHTML;
}

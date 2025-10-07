function showToast(title, message, type = 'normal', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    
    if (!toastComponent) return;

    // Remove all type classes first
    toastComponent.classList.remove(
        'bg-red-50', 'border-red-500', 'text-red-600',
        'bg-blue-50', 'border-blue-500', 'text-blue-600',
        'text-gray-800', 'border-blue-300', 'bg-blue-50'
    );

    // Set type styles and icon
    if (type === 'success') {
        toastComponent.classList.add('bg-blue-50', 'border-blue-500', 'text-blue-600');
        toastComponent.style.border = '1px solid #75c6ddff';
    } else if (type === 'error') {
        toastComponent.classList.add('bg-red-50', 'border-red-500', 'text-red-600');
        toastComponent.style.border = '1px solid #ef4444';
    } else {
        toastComponent.classList.add('bg-blue-50', 'border-blue-300', 'text-gray-800');
        toastComponent.style.border = '1px solid #d1d5db';
    }

    toastTitle.textContent = title;
    toastMessage.textContent = message;

    toastComponent.classList.remove('opacity-0', 'translate-y-64');
    toastComponent.classList.add('opacity-90', 'translate-y-0');

    setTimeout(() => {
        toastComponent.classList.remove('opacity-90', 'translate-y-0');
        toastComponent.classList.add('opacity-0', 'translate-y-64');
    }, duration);
}
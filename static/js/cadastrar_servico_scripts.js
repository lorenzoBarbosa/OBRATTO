// Validação e funcionalidades do formulário
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('serviceForm');
    const requiredFields = ['serviceName', 'serviceCategory', 'serviceDescription', 'servicePrice', 'serviceLocation', 'contactPhone'];
    
    // Máscara para telefone
    const phoneInput = document.getElementById('contactPhone');
    if (phoneInput) {
        phoneInput.addEventListener('input', function(e) {
            let value = e.target.value.replace(/\D/g, '');
            if (value.length <= 11) {
                value = value.replace(/(\d{2})(\d{5})(\d{4})/, '($1) $2-$3');
                if (value.length < 14) {
                    value = value.replace(/(\d{2})(\d{4})(\d{4})/, '($1) $2-$3');
                }
            }
            e.target.value = value;
        });
    }

    // Máscara para preço
    const priceInput = document.getElementById('servicePrice');
    const priceType = document.getElementById('priceType');
    
    if (priceInput && priceType) {
        function updatePricePlaceholder() {
            const type = priceType.value;
            switch(type) {
                case 'm2':
                    priceInput.placeholder = 'Ex: R$ 25,00/m²';
                    break;
                case 'hora':
                    priceInput.placeholder = 'Ex: R$ 45,00/hora';
                    break;
                case 'diaria':
                    priceInput.placeholder = 'Ex: R$ 200,00/dia';
                    break;
                case 'fixo':
                    priceInput.placeholder = 'Ex: R$ 500,00';
                    break;
                case 'orcamento':
                    priceInput.placeholder = 'Sob orçamento';
                    break;
            }
        }

        priceType.addEventListener('change', updatePricePlaceholder);
        updatePricePlaceholder();

        priceInput.addEventListener('input', function(e) {
            if (priceType.value !== 'orcamento') {
                let value = e.target.value.replace(/\D/g, '');
                value = (value / 100).toLocaleString('pt-BR', {
                    style: 'currency',
                    currency: 'BRL'
                });
                e.target.value = value;
            }
        });
    }

    // Validação em tempo real
    function validateField(fieldId) {
        const field = document.getElementById(fieldId);
        const errorElement = document.getElementById(fieldId + 'Error');
        
        if (!field || !errorElement) return true;

        let isValid = true;
        let errorMessage = '';

        // Validação específica por campo
        switch(fieldId) {
            case 'serviceName':
                if (field.value.trim().length < 3) {
                    isValid = false;
                    errorMessage = 'Nome do serviço deve ter pelo menos 3 caracteres';
                }
                break;
            
            case 'serviceCategory':
                if (!field.value) {
                    isValid = false;
                    errorMessage = 'Selecione uma categoria';
                }
                break;
            
            case 'serviceDescription':
                if (field.value.trim().length < 20) {
                    isValid = false;
                    errorMessage = 'Descrição deve ter pelo menos 20 caracteres';
                }
                break;
            
            case 'servicePrice':
                if (!field.value.trim()) {
                    isValid = false;
                    errorMessage = 'Informe o preço do serviço';
                }
                break;
            
            case 'serviceLocation':
                if (field.value.trim().length < 3) {
                    isValid = false;
                    errorMessage = 'Informe a área de atuação';
                }
                break;
            
            case 'contactPhone':
                const phoneRegex = /^\(\d{2}\)\s\d{4,5}-\d{4}$/;
                if (!phoneRegex.test(field.value)) {
                    isValid = false;
                    errorMessage = 'Telefone deve estar no formato (11) 99999-9999';
                }
                break;
            
            case 'contactEmail':
                if (field.value && !isValidEmail(field.value)) {
                    isValid = false;
                    errorMessage = 'E-mail inválido';
                }
                break;
        }

        // Exibir ou ocultar erro
        if (isValid) {
            errorElement.textContent = '';
            field.style.borderColor = 'rgba(52, 152, 219, 0.2)';
        } else {
            errorElement.textContent = errorMessage;
            field.style.borderColor = '#e74c3c';
        }

        return isValid;
    }

    // Validação de email
    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    // Adicionar eventos de validação
    requiredFields.forEach(fieldId => {
        const field = document.getElementById(fieldId);
        if (field) {
            field.addEventListener('blur', () => validateField(fieldId));
            field.addEventListener('input', () => {
                // Validação em tempo real para alguns campos
                if (['serviceName', 'serviceDescription'].includes(fieldId)) {
                    setTimeout(() => validateField(fieldId), 500);
                }
            });
        }
    });

    // Validação do email (opcional)
    const emailField = document.getElementById('contactEmail');
    if (emailField) {
        emailField.addEventListener('blur', () => validateField('contactEmail'));
    }

    // Submissão do formulário
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            let isFormValid = true;
            
            // Validar todos os campos obrigatórios
            requiredFields.forEach(fieldId => {
                if (!validateField(fieldId)) {
                    isFormValid = false;
                }
            });

            // Validar email se preenchido
            if (emailField && emailField.value) {
                if (!validateField('contactEmail')) {
                    isFormValid = false;
                }
            }

            if (isFormValid) {
                // Simular envio do formulário
                showSuccessMessage();
                // Aqui você adicionaria a lógica para enviar os dados para o servidor
            } else {
                showErrorMessage('Por favor, corrija os erros antes de continuar.');
                // Focar no primeiro campo com erro
                const firstError = document.querySelector('.error-message:not(:empty)');
                if (firstError) {
                    const fieldId = firstError.id.replace('Error', '');
                    const field = document.getElementById(fieldId);
                    if (field) {
                        field.focus();
                        field.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    }
                }
            }
        });
    }

    // Função para exibir mensagem de sucesso
    function showSuccessMessage() {
        // Remover mensagens anteriores
        removeMessages();
        
        const successDiv = document.createElement('div');
        successDiv.className = 'success-message';
        successDiv.innerHTML = `
            <div style="
                background: linear-gradient(135deg, #00b894 0%, #00cec9 100%);
                color: white;
                padding: 20px;
                border-radius: 10px;
                margin: 20px 0;
                text-align: center;
                box-shadow: 0 4px 15px rgba(0, 184, 148, 0.3);
                animation: slideIn 0.5s ease;
            ">
                <h3 style="margin: 0 0 10px 0;">✅ Serviço cadastrado com sucesso!</h3>
                <p style="margin: 0;">Seu serviço foi registrado e estará disponível em breve.</p>
            </div>
        `;
        
        form.insertBefore(successDiv, form.firstChild);
        
        // Rolar para o topo
        successDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        
        // Limpar formulário após 3 segundos
        setTimeout(() => {
            form.reset();
            removeMessages();
        }, 3000);
    }

    // Função para exibir mensagem de erro
    function showErrorMessage(message) {
        removeMessages();
        
        const errorDiv = document.createElement('div');
        errorDiv.className = 'form-error-message';
        errorDiv.innerHTML = `
            <div style="
                background: linear-gradient(135deg, #e17055 0%, #d63031 100%);
                color: white;
                padding: 15px;
                border-radius: 10px;
                margin: 20px 0;
                text-align: center;
                box-shadow: 0 4px 15px rgba(225, 112, 85, 0.3);
                animation: slideIn 0.5s ease;
            ">
                <strong>❌ ${message}</strong>
            </div>
        `;
        
        form.insertBefore(errorDiv, form.firstChild);
        errorDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    // Função para remover mensagens
    function removeMessages() {
        const messages = document.querySelectorAll('.success-message, .form-error-message');
        messages.forEach(msg => msg.remove());
    }

    // Adicionar animações CSS
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .form-group input:invalid:not(:focus):not(:placeholder-shown),
        .form-group select:invalid:not(:focus),
        .form-group textarea:invalid:not(:focus):not(:placeholder-shown) {
            border-color: #e74c3c;
            animation: shake 0.5s ease-in-out;
        }
        
        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-5px); }
            75% { transform: translateX(5px); }
        }
    `;
    document.head.appendChild(style);
});

// Função para coletar dados do formulário (para uso futuro)
function getFormData() {
    const formData = new FormData(document.getElementById('serviceForm'));
    const data = {};
    
    for (let [key, value] of formData.entries()) {
        if (data[key]) {
            // Se já existe, transformar em array
            if (Array.isArray(data[key])) {
                data[key].push(value);
            } else {
                data[key] = [data[key], value];
            }
        } else {
            data[key] = value;
        }
    }
    
    return data;
}


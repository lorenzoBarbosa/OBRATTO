const prestadores = [
    {
        id: 1,
        nome: "João da Silva Serviços Gerais",
        cpf: "123.456.789-00",
        email: "joao@email.com",
        telefone: "(11) 98765-4321",
        endereco: "Rua dos Serviços, 45 - São Paulo, SP",
        status: "pendente",
        dataCadastro: "28/01/2025",
        servicosOferecidos: "Eletricista, Encanador, Pintor",
        denuncias: [],
        advertencias: 0,
        documentos: [
            { nome: "Documento de Identidade (RG/CNH)", status: "pendente" },
            { nome: "CPF", status: "pendente" }
        ]
    },
    {
        id: 2,
        nome: "Maria Santos Reparos Rápidos",
        cpf: "987.654.321-00",
        email: "maria@email.com",
        telefone: "(21) 91234-5678",
        endereco: "Av. dos Reparos, 101 - Rio de Janeiro, RJ",
        status: "aprovado",
        dataCadastro: "15/01/2025",
        servicosOferecidos: "Encanador, Reparos Hidráulicos",
        denuncias: [
            {
                tipo: "Serviço mal feito",
                data: "26/01/2025",
                descricao: "O conserto da pia ficou pingando logo após o serviço ser concluído.",
                cliente: "Pedro Almeida"
            },
            {
                tipo: "Cobrança indevida",
                data: "24/01/2025",
                descricao: "Cobrou um valor diferente do combinado no orçamento inicial.",
                cliente: "Carla Pires"
            }
        ],
        advertencias: 0,
        documentos: [
            { nome: "Documento de Identidade (RG/CNH)", status: "verificado" },
            { nome: "CPF", status: "verificado" }
        ]
    },
    {
        id: 3,
        nome: "Serviços Express",
        cpf: "111.222.333-44",
        email: "servicos_express@email.com",
        telefone: "(31) 98765-1234",
        endereco: "Rua das Limpezas, 202 - Belo Horizonte, MG",
        status: "advertido",
        dataCadastro: "10/01/2025",
        servicosOferecidos: "Limpeza Residencial e Comercial",
        denuncias: [
             {
                tipo: "Má conduta",
                data: "25/01/2025",
                descricao: "Prestador chegou atrasado e teve atitude grosseira.",
                cliente: "Roberto Carlos"
            }
        ],
        advertencias: 1,
        documentos: [
            { nome: "Documento de Identidade (RG/CNH)", status: "verificado" },
            { nome: "CPF", status: "verificado" }
        ]
    },
    {
        id: 4,
        nome: "Pedro Lopes Jardinagem",
        cpf: "555.666.777-88",
        email: "pedro.lopes@email.com",
        telefone: "(41) 92345-6789",
        endereco: "Av. das Flores, 303 - Curitiba, PR",
        status: "aprovado",
        dataCadastro: "05/01/2025",
        servicosOferecidos: "Jardinagem, Paisagismo, Poda de Árvores",
        denuncias: [],
        advertencias: 0,
        documentos: [
            { nome: "Documento de Identidade (RG/CNH)", status: "verificado" },
            { nome: "CPF", status: "verificado" }
        ]
    }
];

function aprovarPrestador(id) {
    mostrarConfirmacao(
        'Aprovar Prestador',
        'Tem certeza que deseja aprovar este prestador? Ele poderá começar a oferecer serviços na plataforma.',
        () => {
            console.log('Aprovando prestador:', id);
            atualizarStatusPrestador(id, 'aprovado');
            mostrarNotificacao('Prestador aprovado com sucesso!', 'success');
        }
    );
}

function rejeitarPrestador(id) {
    mostrarConfirmacao(
        'Rejeitar Prestador',
        'Tem certeza que deseja rejeitar este prestador? Esta ação não pode ser desfeita.',
        () => {
            const motivo = document.getElementById('motivoAcao').value;
            console.log('Rejeitando prestador:', id, 'Motivo:', motivo);
            atualizarStatusPrestador(id, 'rejeitado');
            mostrarNotificacao('Prestador rejeitado com sucesso!', 'warning');
        },
        true
    );
}

function advertirPrestador(id) {
    mostrarConfirmacao(
        'Advertir Prestador',
        'Tem certeza que deseja advertir este prestador? A advertência ficará registrada no histórico.',
        () => {
            const motivo = document.getElementById('motivoAcao').value;
            console.log('Advertindo prestador:', id, 'Motivo:', motivo);
            atualizarStatusPrestador(id, 'advertido');
            mostrarNotificacao('Advertência aplicada com sucesso!', 'warning');
        },
        true
    );
}

function banirPrestador(id) {
    mostrarConfirmacao(
        'Banir Prestador',
        'ATENÇÃO: Esta ação irá banir permanentemente o prestador da plataforma. Esta ação não pode ser desfeita.',
        () => {
            const motivo = document.getElementById('motivoAcao').value;
            console.log('Banindo prestador:', id, 'Motivo:', motivo);
            atualizarStatusPrestador(id, 'banido');
            mostrarNotificacao('Prestador banido permanentemente!', 'danger');
        },
        true
    );
}

function verDetalhes(id) {
    const prestador = prestadores.find(p => p.id === id);
    if (prestador) {
        const documentosHtml = prestador.documentos.map(doc => 
            `<div class="documento-item">
                <span class="documento-nome">${doc.nome}</span>
                <span class="documento-status doc-${doc.status}">${doc.status}</span>
            </div>`
        ).join('');
        
        const denunciasHtml = prestador.denuncias.length > 0 ? 
            prestador.denuncias.map(denuncia => 
                `<div class="denuncia-item">
                    <div class="denuncia-header">
                        <span class="denuncia-tipo">${denuncia.tipo}</span>
                        <span class="denuncia-data">${denuncia.data}</span>
                    </div>
                    <div class="denuncia-descricao">${denuncia.descricao}</div>
                    <small class="text-muted">Denunciante: ${denuncia.cliente}</small>
                </div>`
            ).join('') : '<p class="text-muted">Nenhuma denúncia registrada.</p>';
        
        const content = `
            <div class="row">
                <div class="col-md-6">
                    <h6><strong>Informações do Prestador</strong></h6>
                    <p><strong>Nome:</strong> ${prestador.nome}</p>
                    <p><strong>CPF:</strong> ${prestador.cpf}</p>
                    <p><strong>Serviços:</strong> ${prestador.servicosOferecidos}</p>
                    <p><strong>Status:</strong> <span class="badge status-${prestador.status}">${prestador.status}</span></p>
                    <p><strong>Data de Cadastro:</strong> ${prestador.dataCadastro}</p>
                </div>
                <div class="col-md-6">
                    <h6><strong>Contato</strong></h6>
                    <p><strong>Email:</strong> ${prestador.email}</p>
                    <p><strong>Telefone:</strong> ${prestador.telefone}</p>
                    <p><strong>Endereço:</strong> ${prestador.endereco}</p>
                    <p><strong>Advertências:</strong> ${prestador.advertencias}</p>
                    <p><strong>Denúncias:</strong> ${prestador.denuncias.length}</p>
                </div>
            </div>
            <div class="row mt-4">
                <div class="col-md-6">
                    <h6><strong>Documentos</strong></h6>
                    <div class="documentos-list">
                        ${documentosHtml}
                    </div>
                </div>
                <div class="col-md-6">
                    <h6><strong>Denúncias (${prestador.denuncias.length})</strong></h6>
                    <div class="denuncias-list">
                        ${denunciasHtml}
                    </div>
                </div>
            </div>
        `;
        
        document.getElementById('modalDetalhesContent').innerHTML = content;
        
        const modalAcoes = document.getElementById('modalAcoes');
        modalAcoes.innerHTML = '';
        
        if (prestador.status === 'pendente') {
            modalAcoes.innerHTML = `
                <button type="button" class="btn btn-success" onclick="aprovarPrestador(${id}); bootstrap.Modal.getInstance(document.getElementById('modalDetalhes')).hide();">
                    <i class="bi bi-check-lg me-1"></i>Aprovar
                </button>
                <button type="button" class="btn btn-danger" onclick="rejeitarPrestador(${id}); bootstrap.Modal.getInstance(document.getElementById('modalDetalhes')).hide();">
                    <i class="bi bi-x-lg me-1"></i>Rejeitar
                </button>
            `;
        } else if (prestador.status === 'aprovado' && prestador.denuncias.length > 0) {
            modalAcoes.innerHTML = `
                <button type="button" class="btn btn-warning" onclick="advertirPrestador(${id}); bootstrap.Modal.getInstance(document.getElementById('modalDetalhes')).hide();">
                    <i class="bi bi-exclamation-triangle me-1"></i>Advertir
                </button>
                <button type="button" class="btn btn-danger" onclick="banirPrestador(${id}); bootstrap.Modal.getInstance(document.getElementById('modalDetalhes')).hide();">
                    <i class="bi bi-ban me-1"></i>Banir
                </button>
            `;
        } else if (prestador.status === 'advertido') {
            modalAcoes.innerHTML = `
                <button type="button" class="btn btn-danger" onclick="banirPrestador(${id}); bootstrap.Modal.getInstance(document.getElementById('modalDetalhes')).hide();">
                    <i class="bi bi-ban me-1"></i>Banir Permanentemente
                </button>
            `;
        }
        
        new bootstrap.Modal(document.getElementById('modalDetalhes')).show();
    }
}

function mostrarConfirmacao(titulo, texto, callback, precisaMotivo = false) {
    document.getElementById('modalConfirmacaoTitulo').textContent = titulo;
    document.getElementById('modalConfirmacaoTexto').textContent = texto;
    
    const motivoContainer = document.getElementById('motivoContainer');
    if (precisaMotivo) {
        motivoContainer.style.display = 'block';
        document.getElementById('motivoAcao').value = '';
    } else {
        motivoContainer.style.display = 'none';
    }
    
    document.getElementById('btnConfirmarAcao').onclick = () => {
        if (precisaMotivo && !document.getElementById('motivoAcao').value.trim()) {
            alert('Por favor, informe o motivo da ação.');
            return;
        }
        callback();
        bootstrap.Modal.getInstance(document.getElementById('modalConfirmacao')).hide();
    };
    
    new bootstrap.Modal(document.getElementById('modalConfirmacao')).show();
}

function atualizarStatusPrestador(id, novoStatus) {
    const prestadorCard = document.querySelector(`.prestador-card[data-id="${id}"]`);
    if (prestadorCard) {
        prestadorCard.classList.remove('pendente', 'aprovado', 'rejeitado', 'advertido', 'banido');
        prestadorCard.classList.add(novoStatus);
        prestadorCard.dataset.status = novoStatus;
        const statusBadge = prestadorCard.querySelector('.prestador-status');
        statusBadge.textContent = novoStatus.charAt(0).toUpperCase() + novoStatus.slice(1);
        statusBadge.classList.remove('status-pendente', 'status-aprovado', 'status-rejeitado', 'status-advertido', 'status-banido');
        statusBadge.classList.add(`status-${novoStatus}`);
        
        // Simulação de atualização de dados, em um sistema real isso seria feito no backend.
        const prestador = prestadores.find(p => p.id === id);
        if (prestador) {
            prestador.status = novoStatus;
            if (novoStatus === 'advertido') {
                prestador.advertencias += 1;
            }
        }
    }
    atualizarEstatisticas();
}

function atualizarEstatisticas() {
    const cards = document.querySelectorAll('.prestador-card');
    let total = cards.length;
    let pendentes = document.querySelectorAll('.prestador-card.pendente').length;
    let aprovados = document.querySelectorAll('.prestador-card.aprovado').length;
    let rejeitados = document.querySelectorAll('.prestador-card.rejeitado').length;
    let advertidos = document.querySelectorAll('.prestador-card.advertido').length;
    let banidos = document.querySelectorAll('.prestador-card.banido').length;
    
    document.getElementById('totalPrestadores').textContent = total;
    document.getElementById('pendentes').textContent = pendentes;
    document.getElementById('aprovados').textContent = aprovados;
    document.getElementById('rejeitados').textContent = rejeitados;
    document.getElementById('advertidos').textContent = advertidos;
    document.getElementById('banidos').textContent = banidos;
}

function aplicarFiltros() {
    const busca = document.getElementById('buscarPrestador').value.toLowerCase();
    const status = document.getElementById('filtroStatus').value;
    const denuncias = document.getElementById('filtroDenuncias').value;
    
    const cards = document.querySelectorAll('.prestador-card');
    
    cards.forEach(card => {
        const nome = card.querySelector('.prestador-nome').textContent.toLowerCase();
        const cardStatus = card.dataset.status;
        const cardDenuncias = parseInt(card.dataset.denuncias);
        
        let mostrar = true;
        
        if (busca && !nome.includes(busca)) {
            mostrar = false;
        }

        if (status && cardStatus !== status) {
            mostrar = false;
        }
        
        if (denuncias === 'com_denuncias' && cardDenuncias === 0) {
            mostrar = false;
        } else if (denuncias === 'sem_denuncias' && cardDenuncias > 0) {
            mostrar = false;
        }
        
        card.style.display = mostrar ? 'block' : 'none';
    });
}

function mostrarNotificacao(mensagem, tipo) {
    const toast = document.createElement('div');
    toast.className = `alert alert-${tipo} alert-dismissible fade show position-fixed`;
    toast.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    toast.innerHTML = `
        ${mensagem}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(toast);
    
    setTimeout(() => {
        if (toast.parentNode) {
            toast.remove();
        }
    }, 5000);
}

document.addEventListener('DOMContentLoaded', function() {
    atualizarEstatisticas();
    
    document.getElementById('buscarPrestador').addEventListener('input', aplicarFiltros);
    document.getElementById('filtroStatus').addEventListener('change', aplicarFiltros);
    document.getElementById('filtroDenuncias').addEventListener('change', aplicarFiltros);
});
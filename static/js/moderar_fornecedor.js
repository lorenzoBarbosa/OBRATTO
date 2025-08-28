const fornecedores = [
    {
        id: 1,
        nome: "Materiais São Paulo Ltda",
        razaoSocial: "Materiais São Paulo Ltda",
        cnpj: "12.345.678/0001-90",
        responsavel: "Carlos Silva",
        email: "contato@materiaissp.com.br",
        telefone: "(11) 3333-3333",
        endereco: "Rua das Obras, 123 - São Paulo, SP",
        status: "pendente",
        dataCadastro: "28/01/2025",
        denuncias: [],
        advertencias: 0,
        documentos: [
            { nome: "Contrato Social", status: "pendente" },
            { nome: "CNPJ", status: "pendente" },
            { nome: "Inscrição Estadual", status: "pendente" }
        ]
    },
    {
        id: 2,
        nome: "Construmax Materiais",
        razaoSocial: "Construmax Materiais de Construção Ltda",
        cnpj: "98.765.432/0001-10",
        responsavel: "Ana Santos",
        email: "vendas@construmax.com.br",
        telefone: "(21) 2222-2222",
        endereco: "Av. Principal, 456 - Rio de Janeiro, RJ",
        status: "aprovado",
        dataCadastro: "15/01/2025",
        denuncias: [
            {
                tipo: "Atraso na Entrega",
                data: "26/01/2025",
                descricao: "Fornecedor atrasou a entrega de materiais em 3 dias sem aviso prévio.",
                cliente: "João Silva"
            },
            {
                tipo: "Produto Defeituoso",
                data: "24/01/2025",
                descricao: "Cimento entregue estava com embalagem danificada e produto endurecido.",
                cliente: "Maria Oliveira"
            }
        ],
        advertencias: 0,
        documentos: [
            { nome: "Contrato Social", status: "verificado" },
            { nome: "CNPJ", status: "verificado" },
            { nome: "Inscrição Estadual", status: "verificado" }
        ]
    }
];

function aprovarFornecedor(id) {
    mostrarConfirmacao(
        'Aprovar Fornecedor',
        'Tem certeza que deseja aprovar este fornecedor? Ele poderá começar a vender na plataforma.',
        () => {
            console.log('Aprovando fornecedor:', id);
            atualizarStatusFornecedor(id, 'aprovado');
            mostrarNotificacao('Fornecedor aprovado com sucesso!', 'success');
        }
    );
}

function rejeitarFornecedor(id) {
    mostrarConfirmacao(
        'Rejeitar Fornecedor',
        'Tem certeza que deseja rejeitar este fornecedor? Esta ação não pode ser desfeita.',
        () => {
            const motivo = document.getElementById('motivoAcao').value;
            console.log('Rejeitando fornecedor:', id, 'Motivo:', motivo);
            atualizarStatusFornecedor(id, 'rejeitado');
            mostrarNotificacao('Fornecedor rejeitado com sucesso!', 'warning');
        },
        true
    );
}

function advertirFornecedor(id) {
    mostrarConfirmacao(
        'Advertir Fornecedor',
        'Tem certeza que deseja advertir este fornecedor? A advertência ficará registrada no histórico.',
        () => {
            const motivo = document.getElementById('motivoAcao').value;
            console.log('Advertindo fornecedor:', id, 'Motivo:', motivo);
            atualizarStatusFornecedor(id, 'advertido');
            mostrarNotificacao('Advertência aplicada com sucesso!', 'warning');
        },
        true
    );
}

function banirFornecedor(id) {
    mostrarConfirmacao(
        'Banir Fornecedor',
        'ATENÇÃO: Esta ação irá banir permanentemente o fornecedor da plataforma. Esta ação não pode ser desfeita.',
        () => {
            const motivo = document.getElementById('motivoAcao').value;
            console.log('Banindo fornecedor:', id, 'Motivo:', motivo);
            atualizarStatusFornecedor(id, 'banido');
            mostrarNotificacao('Fornecedor banido permanentemente!', 'danger');
        },
        true
    );
}

function verDetalhes(id) {
    const fornecedor = fornecedores.find(f => f.id === id);
    if (fornecedor) {
        const documentosHtml = fornecedor.documentos.map(doc => 
            `<div class="documento-item">
                <span class="documento-nome">${doc.nome}</span>
                <span class="documento-status doc-${doc.status}">${doc.status}</span>
            </div>`
        ).join('');
        
        const denunciasHtml = fornecedor.denuncias.length > 0 ? 
            fornecedor.denuncias.map(denuncia => 
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
                    <h6><strong>Informações da Empresa</strong></h6>
                    <p><strong>Nome:</strong> ${fornecedor.nome}</p>
                    <p><strong>Razão Social:</strong> ${fornecedor.razaoSocial}</p>
                    <p><strong>CNPJ:</strong> ${fornecedor.cnpj}</p>
                    <p><strong>Responsável:</strong> ${fornecedor.responsavel}</p>
                    <p><strong>Status:</strong> <span class="badge status-${fornecedor.status}">${fornecedor.status}</span></p>
                    <p><strong>Data de Cadastro:</strong> ${fornecedor.dataCadastro}</p>
                </div>
                <div class="col-md-6">
                    <h6><strong>Contato</strong></h6>
                    <p><strong>Email:</strong> ${fornecedor.email}</p>
                    <p><strong>Telefone:</strong> ${fornecedor.telefone}</p>
                    <p><strong>Endereço:</strong> ${fornecedor.endereco}</p>
                    <p><strong>Advertências:</strong> ${fornecedor.advertencias}</p>
                    <p><strong>Denúncias:</strong> ${fornecedor.denuncias.length}</p>
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
                    <h6><strong>Denúncias (${fornecedor.denuncias.length})</strong></h6>
                    <div class="denuncias-list">
                        ${denunciasHtml}
                    </div>
                </div>
            </div>
        `;
        
        document.getElementById('modalDetalhesContent').innerHTML = content;
        
        const modalAcoes = document.getElementById('modalAcoes');
        modalAcoes.innerHTML = '';
        
        if (fornecedor.status === 'pendente') {
            modalAcoes.innerHTML = `
                <button type="button" class="btn btn-success" onclick="aprovarFornecedor(${id}); bootstrap.Modal.getInstance(document.getElementById('modalDetalhes')).hide();">
                    <i class="bi bi-check-lg me-1"></i>Aprovar
                </button>
                <button type="button" class="btn btn-danger" onclick="rejeitarFornecedor(${id}); bootstrap.Modal.getInstance(document.getElementById('modalDetalhes')).hide();">
                    <i class="bi bi-x-lg me-1"></i>Rejeitar
                </button>
            `;
        } else if (fornecedor.status === 'aprovado' && fornecedor.denuncias.length > 0) {
            modalAcoes.innerHTML = `
                <button type="button" class="btn btn-warning" onclick="advertirFornecedor(${id}); bootstrap.Modal.getInstance(document.getElementById('modalDetalhes')).hide();">
                    <i class="bi bi-exclamation-triangle me-1"></i>Advertir
                </button>
                <button type="button" class="btn btn-danger" onclick="banirFornecedor(${id}); bootstrap.Modal.getInstance(document.getElementById('modalDetalhes')).hide();">
                    <i class="bi bi-ban me-1"></i>Banir
                </button>
            `;
        } else if (fornecedor.status === 'advertido') {
            modalAcoes.innerHTML = `
                <button type="button" class="btn btn-danger" onclick="banirFornecedor(${id}); bootstrap.Modal.getInstance(document.getElementById('modalDetalhes')).hide();">
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

function atualizarStatusFornecedor(id, novoStatus) {
    atualizarEstatisticas();
}

function atualizarEstatisticas() {
    const cards = document.querySelectorAll('.fornecedor-card');
    let total = cards.length;
    let pendentes = document.querySelectorAll('.fornecedor-card.pendente').length;
    let aprovados = document.querySelectorAll('.fornecedor-card.aprovado').length;
    let rejeitados = document.querySelectorAll('.fornecedor-card.rejeitado').length;
    let advertidos = document.querySelectorAll('.fornecedor-card.advertido').length;
    let banidos = document.querySelectorAll('.fornecedor-card.banido').length;
    
    document.getElementById('totalFornecedores').textContent = total;
    document.getElementById('pendentes').textContent = pendentes;
    document.getElementById('aprovados').textContent = aprovados;
    document.getElementById('rejeitados').textContent = rejeitados;
    document.getElementById('advertidos').textContent = advertidos;
    document.getElementById('banidos').textContent = banidos;
}

function aplicarFiltros() {
    const busca = document.getElementById('buscarFornecedor').value.toLowerCase();
    const status = document.getElementById('filtroStatus').value;
    const denuncias = document.getElementById('filtroDenuncias').value;
    
    const cards = document.querySelectorAll('.fornecedor-card');
    
    cards.forEach(card => {
        const nome = card.querySelector('.fornecedor-nome').textContent.toLowerCase();
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
    
    document.getElementById('buscarFornecedor').addEventListener('input', aplicarFiltros);
    document.getElementById('filtroStatus').addEventListener('change', aplicarFiltros);
    document.getElementById('filtroDenuncias').addEventListener('change', aplicarFiltros);
});
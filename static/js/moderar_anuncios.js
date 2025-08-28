const anuncios = [
    {
        id: 1,
        titulo: "Serviços de Pedreiro Especializado",
        usuario: "João Silva",
        tipo: "prestador",
        status: "pendente",
        data: "28/01/2025",
        localizacao: "São Paulo, SP",
        categoria: "Construção",
        descricao: "Oferecemos serviços completos de pedreiro com mais de 15 anos de experiência. Especializado em alvenaria, acabamentos, reformas residenciais e comerciais. Orçamento gratuito e garantia de qualidade.",
        telefone: "(11) 99999-9999",
        email: "joao.silva@email.com",
        experiencia: "15 anos",
        preco: "R$ 80/hora"
    },
    {
        id: 2,
        titulo: "Materiais de Construção - Preços Especiais",
        usuario: "Construmax Ltda",
        tipo: "fornecedor",
        status: "aprovado",
        data: "27/01/2025",
        localizacao: "Rio de Janeiro, RJ",
        categoria: "Materiais",
        descricao: "Fornecemos materiais de construção com os melhores preços da região. Cimento, areia, brita, tijolos, telhas e muito mais. Entrega rápida e atendimento especializado.",
        telefone: "(21) 3333-3333",
        email: "vendas@construmax.com.br",
        cnpj: "12.345.678/0001-90",
        endereco: "Rua das Obras, 123 - Centro"
    }
];

function aprovarAnuncio(id) {
    mostrarConfirmacao(
        'Aprovar Anúncio',
        'Tem certeza que deseja aprovar este anúncio? Ele ficará visível para todos os usuários.',
        () => {
            // Aqui você faria a chamada para a API
            console.log('Aprovando anúncio:', id);
            atualizarStatusAnuncio(id, 'aprovado');
            mostrarNotificacao('Anúncio aprovado com sucesso!', 'success');
        }
    );
}

function rejeitarAnuncio(id) {
    mostrarConfirmacao(
        'Rejeitar Anúncio',
        'Tem certeza que deseja rejeitar este anúncio? Esta ação não pode ser desfeita.',
        () => {
            // Aqui você faria a chamada para a API
            console.log('Rejeitando anúncio:', id);
            atualizarStatusAnuncio(id, 'rejeitado');
            mostrarNotificacao('Anúncio rejeitado com sucesso!', 'warning');
        }
    );
}

function verDetalhes(id) {
    const anuncio = anuncios.find(a => a.id === id);
    if (anuncio) {
        const content = `
            <div class="row">
                <div class="col-md-6">
                    <h6><strong>Informações Básicas</strong></h6>
                    <p><strong>Título:</strong> ${anuncio.titulo}</p>
                    <p><strong>Usuário:</strong> ${anuncio.usuario}</p>
                    <p><strong>Tipo:</strong> ${anuncio.tipo}</p>
                    <p><strong>Status:</strong> <span class="badge status-${anuncio.status}">${anuncio.status}</span></p>
                    <p><strong>Data:</strong> ${anuncio.data}</p>
                    <p><strong>Localização:</strong> ${anuncio.localizacao}</p>
                </div>
                <div class="col-md-6">
                    <h6><strong>Contato</strong></h6>
                    <p><strong>Telefone:</strong> ${anuncio.telefone || 'Não informado'}</p>
                    <p><strong>Email:</strong> ${anuncio.email || 'Não informado'}</p>
                    ${anuncio.cnpj ? `<p><strong>CNPJ:</strong> ${anuncio.cnpj}</p>` : ''}
                    ${anuncio.experiencia ? `<p><strong>Experiência:</strong> ${anuncio.experiencia}</p>` : ''}
                    ${anuncio.preco ? `<p><strong>Preço:</strong> ${anuncio.preco}</p>` : ''}
                </div>
            </div>
            <div class="row mt-3">
                <div class="col-12">
                    <h6><strong>Descrição Completa</strong></h6>
                    <p>${anuncio.descricao}</p>
                </div>
            </div>
        `;
        
        document.getElementById('modalDetalhesContent').innerHTML = content;
        
        document.getElementById('btnAprovarModal').onclick = () => {
            aprovarAnuncio(id);
            bootstrap.Modal.getInstance(document.getElementById('modalDetalhes')).hide();
        };
        
        document.getElementById('btnRejeitarModal').onclick = () => {
            rejeitarAnuncio(id);
            bootstrap.Modal.getInstance(document.getElementById('modalDetalhes')).hide();
        };
        
        new bootstrap.Modal(document.getElementById('modalDetalhes')).show();
    }
}

function mostrarConfirmacao(titulo, texto, callback) {
    document.getElementById('modalConfirmacaoTitulo').textContent = titulo;
    document.getElementById('modalConfirmacaoTexto').textContent = texto;
    document.getElementById('btnConfirmarAcao').onclick = () => {
        callback();
        bootstrap.Modal.getInstance(document.getElementById('modalConfirmacao')).hide();
    };
    new bootstrap.Modal(document.getElementById('modalConfirmacao')).show();
}

function atualizarStatusAnuncio(id, novoStatus) {
    const cards = document.querySelectorAll('.anuncio-card');
    cards.forEach(card => {
    });
    
    atualizarEstatisticas();
}

function atualizarEstatisticas() {
    const pendentes = document.querySelectorAll('.anuncio-card.pendente').length;
    const aprovados = document.querySelectorAll('.anuncio-card.aprovado').length;
    const rejeitados = document.querySelectorAll('.anuncio-card.rejeitado').length;
    const total = pendentes + aprovados + rejeitados;
    
    document.getElementById('totalAnuncios').textContent = total;
    document.getElementById('pendentes').textContent = pendentes;
    document.getElementById('aprovados').textContent = aprovados;
    document.getElementById('rejeitados').textContent = rejeitados;
}

function aplicarFiltros() {
    const busca = document.getElementById('buscarAnuncio').value.toLowerCase();
    const status = document.getElementById('filtroStatus').value;
    const tipo = document.getElementById('filtroTipo').value;
    
    const cards = document.querySelectorAll('.anuncio-card');
    
    cards.forEach(card => {
        const titulo = card.querySelector('.anuncio-titulo').textContent.toLowerCase();
        const descricao = card.querySelector('.anuncio-descricao').textContent.toLowerCase();
        const cardStatus = card.dataset.status;
        const cardTipo = card.dataset.tipo;
        
        let mostrar = true;
        
        if (busca && !titulo.includes(busca) && !descricao.includes(busca)) {
            mostrar = false;
        }
        
        if (status && cardStatus !== status) {
            mostrar = false;
        }
        
        if (tipo && cardTipo !== tipo) {
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
    
    document.getElementById('buscarAnuncio').addEventListener('input', aplicarFiltros);
    document.getElementById('filtroStatus').addEventListener('change', aplicarFiltros);
    document.getElementById('filtroTipo').addEventListener('change', aplicarFiltros);
});
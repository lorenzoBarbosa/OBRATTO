document.addEventListener("DOMContentLoaded", () => {
    const toggleBtn = document.querySelector(".toggle-btn");
    const sidebar = document.querySelector(".sidebar");

    if (toggleBtn && sidebar) {
        toggleBtn.addEventListener("click", () => {
            sidebar.classList.toggle("show");
        });
    }
});

function confirmDelete(productId, productName) {
    document.getElementById('productNameToDelete').textContent = productName;
    document.getElementById('confirmDeleteBtn').onclick = function () {
        window.location.href = '/fornecedor/produtos/excluir/' + productId;
    };
    new bootstrap.Modal(document.getElementById('deleteModal')).show();
}

function viewProduct(productId) {
    const productCard = document.querySelector(`[data-product-id="${productId}"]`);
    const name = productCard.querySelector('.product-name').textContent;
    const description = productCard.querySelector('.product-description').textContent;
    const price = productCard.querySelector('.price').textContent;
    const quantity = productCard.querySelector('.quantity').textContent;

    document.getElementById('modalProductId').textContent = productId;
    document.getElementById('modalProductName').textContent = name;
    document.getElementById('modalProductDescription').textContent = description;
    document.getElementById('modalProductPrice').textContent = price;
    document.getElementById('modalProductQuantity').textContent = quantity;

    document.getElementById('editFromModal').onclick = function () {
        window.location.href = '/fornecedor/produtos/atualizar/' + productId;
    };

    new bootstrap.Modal(document.getElementById('viewProductModal')).show();
}

document.querySelectorAll('.view-btn').forEach(btn => {
    btn.addEventListener('click', function () {
        document.querySelectorAll('.view-btn').forEach(b => b.classList.remove('active'));
        this.classList.add('active');

        const view = this.dataset.view;
        const container = document.getElementById('productsContainer');

        if (view === 'list') {
            container.classList.add('list-view');
        } else {
            container.classList.remove('list-view');
        }
    });
});

setTimeout(function () {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        if (alert.classList.contains('show')) {
            bootstrap.Alert.getOrCreateInstance(alert).close();
        }
    });
}, 5000);

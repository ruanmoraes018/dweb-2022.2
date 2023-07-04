var rotaId; // Define a variável rotaId como uma variável global

$('#confirmarDelecao').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) // Botão que acionou o modal
    rotaId = button.data('rota') // Define o valor da variável rotaId
    
    // Atualiza a URL de deleção com o ID da rota
})
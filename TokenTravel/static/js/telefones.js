function validarTelefone() {
    var telefone = document.getElementById("cadastro-telefone").value;
    if (telefone === "") {
        alert("Por favor, informe o número de telefone.");
        return false;
    } else if (telefone.length < 15) {
        alert("O número de telefone informado é inválido.");
        return false;
    } else {
        return true;
    }
}
// Obtém o elemento de entrada de telefone
var telefoneInput = document.getElementById('cadastro-telefone');

// Adiciona um ouvinte de eventos ao elemento de entrada de telefone
telefoneInput.addEventListener('input', function() {
    // Remove todos os caracteres não numéricos do número de telefone
    var numeroTelefone = this.value.replace(/\D/g, '');

    // Aplica a formatação de telefone com parênteses e traços
    if (numeroTelefone.length == 11) {
      numeroTelefone = numeroTelefone.replace(/^(\d{2})(\d{5})(\d{4})$/, '($1) $2-$3');
    } else if (numeroTelefone.length == 10) {
      numeroTelefone = numeroTelefone.replace(/^(\d{2})(\d{4})(\d{4})$/, '($1) $2-$3');
    } else {
      numeroTelefone = numeroTelefone.replace(/^(\d{2})(\d{4})(\d{0,4})$/, '($1) $2-$3');
    }

    // Define o valor do elemento de entrada de telefone formatado
    this.value = numeroTelefone;
});
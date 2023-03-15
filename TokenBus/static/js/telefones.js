function validarTelefone() {
    var telefone = document.getElementById("inputTelefone").value;
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
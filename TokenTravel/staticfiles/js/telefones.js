function validarTelefone() {
    var telefone = document.getElementById("telefone").value;
    if (telefone === "") {
        alert("Por favor, informe o número de telefone.");
        return false;
    } else if (telefone.length < 11) {
        alert("O número de telefone informado é inválido.");
        return false;
    } else {
        return true;}}
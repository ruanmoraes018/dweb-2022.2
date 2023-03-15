function validarSenha() {
    var senha = document.getElementById("inputPassword").value;
    var confirmarSenha = document.getElementById("inputConfirmarSenha").value;
    if (senha != confirmarSenha) {
        alert("As senhas não coincidem!");
        return false;
    }
        return true;
}
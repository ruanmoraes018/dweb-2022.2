function validarSenhas() {
    var senha = document.getElementById('password').value;
    var confirmarSenha = document.getElementById('confirmar_senha').value;

    if (senha !== confirmarSenha) {
      alert('As senhas não coincidem!');
    }
  }

function verificarDigitacao(event) {
    if (event.target.value.length > 20) {
        alert("Texto muito longo!");
    }
    }

function validarSenha() {
    var senha = document.getElementById("senha").value;
    var uppercase = /[A-Z]/;
    var numero = /[0-9]/;
    var especial = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/;

    if (senha.length < 6) {
        alert("A senha deve ter pelo menos 6 caracteres.");
        return false;
    }
    if (!uppercase.test(senha) || !numero.test(senha) || !especial.test(senha)) {
        alert("A senha deve conter pelo menos uma letra maiúscula, um número e um caractere especial.");
        return false;
    }
    return true;
    }

function validarCadastro() {
  var senha = document.getElementById("senha").value;
  var confirmar = document.getElementById("confirmar_senha").value;

  if (senha !== confirmar) {
    alert("As senhas não coincidem!");
    return false;
  }
  return validarSenha();
}

function aplicarMascaraCPF() {
  var cpf = document.getElementById("cpf");
  cpf.value = cpf.value.replace(/\D/g, '')
    .replace(/(\d{3})(\d)/, '$1.$2')
    .replace(/(\d{3})(\d)/, '$1.$2')
    .replace(/(\d{3})(\d{1,2})$/, '$1-$2');
}

function aplicarMascaraTelefone() {
  var tel = document.getElementById("telefone");
  tel.value = tel.value.replace(/\D/g, '')
    .replace(/(\d{2})(\d)/, '($1) $2')
    .replace(/(\d{5})(\d)/, '$1-$2');
}

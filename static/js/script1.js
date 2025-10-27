function verificarDigitacao(event) {
    const fieldValue = event.target.value;
    if (fieldValue.length > 20) {
        alert("Texto muito longo!");
    }
}

function validarSenha() {
    var senha = document.getElementById("senha").value;

    // Verificar o tamanho mínimo da senha
    if (senha.length < 6) {
        alert("A senha deve ter pelo menos 6 caracteres");
        return false;
    }

    // Verificar se a senha contém pelo menos maiúsula e números
    var uppercaseRegex = /[A-Z]/; //Regex é como uma máscara
    var numeroRegex = /[0-9]/;
    var especialRegex = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/;

    // Verificar todas as condições
    if (!uppercaseRegex.test(senha) || !numeroRegex.test(senha) || !especialRegex.test(senha)) {
        alert("A senha deve conter pelo menos uma letra maiúscula, um número e um caractere especial");
        return false; // não passou na validação, retorna false 
    }
    return true; // o formulário será enviado para a rota /autenticar
}

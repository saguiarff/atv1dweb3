<h2>Atividade 1 - Aplicação Flask | Disciplina: Desenvolvimento Web III</h2>
Foi criado o script <code>AppFlask.py</code> em um ambiente virtual com Flask instalado<br><br>
<li>Commit 1:</li>
<h3>01 - inicia o app Flask, e uma unica rota (‘/’) que retorna 'Olá!'</h3>
<ol>
  <li>É importada a classe <code>Flask</code> da biblioteca flask;</li>
  <li>Em seguida, é criada uma aplicação chamada <code>app_Sofia</code>;</li>
  O argumento <code>__name__</code> ajuda o Flask a localizar arquivos de aplicação, imagens e templates.
  <li>Depois, é adicionada uma rota na aplicação <code>app_Sofia</code> com uma função que retorna <code>'Olá!'</code>;</li>
  As rotas mapeiam URLs para essas funções, tipicamente definidas usando o decorador <code>@app.route</code>, no caso do código é <code>@app_Sofia.route</code>.
  <li>No final, inicia-se o servidor Flask localmente com <code>app_Sofia.run()</code>.</li>
</ol>
<br> 
<li>Commit 2:</li>
<h3>02 - criação de uma função de saudação, sem rota definida</h3>
<ol>
  <li>Foi criado a rota <code>/ola</code> que retona 'Olá!';</li>
  <li>Depois foi adicionada uma nova função dinâmica chamada <code>saudacoes</code>, sem rota, com argumentos contidos no novo script <code>appImport.py, o qual importa a função;</code></li>
  <li>O servidor Flask foi atualizado para iniciar na porta 8000, mas apenas se o arquivo estiver sendo executado diretamente no <code>AppFlask.py</code>, pois evita que o servidor rode automaticamente ao importar este arquivo de outro script.</li>
</ol>
<li>Commit 3:</li>
<h3>03 - Cria objeto da aplicação Flask, adiciona rota <code>/rota1</code> com a função principal e <code>/rota2</code> com resposta em HTML</h3>
Obs.: Eu sei que o objeto da aplicação Flask foi criado no <b>Commit 1</b>, acho que por isso estar destacado esse fato em um comentário no código original eu acabei me confundindo, estava cansada, realmente foi erro meu, não foi chatgpteses.
<ol>
  <br>
  <li>A rota <code>/ola</code> foi substituída pela <code>/rota1</code>;</li>
  <li>Têm a adição de uma nova rota chamada <code>/rota2</code> com uma função com uma variável <code>resposta</code> que contém uma string HTML, e ela retorna a mesma.</li>
</ol>

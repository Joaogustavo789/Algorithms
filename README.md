
# Algorithms

Algorithms é um projeto que aborda sobre algoritmos e suas complexidades, com o objetivo de resolver situações que não possui uma otimização de tempo. 
Foi desenvolvido utilizando a linguagem de programação `Python`.

## Rodando localmente

<details>
    <summary>Clique aqui para expandir</summary>
    <br>

- Clone o projeto

```bash
  git clone git@github.com:Joaogustavo789/Algorithms.git
```

- Entre no diretório do projeto

```bash
  cd Algorithms
```

- Crie o Ambiente Virtual

```bash
  python3 -m venv .venv
```
    
- Ative o Ambiente Virtual
    
```bash
  source .venv/bin/activate
```

- Instale as dependências dentro do Ambiente Virtual

```bash
  python3 -m pip install -r dev-requirements.txt
```

##### OBSERVAÇÃO

- Para sair do Ambiente Virtual, basta rodar o comando `deactivate`.
    
</details>

## Rodando os testes

<details>
  <summary>Clique aqui para expandir</summary>
  <br>

- Para rodar os testes, rode o seguinte comando dentro do Ambiente Virtual

```bash
  python3 -m pytest
```

</details>

## Stack utilizada

<table width="320px" align="center">
  <tbody>
    <tr valign="top">
      <td width="80px" align="center">
        <span><strong>Python</strong></span>
        <img height="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" />
      </td>
      <td width="80px" align="center">
        <span><strong>Pytest</strong></span>
        <img height="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytest/pytest-original.svg" />
      </td>
    </tr>
  </tbody>
</table>

## Funcionalidades

- Busca Linear (Algoritmo de busca)
- Merge Sort (Algoritmo de ordenação)
- Iteratividade
- Recursividade
- Teste

## Aprendizados

Nesse projeto, aprendi o que são algoritmos, suas complexidades, que possuem algumas noções como: `O(1)`, `O(n)`, `O(log n)`, `O(n^2)`, `O(n^3)` e 
`O(n!)`, definir `melhor caso`, `caso médio`, `pior caso` de uma Ordem de Complexidade. Aprendi a encontrar a quantidade de estudantes que estavam 
estudando em um horário específico utilizando a `busca linear`, na qual irá percorrer item por item, aprendi a identificar palíndromos utilizando dois 
algoritmos, o primeiro foi usando a `recursividade`, na qual tem um caso baso, um caso de decremento, e o segundo foi usando a `iteratividade`, na qual 
possui um laço de repetição, aprendi a identificar anagramas utilizando o `merge sort`, algoritmo de ordenação que possui como estrategia dividir e 
conquistar, aprendi a encontrar numéros repetidos em uma lista também utilizando a busca linear, porém foi necessário ordenar essa lista para depois 
percorrer item por item e por fim, implementei um teste de uma função que encripta uma mensagem, na qual eu testo se ao chama-la com os devidos 
parametros ela retorna a resposta esperada.

## Documentação

- [Python](https://www.python.org/)
- [Pytest](https://docs.pytest.org/)

## Feedback

Se você tiver algum feedback, por favor nos deixe saber por meio de jgustavomendonca@gmail.com

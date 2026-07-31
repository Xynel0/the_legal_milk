# Aula 1 - Conjuntos Numéricos (revisão)

> Uma revisão dos conjuntos numéricos comumente vistos no ensino médio e uma breve apresentação de conceitos a serem explorados mais à frente

## Naturais ($\mathbb{N}$)

<p>
  O Conjunto dos Naturais (representado por $\mathbb{N}$) é composto por números que servem para contagem ou ordenação.
  <br>
  <br>
  Veja o exemplo do número $3$: este símbolo "3" é o símbolo usado no sistema hindu-arábico para representar a <strong>quantidade três</strong>, ou seja, a quantidade de elementos de qualquer conjunto que possa ser colocado em correspondencia de um-para-um com o conjunto $\{x, y, z\}$ ou com o conjunto $\{!, @, \#\}$ (ou qualquer conjunto com esta mesma <strong>quantidade</strong> de elementos).
  <br>
  <br>
  Perceba que o <strong>número</strong> três é o conceito abstrato da quantidade três, enquanto o <strong>algarismo</strong> 3 é apenas um símbolo usado para representar o <strong>numeral</strong> 3, que por sua vez é a representação escrita do número $3$
  <br>
  Ou seja:
  <br>
  <ul>
    <li>
      <strong>Número:</strong> Ideia de quantidade (ex.: o número quarenta e dois)
    </li>
    <li>
      <strong>Algarismo:</strong> Cada símbolo básico usado para construir a escrita do número (ex.: os algarismos $4$ e $2$ ou os algarismos $X$, $L$ e $I$)
    </li>
    <li>
      <strong>Numeral:</strong> A representação escrita do número (ex.: o numeral $42$, ou o numeral $XLII$)
    </li>
  </ul>
  <br>
  É importante mencionar que nem sempre a humanidade dispôs de palavras ou símbolos para representar quantidades. Há relatos de que muito tempo atrás os humanos recorriam a sacos com pedras para representar quantidades. Por exemplo, a quantidade de galinhas na imagem abaixo seria representada pelo saco de pedras ao lado, em que cada pedra correspondia a uma única galinha e cada galinha correspondia a uma única pedra. Daí surge a palavra <strong>Calcular</strong>, que significa "fazer conta com pedras". Assim, pode-se dizer que o uso de sacos com pedras foi o primeiro sistema (rudimentar) de numeração.
  <br>
</p>

<div align="center">
  <img src="./calculo1_assets/galinhas_e_saco_de_pedras.png" alt="Galinhas ao lado de um saco de pedras, ilustrando um sistema rudimentar de contagem">
</div>

<p>
  <br>
  Um grande progresso foi o uso de palavras para representar quantidades e, posteriormente, o advento de símbolos para representá-las. Houveram diversos sistemas de numeração que associavam símbolos a quantidades, sendo o sistema de numeração romano um dos mais conhecidos. Atualmente, porém, o sistema mais amplamente difundido e usado é o sistema hindu-arábico, que possui dez símbolos: 0, 1, 2, 3, 4, 5, 6, 7, 8 e 9. A partir de combinações desses símbolos podemos representar cada número natural.
</p>
<div class="definicoes" id="1">
  <h3 id="Números naturais">
    <strong>DEFINIÇÃO</strong>
  </h3>
  <p>
    O <strong>conjunto dos números naturais</strong> é o conjunto denotado por $\mathbb{N}$ e dado por
    <br>
  </p>
  <p class="p_centralizado" align="center">
    $$\mathbb{N}≔\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, \ldots \}$$
    <br>
  </p>
  <p>
    A notação $\mathbb{N}^*$ exclui o $0$, e refere-se aos <strong>naturais não nulos</strong>, ou seja:
  </p>
  <p class="p_centralizado" align="center">
    $$\mathbb{N}^*≔\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, \ldots \}$$
    <br>
  </p>
</div>

---

#### **Observação:**
O símbolo " $≔$ " signigica que a igualdade ali representada é uma **definição**, isto é, uma descrição daquilo. É como está definido e, portanto, não necessita de prova.

---

As quatro operações fundamentais, adição($+$), subtração($-$), multiplicação ($\cdot$) e divisão($\div$), uma vez que são operações abstratas, não dependem do sistema numérico para serem executadas. Mesmo no caso do saco com pedras, ainda é possível realizá-las, dentro do princípio de que somar é juntar, subtrair é retirar, multiplicar é juntar partes iguais e dividir é separar em partes iguais. Vejamos agora, parte destas operações e suas propriedades.

As operações de adição e multiplicação (em $\mathbb{N}$) satisfazem as seguintes propriedades:

| Propriedade | O que diz | Significado |
|-------------|-------------|-------------|
| **Fechamento** | $$a+b, a\cdot b \in \mathbb{N}, \forall a, b \in \mathbb{N}$$ | Os números $a + b$ e $a \cdot b$ pertencem aos naturais, quaisquer que sejam $a$ e $b$ naturais |
| **Associatividade** | $$(a+b)+c = a+(b+c)$$ e $$(a\cdot b)\cdot c = a\cdot (b\cdot c), \forall a, b, c \in \mathbb{N}$$ | $$(a+b)+c = a+(b+c)$$ e $$(a\cdot b)\cdot c = a\cdot (b\cdot c)$$, quaisquer que sejam $a$, $b$ e $c$ naturais |
| **Comutatividade** | $$a + b = b + a$$ e $$a\cdot b = b\cdot a, \forall a, b \in \mathbb{N}$$ | $$a + b = b + a$$ e $$a\cdot b = b\cdot a$$, quaisquer que sejam $a$ e $b$ naturais |
| Existência do **elemento neutro** | $$a+0 = a$$ e $$a\cdot 1 = a, \forall a \in \mathbb{N}$$ | $$a+0 = a$$ e $$a\cdot 1 = a$$, para todo $a$ natural |
| **Distributividade** da multiplicação em relação à adição | $a \cdot (b+c) = a \cdot b + b \cdot c, \forall a, b, c \in \mathbb{N}$ | $a \cdot (b+c) = a \cdot b + b \cdot c$, para quaisquer $a$, $b$ e $c$ naturais |
| **Integridade** da adição | $a, b \in \mathbb{N} \land a + b = 0 \implies a = 0 \land b = 0$ | se $a, b \in \mathbb{N}$ e $a + b = 0,$ então $a = 0$ e $b = 0$ |
> Nota: Para rever os significados dos sinais acima, e outros, [clique aqui](../arquivos_uteis_s1/simbolos_matematicos_e_logicos.md)

#### Em outras palavras...
<ul>
  <li><strong>Fechamento:</strong><br> A soma de dois naturais resulta num natural, assim como o produto de dois naturais resulta num natural</li>
  <li><strong>Associatividade:</strong><br> A ordem em que são feitas varias somas não altera o resultado, assim como a ordem em que são feitas varias multiplicações não altera o resultado (não confundir com a ordem entre operações diferentes. Multiplicação segue tendo prioridade sobre a soma).</li>
  <li><strong>Comutatividade:</strong><br> A ordem das parcelas não altera a soma, assim como a ordem dos fatores não altera o produto.</li>
  <li><strong>Elemento neutro:</strong><br> Somar 0 não altera nada, assim como multiplicar por 1 também não altera nada.</li>
  <li><strong>Distributividade:</strong><br> O produto de um número por uma soma pode ser escrito como a soma de cada parcela multiplicada individualmente pelo número (o famoso "chuveirinho"). </li>
  <li><strong>Integridade:</strong><br> Se uma soma de naturais dá 0, ambos são 0. Por outro lado, se o produto de dois naturais resulta em 0, OU um deles é 0, OU o outro é 0.</li>
</ul>

---

#### **Observação:**
A soma e o produto de $n$ números naturais ($a_1, a_2, \ldots , a_n$) pode ser simplesmente expressa como
<p class="p_centralizado" align="center">
  $$a_1 + a_2 + \cdots + a_n $$ e $$a_1 \cdot a_2 \cdot \ldots \cdot a_n$$,
  <br>
</p>

sendo desnecessário usar parênteses já que, pelas propriedades da associatividade e da comutatividade, não faz diferença por onde se começa a execução das operações (não confundir com a ordem entre operações diferentes. Multiplicação segue tendo prioridade sobre a soma).

---

Uma equação pode ser entendida como um tipo de pergunta. Por exemplo, a expressão

<p class="p_centralizado" align="center">
  $$2x +4 = 10$$,
</p>

no universo dos números naturais, pode ser entendida como a pergunta: "Qual o número natural cujo dobro mais quatro é igual a 10?"

Uma ***solução*** desta equação é qualquer resposta correta para esta pergunta, ou seja, qualquer número natural cujo dobro mais quatro é igual a 10. Analisando brevemente a equação, é possivel perceber que $3$ é uma solução (neste caso, a única solução) para esta pergunta.

O ***conjunto solução*** de uma equação é formado por **cada resposta**, dentro do universo de interesse, para a pergunta em questão. No caso da equação acima, o seu conjunto solução em $\mathbb{N}$, é o conjunto $\mathit{S}$ dado por

<p class="p_centralizado" align="center">
  $$\mathit{S} = \{3\}$$.
</p>

Vejamos outro caso:
No universo dos naturais, a equação $x + 3 = 5$ possui solução. Sabemos que seu conjunto solução $\mathit{S}$ é unitário e dado por $\mathit{S} = \{2\}$. Já a equação $x + 5 = 2$  não possui solução nesse universo (pois não existe nenhum número natural que, somado a 5, resulte em 2). Nesse caso, seu conjunto solução $\mathit{S}$ é vazio, sendo representado por


<p class="p_centralizado" align="center">
  $$\mathit{S} = \varnothing$$.
</p>

> Nota: abordaremos teoria dos conjuntos em [uma aula mais à frente]() <!-- ADICIONAR LINK PARA A AULA DE CONJUNTOS -->

---
---

## Inteiros ($\mathbb{Z}$)

Para, por exemplo, dar uma solução à equação $x + 5 = 2$, contar grandezas em caráter relativo, entre outros motivos, foram criados os números inteiros (representados por $\mathbb{Z}$)

<div class="definicoes" id="2">
  <h3 id="Números inteiros">
    <strong>DEFINIÇÃO</strong>
  </h3>
  <p>O <strong>conjunto dos números inteiros</strong> é denotado por $\mathbb{Z}$ e dado por</p>
  <p class="p_centralizado" align="center">
    $$\mathbb{Z}≔\{\ldots , -4, -3, -2, -1, 0, +1, +2, +3, +4, \ldots \}$$
    <br>
  </p>
  <p>
    A notação $\mathbb{Z}^*$ exclui o $0$, e refere-se aos <strong>inteiros não nulos</strong>, ou seja:
  </p>
  <p class="p_centralizado" align="center">
    $$\mathbb{Z}^*≔\{\ldots , -4, -3, -2, -1, +1, +2, +3, +4, \ldots \}$$
    <br>
  </p>
</div>

---

 observação: uma vez que $+1=1, +2=2, \ldots$, cada natural é também um inteiro

---

Vejamos agora, algumas definições aplicaveis a elementos destes conjuntos

<div class="definicoes" id="3">
  <h3 id="Número par">
    <strong>DEFINIÇÃO</strong>
  </h3>
  <p>
    Seja $n \in \mathbb{Z}$. Dizemos que <strong>$n$ é par</strong> quando existe algum número inteiro $k$ tal que $n=2k$. Ou seja, $n$ é par se houver algum inteiro que, multiplicado por $2$, resulte em $n$.
  </p>
</div>

Assim, já que $2=2\cdot 1$, $6=2\cdot 3$, $-1010 = 2\cdot (-505)$ e $0=2\cdot 0$, os números $2$, $6$, $-1010$ e $0$ são pares.

<p>Veja que cada inteiro no conjunto $\{0, -2, +2, -4, +4, -6, +6, \ldots\}$ é par.</p>

<div class="definicoes" id="4">
  <h3 id="Número ímpar">
    <strong>DEFINIÇÃO</strong>
  </h3>
  <p>
    Seja $n \in \mathbb{Z}$. Dizemos que <strong>$n$ é ímpar</strong> quando existe algum número inteiro $k$ tal que $n=2k+1$. Ou seja, $n$ é ímpar se houver algum inteiro que, multiplicado por $2$, resulte em um número que, somado a $1$, resulte em $n$.
  </p>
</div>

Assim, já que $3=2\cdot 1 + 1$, $7=2\cdot 3 + 1$, $-1009 = 2\cdot (-505) +1$ e $1=2\cdot 0 + 1$, os números $3$, $7$, $-1009$ e $1$ são pares.

<p>Veja que cada inteiro no conjunto $\{-1, 1, -3, +3, -5, +5, -7, +7, \ldots\}$ é par.</p>

Analisando brevemente o conjunto dos pares e dos ímpares, é possível perceber que **cada número inteiro ou é par, ou é ímpar**.


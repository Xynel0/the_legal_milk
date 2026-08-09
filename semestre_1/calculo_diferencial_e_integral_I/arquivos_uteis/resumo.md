<div class="definicoes" id="1">
<h3 id="Números naturais">
<strong>Números Naturais</strong>
</h3>
<p>
    O <strong>conjunto dos números naturais</strong> é o conjunto denotado por $\mathbb{N}$ e dado por
    <br/>
</p>
<p align="center" class="p_centralizado">
    $$\mathbb{N}≔\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, \ldots \}$$
    <br/>
</p>
<p>
    A notação $\mathbb{N}^*$ exclui o $0$, e refere-se aos <strong>naturais não nulos</strong>, ou seja:
  </p>
<p align="center" class="p_centralizado">
    $$\mathbb{N}^*≔\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, \ldots \}$$
    <br/>
</p>
</div>

---

<div class="definicoes" id="2">
<h3 id="Números inteiros">
<strong>Números Inteiros</strong>
</h3>
<p>O <strong>conjunto dos números inteiros</strong> é denotado por $\mathbb{Z}$ e dado por</p>
<p align="center" class="p_centralizado">
    $$\mathbb{Z}≔\{\ldots , -4, -3, -2, -1, 0, +1, +2, +3, +4, \ldots \}$$
    <br/>
</p>
<p>
    A notação $\mathbb{Z}^*$ exclui o $0$, e refere-se aos <strong>inteiros não nulos</strong>, ou seja:
  </p>
<p align="center" class="p_centralizado">
    $$\mathbb{Z}^*≔\{\ldots , -4, -3, -2, -1, +1, +2, +3, +4, \ldots \}$$
    <br/>
</p>
</div>

---

<div class="definicoes" id="3">
<h3 id="Número par">
<strong>Número Par</strong>
</h3>
<p>
    Seja $n \in \mathbb{Z}$. Dizemos que <strong>$n$ é par</strong> quando existe algum número inteiro $k$ tal que $n=2k$. Ou seja, $n$ é par se houver algum inteiro que, multiplicado por $2$, resulte em $n$.
  </p>
</div>

---

<div class="definicoes" id="4">
<h3 id="Número ímpar">
<strong>Número Ímpar</strong>
</h3>
<p>
    Seja $n \in \mathbb{Z}$. Dizemos que <strong>$n$ é ímpar</strong> quando existe algum número inteiro $k$ tal que $n=2k+1$. Ou seja, $n$ é ímpar se houver algum inteiro que, multiplicado por $2$, resulte em um número que, somado a $1$, resulte em $n$.
  </p>
</div>

---

<div class="definicoes" id="5">
<h3 id="Multiplicidade">
<strong>Multiplicidade</strong>
</h3>
<p>
    Sejam $m, n \in \mathbb{Z}$. Dizemos que $n$ é <strong>múltiplo</strong> de $m$ quando existe algum inteiro $k$ tal que $n = k \cdot m$. Ou seja, $n$ é múltiplo de $m$ se houver algum inteiro que, multiplicado por $m$ resulte em $n$. Vale lembrar que este inteiro $k$ também pode ser $0$ e, portanto, $0$ é múltiplo de qualquer número inteiro, já que $0 = 0 \cdot m, \forall m \in \mathbb{Z}$.
  </p>
</div>

---

<div class="definicoes" id="6">
<h3 id="Divisibilidade">
<strong>Divisibilidade</strong>
</h3>
<p>Sejam $n \in \mathbb{Z}, m \in \mathbb{Z}^*$. Dizemos que <strong>$m$ divide $n$</strong> (ou que $n$ é divisível por $m$, ou ainda, que $m$ é um fator de $n$) quando $\exists k \in \mathbb{Z}$ tal que $n = k \cdot m$. Ou seja, $m$ divide $n$ se é possível encontrar algum inteiro $k$ que, multiplicado por $m$, resulte em $n$.
  </p>
</div>

---

<div class="definicoes" id="7">
<h3 id="Máximo divisor comum (M.D.C.)">
<strong>Máximo Divisor Comum (M.D.C.)</strong>
</h3>
<p>Sejam $a, b \in \mathbb{Z}$, com $a \neq 0$ OU $b \neq 0$. O <strong>Máximo Divisor Comum</strong> de $a$ e $b$ é o maior inteiro positivo que divide $a$ e que divide $b$, sendo denotado por $\mathrm{MDC}(a,b)$. Como o nome bem sugere, o MDC de dois números é o maior inteiro que é divisor comum, que consegue dividir esses dois números ao mesmo tempo.</p>
</div>

---

<div class="definicoes" id="8">
<h3 id="Primos entre si"><strong>Primos Entre Si</strong></h3>
<p>Dizemos que $a$ e $b$ são <strong>primos entre si</strong> quando $\mathrm{MDC}(a, b) = 1$.</p>
</div>

---

<div class="definicoes" id="9">
<h3 id="Números Primos">
<strong>Números Primos</strong>
</h3>
<p>
    Seja $p \in \mathbb{Z}$. Dizemos que $p$ é <strong>primo</strong> quando
  </p>
<ul align="center" class="ul_centralizado">
<li>$p \neq 0$,</li>
<li>$p \neq 1$,</li>
<li>$p \neq -1$ e</li>
<li>$p$ possui somente divisores triviais $(1, -1, p, -p)$.</li>
</ul>
</div>

---

<div class="definicoes" id="10">
<h3 id="Números Compostos">
<strong>Números Compostos</strong>
</h3>
<p> dado $p \in \mathbb{Z}$, dizemos que $p$ é <strong>composto</strong> quando</p>
<ul align="center" class="ul_centralizado">
<li>$p \neq 0$,</li>
<li>$p \neq 1$,</li>
<li>$p \neq -1$ e</li>
<li>$p$ possui ao menos um divisor não trivial, ou seja, não é primo.</li>
</ul>
</div>

---

<div class="proposicoes" id="1">
<h3>
<strong>Proposição</strong>
</h3>
<p>Seja $n \in \mathbb{Z}$. Se $n$ é par então $n^2$ é par.</p>
<a href="#Seja n inteiro. Se n é par, n ao quadrado é par">ver prova</a>
</div>

---

<div class="proposicoes" id="2">
<h3>
<strong>Corolário</strong>
</h3>
<p>Seja $n \in \mathbb{Z}$. Se $n^2$ é ímpar, então $n$ é ímpar.</p>
</div>

---

<div class="proposicoes" id="3">
<h3>
<strong>Proposição</strong>
</h3>
<p>Seja $n \in \mathbb{Z}$. Se $n$ é ímpar então $n^2$ é ímpar.</p>
<a href="#Seja n inteiro. Se n é ímpar, n ao quadrado é ímpar">ver prova</a>
</div>

---

<div class="proposicoes" id="4">
<h3>
<strong>Corolário</strong>
</h3>
<p>Seja $n \in \mathbb{Z}$. Se $n^2$ é par, então $n$ é par.</p>
</div>

---

<div class="provas" id="1">
<h3 id="Seja n inteiro. Se n é par, n ao quadrado é par">
<strong>Seja N Inteiro. Se N É Par, N Ao Quadrado É Par</strong>
</h3>
<p>Demonstração: Se $n$ é par, então, <a href="#Número par">por definição</a>, existe $k \in \mathbb{Z}$ tal que $n = 2k$. Assim, $n^2 = (2k)^2 = 4k^2 = 2 \cdot (2k^2)$. Sendo $k_1 = 2k^2$, tem-se $n^2 = 2k_1 \in \mathbb{Z}$. Portanto, $n^2$ também é par.</p>
</div>

---

<div class="provas" id="2">
<h3 id="Seja n inteiro. Se n é ímpar, n ao quadrado é ímpar">
<strong>Seja N Inteiro. Se N É Ímpar, N Ao Quadrado É Ímpar</strong>
</h3>
<p>Demonstração: Se $n$ é ímpar, então, <a href="#Número ímpar">por definição</a>, existe $k \in \mathbb{Z}$ tal que $n = 2k + 1$. Assim, $n^2 = (2k + 1)^2 = 4k^2 + 4k + 1 = 2 \cdot (2k^2 + 2k) + 1$. Sendo $k_1 = 2k^2 + 2k$, tem-se $n^2 = 2k_1 + 1 \in \mathbb{Z}$. Portanto, $n^2$ também é ímpar.</p>
</div>

---


# Capítulo 3

<div class="definicoes" id="algebra-booleana">
  <h3 id="Álgebra booleana">Álgebra booleana</h3>

A **Álgebra Booleana** é uma ramificação da matemática lógica utilizada para analisar e simplificar circuitos digitais, operando exclusivamente com valores binários: falso ($0$) ou verdadeiro ($1$).

*   **Operação NOT (Negação lógica):** A saída é o inverso da entrada.
    *   *Representação:* $\overline A$ ou $f(a) = 1 - a$.
*   **Operação OR (Disjunção lógica):** A saída é verdadeira se pelo menos uma das variáveis de entrada for verdadeira.
    *   *Representação:* $A + B$ (Álgebra Booleana) ou $f(a,b) = a + b - ab$ (Álgebra tradicional).
    *   **Operação NOR:** É a negação da operação OR, dada por $\overline {A + B}$ ou $f(a,b) = (1 - a)(1 - b)$.
*   **Operação AND (Conjunção lógica):** A saída é verdadeira se, e somente se, todas as variáveis de entrada forem verdadeiras.
    *   *Representação:* $A \cdot B$ ou $f(a,b) = a \cdot b$.
    *   **Operação NAND:** É a negação da operação AND, dada por $\overline {A \cdot B}$ ou $f(a,b) = 1 - ab$.
*   **Operação XOR (OU Exclusivo):** 
    *   Para duas entradas, a saída é verdadeira se as variáveis forem diferentes.
    *   Para três ou mais entradas, a saída é verdadeira se a quantidade de entradas verdadeiras for ímpar (*Paridade Ímpar*).
    *   *Representação:* $A \oplus B \oplus C$, $f(a,b) = a + b - 2ab$ ou $(A \cdot \overline B) + (\overline A \cdot B)$.
*   **Operação XNOR (NÃO OU Exclusivo):**
    *   Para duas entradas, a saída é verdadeira se ambas forem iguais.
    *   Para três ou mais entradas, a saída é verdadeira se a quantidade de entradas verdadeiras for par (*Paridade Par*).
    *   *Representação:* $A \odot B \odot C$, $f(a,b) = 2ab - a - b + 1$ ou $(A \cdot B) + (\overline A \cdot \overline B)$.
</div>

> ⚠️ **Nota:** Nas funções numéricas ( $f(a)$ e $f(a, b)$ ), o domínio é estritamente o conjunto binário $\{0, 1\}$. Essas funções são apresentadas como recurso complementar de fundamentação matemática.

---

<div id="tabelas-verdade">
  <h3 style="color: #2b6cb0; margin-top: 0;">Tabelas-Verdade</h3>

As **tabelas-verdade** são representações estruturadas em matrizes que permitem visualizar todos os resultados possíveis de uma operação lógica a partir de cada combinação de suas variáveis de entrada.
</div>

## NOT
| $A$ | NOT ($\overline{A}$) |
|:---:|:-------------------:|
|  0  |          1          |
|  1  |          0          |

## OR & NOR
| $A$ | $B$ | OR ($A+B$) | NOR ($\overline{A+B}$) |
|:---:|:---:|:----------:|:---------------------:|
|  0  |  0  |     0      |           1           |
|  0  |  1  |     1      |           0           |
|  1  |  0  |     1      |           0           |
|  1  |  1  |     1      |           0           |

## AND & NAND
| $A$ | $B$ | AND ($A \cdot B$) | NAND ($\overline{A \cdot B}$) |
|:---:|:---:|:-----------------:|:----------------------------:|
|  0  |  0  |         0         |              1               |
|  0  |  1  |         0         |              1               |
|  1  |  0  |         0         |              1               |
|  1  |  1  |         1         |              0               |

## XOR & XNOR
| $A$ | $B$ | XOR ($A \oplus B$) | XNOR ($A \odot B$) |
|:---:|:---:|:-----------------:|:------------------:|
|  0  |  0  |         0         |         1          |
|  0  |  1  |         1         |         0          |
|  1  |  0  |         1         |         0          |
|  1  |  1  |         0         |         1          |

---

<div id="teoremas-demorgan" style="border-left: 4px solid #2b6cb0; padding-left: 15px; margin-bottom: 25px;">
  <h3 style="color: #2b6cb0; margin-top: 0;">Teoremas de DeMorgan</h3>

Estas leis estabelecem relações equivalência entre as negações de conjunções e disjunções:

*   **Primeiro Teorema:** A negação da disjunção é igual à conjunção das negações.
    $$\overline{A+B} = \overline{A} \cdot \overline{B}$$
*   **Segundo Teorema:** A negação da conjunção é igual à disjunção das negações.
    $$\overline{A \cdot B} = \overline{A} + \overline{B}$$
</div>

---

<div id="teoremas-booleanos" style="border-left: 4px solid #2b6cb0; padding-left: 15px; margin-bottom: 25px;">
  <h3 style="color: #2b6cb0; margin-top: 0;">Teoremas Booleanos</h3>

Conjunto de identidades algébricas fundamentais utilizadas para a simplificação e otimização de circuitos lógicos.

### Teoremas de Uma Variável

| Operação AND | Operação OR |
|:---|:---|
| 1. $X \cdot 0 = 0$ | 1. $X + 0 = X$ |
| 2. $X \cdot 1 = X$ | 2. $X + 1 = 1$ |
| 3. $X \cdot X = X$ | 3. $X + X = X$ |
| 4. $X \cdot \overline{X} = 0$ | 4. $X + \overline{X} = 1$ |

Aqui está a seção dos **Teoremas Booleanos** atualizada, com os teoremas de múltiplas variáveis também organizados em formato de tabela para manter a consistência visual:

---

<div id="teoremas-booleanos" style="border-left: 4px solid #2b6cb0; padding-left: 15px; margin-bottom: 25px;">
  <h3 style="color: #2b6cb0; margin-top: 0;">Teoremas Booleanos</h3>

Conjunto de identidades algébricas fundamentais utilizadas para a simplificação e otimização de circuitos lógicos digitais.

### Teoremas de Uma Variável

| Operação AND | Operação OR |
|:---|:---|
| 1. $X \cdot 0 = 0$ | 1. $X + 0 = X$ |
| 2. $X \cdot 1 = X$ | 2. $X + 1 = 1$ |
| 3. $X \cdot X = X$ | 3. $X + X = X$ |
| 4. $X \cdot \overline{X} = 0$ | 4. $X + \overline{X} = 1$ |

<br>

### Teoremas de Múltiplas Variáveis

| Identificador | Expressão Matemática | Propriedade |
| :---: | :--- | :--- |
| **1** | $X + Y = Y + X$ | Comutativa |
| **2** | $X \cdot Y = Y \cdot X$ | Comutativa |
| **3** | $X + (Y + Z) = (X + Y) + Z = X + Y + Z$ | Associativa |
| **4** | $X(YZ) = (XY)Z = XYZ$ | Associativa |
| **5** | $X(Y + Z) = XY + XZ$ | Distributiva |
| **6** | $(W + X)(Y + Z) = WY + WZ + XY + XZ$ | Distributiva Expandida |
| **7** | $X + XY = X$ | Absorção |
| **8** | $X + \overline{X}Y = X + Y$ | Simplificação / Absorção |
| **9** | $\overline{X} + XY = \overline{X} + Y$ | Simplificação / Absorção |

</div>

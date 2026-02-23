# 📊 IAFX Prime v7 - Guia Completo do Usuário

## 🎯 O Que é o IAFX Prime v7?

O **IAFX Prime v7** é um Expert Advisor (robô de negociação) inteligente para MetaTrader 5 que opera com estratégias deGrid (grade) combinadas com sistemas avançados de proteção de capital e gestão de risco.

---

## 🚀 Principais Funcionalidades

### ✅ Estratégias de Operação

O robô trabalha com **duas estratégias principais** que se adaptam conforme o mercado:

#### 🔷 **Grid Super (Agressivo) - Dinâmica VKGLinear**
- **Quando usa**: Quando já existe mais de 1 ordem aberta e o preço se afasta `grid_super_pontos` pontos
- **Como funciona**:
  - Ativação puramente por distância em pontos (não depende de indicadores)
  - Abre posições com volume multiplicado (mais agressivo)
  - Fecha a posição mais antiga quando o conjunto fica lucrativo (dinâmica VKGLinear)
  - Mantém apenas as posições mais recentes
- **Parâmetro**: `grid_super_pontos` (padrão: 75 pontos)
- **Vantagem**: Aproveita tendências fortes rapidamente, sem filtros de indicadores
- **Cuidado**: Mais agressivo, requer atenção ao DD%

#### 🔶 **Grid Médio (Defensivo)**
- **Quando usa**: Quando o mercado está em reversão
- **Como funciona**:
  - Abre posições defensivas sem aumentar agressividade
  - Limite máximo de 15 ordens para proteger a conta
  - Espera o conjunto todo ficar lucrativo
- **Vantagem**: Mais seguro em mercados laterais
- **Limite**: Máximo de 15 ordens (configurável)

---

## 🛡️ Sistema de Defesa em 3 Camadas

O robô possui **3 alertas de defesa** que ativam automaticamente conforme o Drawdown (DD%) **ou o VIX** aumenta (quem chegar primeiro):

### 🟡 **Alerta A - Grid Adaptativo**
- **Ativado por**: DD% >= `alertaDDA` (padrão 10%) **OU** VIX >= `vix_alerta_a` (padrão 21.0)
- **O que acontece**: Grid aumenta 1.5x
- **Por quê**: Espaça mais as ordens para dar mais "respiro" ao mercado
- **Exemplo**: Se grid era 150 pontos, vira 225 pontos
- **Desativa quando**: DD% E VIX voltam abaixo dos thresholds (com histerese)

### 🟠 **Alerta B - Mudança de Timeframe**
- **Ativado por**: DD% >= `alertaDDB` (padrão 20%) **OU** VIX >= `vix_alerta_b` (padrão 24.0) **OU** VIX spike >= 30% em 1 dia
- **O que acontece**: Todos os indicadores mudam para timeframe de segurança
- **Por quê**: Timeframe maior = sinais mais confiáveis
- **Padrão**: Muda para M15 (15 minutos)
- **Desativa quando**: DD% E VIX voltam abaixo dos thresholds

### 🔴 **Alerta C - Modo Emergência (30% DD)**
- **O que acontece**: Grid Super entra em modo super conservador
- **Como funciona**:
  - Reduz multiplicador de lote pela metade
  - Mantém apenas 50% do multiplicador original
- **Objetivo**: Proteção máxima do capital em situação crítica

---

## 💰 Sistema Inteligente de Fechamento

### 🎯 **Alvos Dinâmicos (Novo!)**

Em vez de valores fixos em dólar, o robô agora trabalha com **percentual do seu saldo**:

- **Alvo Principal**: 0.5% do balance (padrão)
- **Alvo Parcial**: 0.25% do balance (padrão)
- **Vantagem**: Se adapta automaticamente ao crescimento da sua conta

#### 📍 **Fechamento em 2 Níveis**

**Nível 1 - Poucas Ordens (< 3 ordens)**
- Alvo: 0.5% do balance
- Fecha: Todas as ordens de uma vez

**Nível 2 - Muitas Ordens (≥ 3 ordens)**
- Primeiro: Fecha 50% das ordens quando atingir 0.25% (Fechamento Parcial)
- Depois: Fecha o restante quando atingir 0.5% (Alvo Final)

### 🌙 **Alvos por Horário (Novo!)**

O robô reduz os alvos durante horários de **baixa liquidez**:

- **Horário reduzido**: 22h às 6h (padrão)
- **Multiplicador**: 0.5x (metade do alvo)
- **Por quê**: Menos liquidez = menos ambição = mais segurança

---

## 📅 Sistema de Meta Diária - 3 Regras Inteligentes

### 🎯 **Regra 1: Meta Diária de 1%**
**Quando**: A qualquer momento do dia
**Condição**: Se o lucro total do dia atingir 1% do balance inicial
**Ação**:
- ✅ Fecha TODAS as posições
- 🔒 Bloqueia o robô até o próximo dia
- 💡 **Objetivo**: Garantir lucro consistente e evitar devolver ganhos

**Exemplo Prático**:
- Balance inicial do dia: R$ 10.000
- Meta: R$ 100 (1%)
- Às 14h você já ganhou R$ 100 → Robô fecha tudo e para até amanhã

---

### 🕐 **Regra 2: Proteção 17h-19h Brasília**
**Quando**: Entre 17h e 19h (horário de Brasília)
**Condição**: Se o lucro realizado do dia for maior que as perdas flutuantes
**Ação**:
- ✅ Fecha TODAS as posições
- 🔒 Garante dia positivo
- 💡 **Objetivo**: Proteger lucros já realizados contra reversões

**Exemplo Prático**:
- Lucro realizado no dia: R$ 150
- Posições abertas com perda flutuante: -R$ 80
- São 18h → Como R$ 150 > R$ 80, fecha tudo garantindo +R$ 70 no dia

---

### 📆 **Regra 3: Sexta-feira com 3% Semanal**
**Quando**: Sexta-feira, a partir das 12h
**Condição**: Se o lucro da semana (realizado + flutuante) for ≥ 3%
**Ação**:
- ✅ Fecha TODAS as posições (positivas e negativas)
- 🔒 Garante 3% da semana
- 📅 Só reabre domingo à noite
- 💡 **Objetivo**: Garantir semana lucrativa e descanso de fim de semana

**Exemplo Prático**:
- Balance: R$ 10.000
- Meta semanal: R$ 300 (3%)
- Sexta-feira 14h: Lucro da semana = R$ 320
- → Robô fecha tudo, garante os 3% e descansa até domingo

---

## ⏰ Horário de Operação

O robô possui uma **janela de bloqueio** configurada automaticamente:

- **Horário bloqueado**: 17:30 às 20:30 (horário de Brasília)
- **Motivo**: Período de fechamento dos mercados europeus — spreads elevados e volatilidade pontual
- **O que acontece**: Nenhuma nova ordem (primeira ou grid) é aberta neste período
- **Posições existentes**: Continuam abertas e gerenciadas normalmente

> O cálculo usa o parâmetro `offset_servidor_brasilia` para converter horário do servidor para Brasília.

---

## 🔐 Breakeven Cascata

### O que é?
Sistema que **move o Stop Loss de TODAS as posições juntas** quando o preço médio se torna lucrativo.

### Como funciona?
1. Calcula o preço médio de todas as posições abertas (BUY e SELL separadamente)
2. Quando o mercado se afasta `breakevan_pontos` pontos do preço médio (ficando positivo)
3. Move o SL de todas as ordens daquela direção para o breakeven (ponto de equilíbrio)
4. **Resultado**: Protege lucro em bloco

### Parâmetros:
- **`usar_breakevan`**: Ativa/desativa o sistema (padrão: true)
- **`breakevan_pontos`**: Distância em pontos para ativar o breakeven (padrão: 150)

### Características:
- ✅ Protege todo o conjunto de ordens
- ✅ Evita perder lucro já conquistado
- ✅ Funciona automaticamente
- ✅ Processa posições BUY e SELL separadamente (não bloqueia com posições mistas)
- ✅ Filtro por magic number (não interfere com outros EAs)
- ✅ Trata corretamente posições sem Stop Loss prévio

---

## ⚙️ Configurações e Inputs - Explicação Detalhada

### 📋 **Seção: Configurações Básicas**

#### `Chave de acesso - licença`
- **O que é**: Código de ativação do robô
- **Valor**: Fornecido pelo desenvolvedor
- **Importante**: Sem a chave correta, o robô não opera

#### `Modo de operação`
- **Opções**:
  - `1 - Automático`: Robô decide tudo sozinho
  - `2 - Manual-Semiautomático`: Você inicia, robô gerencia
- **Recomendado**: Automático para traders experientes

#### `Tipo de operação`
- **Opções**:
  - `0 - Compras e Vendas`: Opera nos dois sentidos
  - `1 - Somente Compras`: Apenas LONG
  - `2 - Somente Vendas`: Apenas SHORT
  - `3 - Swap +`: Opera apenas no lado com swap positivo da corretora
  - `4 - Carry Trade`: Opera no lado favorável pelo diferencial de taxas de juros
- **Swap+ vs Carry Trade**:
  - **Swap+** consulta os valores reais de swap da corretora (`SYMBOL_SWAP_LONG` / `SYMBOL_SWAP_SHORT`). É pragmático: reflete o custo real que você vai ter. Porém, se a corretora cobrar swap negativo nos dois lados, retorna "NONE" e opera sem filtro nenhum.
  - **Carry Trade** compara as taxas de juros dos bancos centrais informadas manualmente nos inputs. Representa a lógica macroeconômica pura. Requer atualização manual quando bancos centrais alteram taxas.
- **Dica**: Use "Swap+" para minimizar custos overnight com base na corretora, ou "Carry Trade" para seguir o diferencial de juros real entre países

#### `Modo TREND`
- **O que é**: Define o modo de análise de tendência usado pelo Grid Super para evitar abrir contra tendência
- **Opções**: 1=Alinhamento | 2=200 | 3=200+50 | 4=200+50+21
- **Padrão**: 2 (Média de 200 períodos)

---

### 💵 **Seção: Lotes e Grid**

#### `Tamanho do lote para ordens`
- **O que é**: Volume inicial das ordens
- **Padrão**: 0.01 (micro lote)
- **Ajuste**: Conforme tamanho da sua conta
- **Fórmula sugerida**: Balance ÷ 10.000 = lote base

#### `Valor acima de 1 multiplica lot nas agressões de tendência`
- **O que é**: Multiplicador para operações de tendência forte
- **Padrão**: 1.0 (sem multiplicar)
- **Exemplo**: 1.5 = aumenta 50% o lote em tendências
- **Cuidado**: Valores altos aumentam risco

#### `Grid em pontos`
- **O que é**: Distância entre cada ordem do Grid Médio em pontos
- **Padrão**: 150 pontos
- **Ajuste**:
  - Menor = Mais ordens (mais agressivo)
  - Maior = Menos ordens (mais conservador)

#### `Distância em pontos para Grid Super (agressão)`
- **O que é**: Distância em pontos para ativar o Grid Super (dinâmica VKGLinear)
- **Padrão**: 75 pontos
- **Importante**: Não depende de indicadores, apenas de distância
- **Ajuste**: Valor menor = mais agressivo, valor maior = mais conservador

#### `Limite máximo de ordens Grid Médio`
- **O que é**: Máximo de ordens na estratégia defensiva
- **Padrão**: 15 ordens
- **Objetivo**: Evitar overtrading e proteger capital

---

### 🎯 **Seção: Alvos e Fechamentos**

#### `Alvo de PL para fechar ordens (em moeda)`
- **O que é**: Antigo sistema de alvo fixo
- **Padrão**: $0.54
- **Status**: Substituído pelo sistema percentual

#### `Qtd de ordens para nivel 2`
- **O que é**: A partir de quantas ordens muda o alvo
- **Padrão**: 3 ordens
- **Explicação**:
  - Menos de 3 ordens = usa alvo maior
  - 3 ou mais ordens = usa alvo menor (mais fácil de atingir)

#### `Alvo de PL para fechar ordens nivel2 (em moeda)`
- **O que é**: Alvo quando tem muitas ordens
- **Padrão**: $0.10
- **Objetivo**: Facilitar fechamento com muitas posições

---

### 📊 **Seção: Alvos Percentuais (NOVO!)**

#### `Usar alvo em % do balance`
- **O que é**: Ativa sistema de alvo dinâmico
- **Padrão**: true (ativado)
- **Vantagem**: Se adapta ao crescimento da conta

#### `Alvo em % do balance`
- **O que é**: Percentual do saldo para fechar tudo
- **Padrão**: 0.5% (meio porcento)
- **Exemplo**: Conta de R$ 10.000 → alvo de R$ 50

#### `Ativar fechamento parcial`
- **O que é**: Fecha metade das ordens antes do alvo final
- **Padrão**: true (ativado)
- **Vantagem**: Realiza lucro gradualmente

#### `% de ordens a fechar no parcial`
- **O que é**: Quantas ordens fechar no fechamento parcial
- **Padrão**: 50% (metade)
- **Exemplo**: 10 ordens abertas → fecha 5 no parcial

#### `% do balance para fechamento parcial`
- **O que é**: Quando ativa o fechamento parcial
- **Padrão**: 0.25% (metade do alvo final)
- **Sequência**:
  1. Atinge 0.25% → Fecha 50% das ordens
  2. Atinge 0.5% → Fecha o restante

---

### 🌙 **Seção: Alvos por Horário (NOVO!)**

#### `Alvos diferentes por horário`
- **O que é**: Ativa/desativa sistema de horários
- **Padrão**: true (ativado)
- **Por quê**: Adapta-se à liquidez do mercado

#### `Hora início alvo reduzido (22 = 22h)`
- **O que é**: Quando começa período de baixa liquidez
- **Padrão**: 22h (10 da noite)
- **Ajuste**: Conforme seu fuso horário

#### `Hora fim alvo reduzido (6 = 6h)`
- **O que é**: Quando termina período de baixa liquidez
- **Padrão**: 6h (manhã)
- **Período**: Das 22h às 6h = 8 horas

#### `Multiplicador alvo no horário reduzido`
- **O que é**: Quanto reduz o alvo durante esse período
- **Padrão**: 0.5 (metade)
- **Exemplo**: Alvo normal R$ 50 → vira R$ 25 à noite

---

### 📅 **Seção: Meta Diária (NOVO!)**

#### `Ativar meta diária (fecha tudo ao atingir)`
- **O que é**: Liga/desliga sistema de meta diária
- **Padrão**: true (ativado)
- **Recomendação**: Manter ativado para proteger lucros

#### `Meta diária em % do balance inicial`
- **O que é**: Percentual do saldo para meta do dia
- **Padrão**: 1.0% (um porcento)
- **Exemplo**: Conta R$ 10.000 → meta de R$ 100/dia

#### `Hora início verificação meta (Brasília)`
- **O que é**: Quando começa verificar Regra 2
- **Padrão**: 17h (5 da tarde)
- **Importante**: Horário de Brasília

#### `Hora fim verificação meta (Brasília)`
- **O que é**: Quando termina verificação Regra 2
- **Padrão**: 19h (7 da noite)
- **Janela**: 17h às 19h = 2 horas

---

### 🛡️ **Seção: Stops e Defesa**

#### `Valor do stop (em moeda)`
- **O que é**: Stop loss fixo em dólar
- **Padrão**: 0.00 (desativado)
- **Exemplo**: 50 = fecha tudo ao perder $50

#### `Valor do stop (em % de Drawdown)`
- **O que é**: Stop loss baseado em DD%
- **Padrão**: 0.00 (desativado)
- **Exemplo**: 40 = fecha tudo se DD chegar a 40%

#### `% do alerta A (defesa aumento de grid)`
- **O que é**: DD% para ativar Alerta A
- **Padrão**: 10.00% (dez porcento)
- **Ação**: Aumenta grid em 1.5x

#### `% do alerta B (defesa aumento de time frame)`
- **O que é**: DD% para ativar Alerta B
- **Padrão**: 20.00% (vinte porcento)
- **Ação**: Muda para timeframe de segurança

#### `% do DD para ativar modo emergência`
- **O que é**: DD% para ativar Alerta C
- **Padrão**: 30.00% (trinta porcento)
- **Ação**: Modo ultra conservador

#### `Máximo exposição moeda por pares`
- **O que é**: Quantos pares pode ter com a mesma moeda
- **Padrão**: 1 (um par por moeda)
- **Exemplo**: Se já tem EURUSD, não abre EURJPY (EUR repetido)

#### `Período de Segurança`
- **O que é**: Timeframe usado no Alerta B
- **Padrão**: M15 (15 minutos)
- **Opções**: M5, M15, M30, H1, H4

---

### 📈 **Seção: Indicadores**

#### `Usar RSI na confluência`
- **O que é**: Incluir RSI nas análises
- **Padrão**: false (desativado)
- **RSI**: Força relativa

#### `Usar MACD na confluência`
- **O que é**: Incluir MACD nas análises
- **Padrão**: true (ativado)
- **MACD**: Convergência/Divergência de médias

#### `Usar ADX na confluência`
- **O que é**: Ativa o ADX como filtro obrigatório de entrada
- **Padrão**: true (ativado)
- **ADX**: Força da tendência
- **Importante**: Quando ativado, o ADX funciona como **condição obrigatória** (não como sinal contável). A primeira ordem só abre se ADX estiver ativo, independente dos outros sinais de confluência

#### `Usar Bollinger na confluência`
- **O que é**: Incluir Bandas de Bollinger
- **Padrão**: true (ativado)
- **Bollinger**: Volatilidade

#### `Usar Bjacare na confluência`
- **O que é**: Incluir indicador Jacaré
- **Padrão**: true (ativado)
- **Bjacare**: Sistema de médias

#### `Usar HH na confluência`
- **O que é**: Incluir Heiken Ashi
- **Padrão**: false (desativado)
- **HH**: Candlesticks suavizados

---

### 🔒 **Seção: Breakeven**

#### `Habilitar breakevan`
- **O que é**: Ativa sistema de Breakeven Cascata
- **Padrão**: true (ativado)
- **Recomendação**: Sempre manter ativado

#### `Distância em pontos para ativar breakeven`
- **O que é**: Quantos pontos o mercado precisa andar além do preço médio para ativar o breakeven
- **Padrão**: 150 pontos
- **Ajuste**: Valor menor ativa mais cedo, valor maior dá mais margem
- **Exemplo**: Se preço médio de compra = 1.1000 e breakeven = 150 pontos, ativa quando preço chega em 1.1150

---

## 🔄 Trailing Stop Individual

### O que é?
Sistema que **move o Stop Loss de cada posição individualmente** conforme o preço avança a favor, protegendo lucro progressivamente.

### Como funciona?
1. Quando uma posição individual atinge lucro de `trailing_step_pontos` (padrão: 150 pontos)
2. O SL é movido para o breakeven + `trailing_buffer_pontos` (padrão: 0 = exato)
3. A cada novo avanço de `trailing_step_pontos`, o SL avança junto
4. **Resultado**: O lucro fica cada vez mais protegido à medida que o preço avança

### Diferença do Breakeven Cascata:
- **Breakeven Cascata**: Move o SL de TODAS as posições juntas baseado no preço médio
- **Trailing Stop Individual**: Move o SL de CADA posição separadamente conforme seu próprio lucro

### Parâmetros:
- **`usar_trailing_individual`**: Ativa/desativa o sistema (padrão: true)
- **`trailing_step_pontos`**: Distância em pontos para cada passo do trailing (padrão: 150)
- **`trailing_buffer_pontos`**: Buffer em pontos acima do breakeven (padrão: 0 = exato)

### Características:
- ✅ Protege cada posição individualmente
- ✅ Funciona em conjunto com o Breakeven Cascata
- ✅ Avanço progressivo (quanto mais lucro, mais protegido)
- ✅ Não interfere com outros EAs (filtro por magic number)

---

## 💎 Fechamento por Equity

### O que é?
Sistema de **saída automática** que fecha todas as posições e remove o EA do gráfico quando a equity (patrimônio) atinge um valor alvo.

### Como funciona?
1. A cada tick, verifica se `AccountEquity >= fechar_valor_equity`
2. Se atingir, fecha TODAS as posições abertas
3. Remove o EA do gráfico automaticamente
4. **Resultado**: Garante que você saia do mercado com o patrimônio desejado

### Parâmetro:
- **`fechar_valor_equity`**: Valor de equity para fechar tudo e remover EA (padrão: 0.0 = desativado)

### Quando usar:
- Definir um objetivo de patrimônio final (ex: "quero sair quando a conta atingir R$ 15.000")
- Proteção contra ganância: define um teto e para automaticamente
- Útil para desafios de contas funded/prop firms

### Exemplo:
- Conta com R$ 10.000 de equity
- `fechar_valor_equity = 12000`
- Quando equity atingir R$ 12.000 → fecha tudo e remove o EA

---

## 📈 Carry Trade - Filtro por Diferencial de Juros

### O que é?
Estratégia que opera apenas na **direção favorável pelo diferencial de taxas de juros** entre os dois países do par de moedas.

### Conceito:
O Carry Trade é uma estratégia macroeconômica clássica: você "compra" a moeda do país com juros mais altos e "vende" a moeda do país com juros mais baixos, recebendo a diferença.

### Como funciona no EA:
1. Você informa manualmente as taxas de juros nos inputs:
   - `taxa_juros_base`: Taxa da 1a moeda do par (ex: EUR em EURUSD)
   - `taxa_juros_cotada`: Taxa da 2a moeda do par (ex: USD em EURUSD)
2. O EA calcula o diferencial: `base - cotada`
3. Se diferencial > 0 → Só compra (BUY)
4. Se diferencial < 0 → Só vende (SELL)
5. Se igual ou não configurado → Opera nos dois lados (sem filtro)

### Parâmetros:
- **`taxa_juros_base`**: Taxa de juros da moeda BASE (padrão: 0.0)
- **`taxa_juros_cotada`**: Taxa de juros da moeda COTADA (padrão: 0.0)

### Exemplo prático:
- Par: USDJPY
- Taxa EUA (base): 5.00%
- Taxa Japão (cotada): 0.50%
- Diferencial: 5.00 - 0.50 = +4.50 → **Só compra**
- Lógica: Comprar USD (juros altos) e vender JPY (juros baixos)

### Importante:
- As taxas **não se atualizam sozinhas** - você precisa alterar os inputs quando os bancos centrais mudarem as taxas
- Diferente do Swap+ que consulta a corretora automaticamente
- Ative com `tipo_op = 4` (Carry Trade)

---

## ⚙️ Seção: Trailing Stop Individual (Configurações)

#### `Habilitar trailing stop individual`
- **O que é**: Ativa sistema de trailing stop por posição
- **Padrão**: true (ativado)
- **Recomendação**: Manter ativado junto com breakeven

#### `Distância em pontos para cada passo do trailing`
- **O que é**: Quantos pontos de lucro para mover o SL
- **Padrão**: 150 pontos
- **Ajuste**: Valor menor protege mais cedo, valor maior dá mais respiro

#### `Buffer em pontos acima do breakeven`
- **O que é**: Margem extra acima do ponto de equilíbrio
- **Padrão**: 0 (move exatamente para o breakeven)
- **Exemplo**: Se buffer = 10, o SL fica 10 pontos acima do breakeven

---

## ⚙️ Seção: Fechamento por Equity (Configurações)

#### `Valor de equity para fechar tudo e remover EA`
- **O que é**: Patrimônio alvo para encerrar operações
- **Padrão**: 0.0 (desativado)
- **Exemplo**: 15000 = fecha tudo quando equity atingir R$ 15.000
- **Importante**: Ao atingir, o EA é removido do gráfico automaticamente

---

## ⚙️ Seção: Carry Trade (Configurações)

#### `Taxa de juros moeda BASE`
- **O que é**: Taxa de juros anual da primeira moeda do par
- **Padrão**: 0.0 (não configurado)
- **Exemplo**: Para EURUSD, informar a taxa do EUR (ex: 3.50)

#### `Taxa de juros moeda COTADA`
- **O que é**: Taxa de juros anual da segunda moeda do par
- **Padrão**: 0.0 (não configurado)
- **Exemplo**: Para EURUSD, informar a taxa do USD (ex: 5.00)

---

## 🌐 Filtro Macro Carry Trade (VIX + SP500 + JPY)

### O que é?
Sistema de **proteção macroeconômica** que monitora indicadores de risco global em tempo real para evitar abrir posições em ambientes adversos. Inspirado nas mesas de carry trade de grandes bancos (UBS, Goldman Sachs, JPMorgan).

### Conceito:
O carry trade funciona bem em ambientes de **risk-on** (mercados calmos, apetite por risco). Quando o VIX sobe, o SP500 cai forte, ou o JPY se fortalece rapidamente, historicamente ocorrem **carry unwinds** - liquidação em massa de posições de carry trade que causam perdas severas.

Este filtro age como um **porteiro na entrada**: só decide se você abre a primeira ordem. Uma vez com posições abertas, o grid médio/super e os Alerts A/B/C cuidam da gestão.

### Como funciona:

#### Regra principal:
- **SEM posições abertas** → Filtro macro completo decide se abre a primeira ordem
- **COM posições abertas** → Apenas verificação de emergência real (VIX ≥ 27 ou carry unwind). Grid continua normalmente sem bloqueios desnecessários

#### Níveis do VIX:
| VIX | Ambiente | Ação |
|-----|----------|------|
| < 21.0 | RISK-ON | Opera normalmente |
| 21.0 - 24.0 | NEUTRO | Alert A ativado (grid +50%) |
| 24.0 - 27.0 | RISK-OFF | Alert B ativado (TF segurança) |
| ≥ 27.0 | EMERGENCIA | Bloqueia novas ordens (primeira e grid) |
| Spike +30% dia | EMERGENCIA | Alert B forçado automaticamente |

#### Carry Unwind (alerta vermelho):
Quando **dois sinais** aparecem juntos:
- USDJPY caindo > 1.2% no dia (JPY fortalecendo com força relevante)
- VIX subindo > 10% no dia

O sistema classifica como **carry unwind em curso** e bloqueia novas aberturas até normalizar.

#### SP500:
- Se SP500 cair mais de 3.0% no dia → Bloqueia primeira ordem (risk-off)

### Dashboard no gráfico:
O EA exibe no canto do gráfico:
```
=============== MACRO CARRY ===============
VIX: 17.50 (-2.1%) | SP500: +0.35%
USDJPY: +0.12% | Unwind: nao
Ambiente: RISK-ON | VIX-A:off VIX-B:off
```

---

## ⚙️ Seção: Filtro Macro (Configurações)

#### `Ativar filtro macro carry trade`
- **O que é**: Liga/desliga todo o sistema de filtro macro
- **Padrão**: true (ativado)
- **Nota**: Se desativado, o EA opera como antes sem nenhum filtro macro

#### `Simbolo do VIX no broker`
- **O que é**: Nome do símbolo VIX na sua corretora
- **Padrão**: "Vix.s" (VT Markets)
- **Outros brokers**: Pode ser "VIX", "VIXM", "VIX.f" - verifique na sua corretora

#### `Simbolo do SP500 no broker`
- **O que é**: Nome do símbolo SP500 na sua corretora
- **Padrão**: "SP500.s" (VT Markets)

#### `VIX maximo para abrir primeira ordem`
- **O que é**: Acima deste valor, não abre a primeira ordem
- **Padrão**: 21.0
- **Conservador**: 18.0 | **Moderado**: 21.0 | **Agressivo**: 24.0

#### `VIX para acionar Alert A`
- **O que é**: VIX que aciona o Alert A (grid aumentado) mesmo sem DD alto
- **Padrão**: 21.0

#### `VIX para acionar Alert B`
- **O que é**: VIX que aciona o Alert B (timeframe segurança) mesmo sem DD alto
- **Padrão**: 24.0

#### `VIX para bloquear novas ordens`
- **O que é**: Acima deste valor, bloqueia QUALQUER nova ordem — inclusive grid (emergência real)
- **Padrão**: 27.0

#### `% de spike VIX em 1 dia para alerta`
- **O que é**: Se VIX subir este percentual em um dia, força Alert B
- **Padrão**: 30.0%
- **Exemplo**: VIX abre em 15, sobe para 19.5 (+30%) → Alert B forçado

#### `Queda % SP500 no dia para bloquear`
- **O que é**: Queda percentual do SP500 que bloqueia a primeira ordem
- **Padrão**: -3.0%

#### `Detectar carry unwind`
- **O que é**: Monitora JPY + VIX simultaneamente para detectar carry unwind
- **Padrão**: true
- **Lógica**: USDJPY caindo > 1.2% **e** VIX subindo > 10% no mesmo dia = bloqueio

#### `Simbolo USDJPY para monitorar JPY`
- **O que é**: Símbolo do USDJPY para medir força do JPY
- **Padrão**: "USDJPY"

### Pares recomendados para carry trade (somente compra):
| Par | Moeda alta | Moeda baixa | Direção |
|-----|-----------|-------------|---------|
| EURJPY | EUR | JPY | Compra |
| GBPJPY | GBP | JPY | Compra |
| USDJPY | USD | JPY | Compra |
| AUDJPY | AUD | JPY | Compra |
| NZDJPY | NZD | JPY | Compra |
| USDCHF | USD | CHF | Compra |
| AUDCHF | AUD | CHF | Compra |
| GBPCHF | GBP | CHF | Compra |

> **Dica**: Configure `tipo_op = 1` (Somente Compras) para estes pares. O filtro macro protege a entrada e os Alerts A/B/C protegem durante a operação.

---

## 🎓 Dicas de Uso

### ✅ **Configuração Conservadora**
```
Lote: 0.01
Grid Médio: 200 pontos
Grid Super: 100 pontos
Breakeven: 200 pontos
Alvo percentual: 0.5%
Meta diária: 1%
Alerta A: 10%
Alerta B: 20%
Alerta C: 30%
Limite Grid Médio: 10 ordens
```

### ⚡ **Configuração Moderada**
```
Lote: 0.02
Grid Médio: 150 pontos
Grid Super: 75 pontos
Breakeven: 150 pontos
Alvo percentual: 0.5%
Meta diária: 1.5%
Alerta A: 12%
Alerta B: 22%
Alerta C: 32%
Limite Grid Médio: 15 ordens
```

### 🚀 **Configuração Agressiva** (Apenas para experientes)
```
Lote: 0.03
Grid Médio: 100 pontos
Grid Super: 50 pontos
Breakeven: 100 pontos
Multiplicador tendência: 1.5
Alvo percentual: 0.7%
Meta diária: 2%
Alerta A: 15%
Alerta B: 25%
Alerta C: 35%
Limite Grid Médio: 20 ordens
```

---

## ⚠️ Avisos Importantes

### 🔴 **Gestão de Risco**
- **Nunca** opere com todo o capital de uma vez
- Reserve no mínimo **40% do capital** como margem de segurança
- Monitore o DD% diariamente
- Respeite os alertas de defesa

### 🟡 **Manutenção**
- Acompanhe o desempenho semanalmente
- Ajuste configurações conforme resultados
- Teste em conta demo antes de usar em conta real
- Mantenha o robô atualizado

### 🟢 **Boas Práticas**
- Comece sempre com configuração conservadora
- Aumente risco gradualmente conforme ganha experiência
- Use a meta diária para garantir lucros consistentes
- Respeite os horários de baixa liquidez

---

## 📞 Suporte

Para dúvidas, sugestões ou suporte:
- 📧 Contate o desenvolvedor: Diego Justo
- 📅 Mantenha o robô sempre atualizado
- 🔄 Versão atual: 7.0

---

## ⚖️ Isenção de Responsabilidade

**AVISO IMPORTANTE**:

Negociar com robôs envolve alto risco e pode não ser adequado para todos os investidores. Resultados anteriores não são garantia de performance futura. Você é o único responsável pelas operações realizadas.

É **fundamental** testar em conta de demonstração antes de operar com capital real.

**Trading de forex e CFDs pode resultar em perdas que excedem seu investimento inicial.**

---

*Documento criado para IAFX Prime v7 - Versão 1.3 - Fevereiro 2026*

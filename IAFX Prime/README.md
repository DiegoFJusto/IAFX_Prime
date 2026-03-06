# 📊 IAFX Prime - Expert Advisor para MetaTrader 5

![Version](https://img.shields.io/badge/Latest-v8.0-blue)
![Status](https://img.shields.io/badge/Status-Production%20Ready-green)
![Language](https://img.shields.io/badge/Language-MQL5-orange)
![License](https://img.shields.io/badge/License-Proprietary-red)

> **Robot de Grid Trading Inteligente com Dual-Strategy (IAFX + FIMATHE)**

---

## 🚀 Sobre o IAFX Prime

**IAFX Prime** é um Expert Advisor (robô de negociação) avançado para MetaTrader 5 que combina:

- ✅ **Grid Trading** com defesas inteligentes em 3 camadas
- ✅ **Indicadores de Confluência** (RSI, MACD, Bollinger, ADX, etc)
- ✅ **Sistema FIMATHE** de canais e rompimentos (v8+)
- ✅ **Breakeven Cascading** sincronizado
- ✅ **Trailing Stop** individual por posição
- ✅ **Filtros Macro** (VIX, Carry Trade, SP500)
- ✅ **Meta Diária** com 3 regras de proteção

### 🎯 Versões Disponíveis

| Versão | Status | Características | Download |
|--------|--------|-----------------|----------|
| **v7.0** | ✅ Estável | Grid + Indicadores | [v7.ex5](https://github.com/DiegoFJusto/IAFX_Prime/releases) |
| **v8.0** | ✅ Nova! | Grid + IAFX + **FIMATHE** | [v8.ex5](https://github.com/DiegoFJusto/IAFX_Prime/releases) |

---

## 📥 Como Instalar

### Passo 1: Download

**Opção A - Do GitHub (Recomendado)**
1. Acesse [Releases](https://github.com/DiegoFJusto/IAFX_Prime/releases)
2. Baixe `IAFX Prime v8.ex5` (ou v7 se preferir)

**Opção B - Clone o Repositório**
```bash
git clone https://github.com/DiegoFJusto/IAFX_Prime.git
```

### Passo 2: Copiar para MetaTrader 5

1. Abra MetaTrader 5
2. Vá em **File → Open Data Folder** (ou simplesmente procure o caminho)
3. Navegue até: `MQL5/Experts/`
4. Cole o arquivo `IAFX Prime v8.ex5` nesta pasta

**Caminho típico:**
```
C:\Users\[SeuUsuário]\AppData\Roaming\MetaQuotes\Terminal\[ID]\MQL5\Experts\
```

### Passo 3: Reiniciar MetaTrader

Feche e abra MetaTrader 5 novamente para que o EA apareça na lista.

### Passo 4: Adicionar ao Gráfico

1. Abra um gráfico (ex: EURUSD, H1)
2. Navegador (esquerda) → Expert Advisors
3. Clique 2x em `IAFX Prime v8`
4. Configure os parâmetros
5. Clique **OK**

---

## ⚙️ Configuração Rápida

### 🟢 Iniciante (Demo)

```
usar_IAFX = true
usar_FIMATHE = false        ← Mantenha desativado até conhecer

Lote Base = 0.01
Grid Médio = 150 pontos
Grid Super = 75 pontos
Meta Diária = 1%
Alerta A (DD%) = 10
Alerta B (DD%) = 20
Alerta C (DD%) = 30
```

**Resultado esperado:** Comportamento idêntico à v7

---

### 🟡 Intermediário (Dual Strategy)

```
usar_IAFX = true
usar_FIMATHE = true         ← Teste a FIMATHE

fimathe_barras = 50         ← Canais em últimas 50 barras
fimathe_percentual_ruptura = 0.5  ← Zona no meio (50%)

Lote Base = 0.01-0.05
Grid Médio = 150 pontos
Meta Diária = 1-1.5%
```

**Resultado esperado:** Primeira ordem vem de IAFX ou FIMATHE (a que sinalizar primeiro). Depois, grid e defesas funcionam normalmente.

---

### 🔴 Avançado (Customizado)

Consulte o arquivo de configuração documentado em:
- 📖 [GUIA_IAFX_PRIME_V8.md](IAFX%20Prime/GUIA_IAFX_PRIME_V8.md) (Detalhado)
- 📖 [GUIA_IAFX_PRIME_V7.md](IAFX%20Prime/GUIA_IAFX_PRIME_V7.md) (Fundamentos)

---

## 📖 Documentação

### v8 (Novo!)
- **[GUIA_IAFX_PRIME_V8.md](IAFX%20Prime/GUIA_IAFX_PRIME_V8.md)** - Guia completo com FIMATHE
- **[GUIA_IAFX_PRIME_V8.html](IAFX%20Prime/GUIA_IAFX_PRIME_V8.html)** - Versão formatada para web

### v7 (Fundamentos)
- **[GUIA_IAFX_PRIME_V7.md](IAFX%20Prime/GUIA_IAFX_PRIME_V7.md)** - Guia original (200+ páginas)
- **[GUIA_IAFX_PRIME_V7.html](IAFX%20Prime/GUIA_IAFX_PRIME_V7.html)** - Versão formatada

### 📝 Tópicos Principais

| Tópico | v7 | v8 |
|--------|:---:|:---:|
| Como funciona Grid | ✅ | ✅ |
| Indicadores | ✅ | ✅ |
| Defesas (Alertas A/B/C) | ✅ | ✅ |
| Breakeven Cascading | ✅ | ✅ |
| Meta Diária | ✅ | ✅ |
| Estratégia FIMATHE | ❌ | ✅ |
| Dual Strategy | ❌ | ✅ |

---

## 🎯 O Que é o FIMATHE (v8)

Estratégia nova que identifica **canais de consolidação** e opera em **rompimentos**:

```
1. Mede highest high (topo) nos últimas 50 barras
2. Mede lowest low (fundo) nos últimas 50 barras
3. Calcula zona neutra (50% do canal)
4. Calcula zona de rompimento (50% configurável)
5. Gera sinal:
   - "C" = Preço rompe ABAIXO → Compra
   - "V" = Preço rompe ACIMA → Venda
   - "X" = Esperando rompimento
```

**Vantagem:** Entrada rápida em canais bem definidos  
**Use quando:** Preferir sinais baseados em preço vs indicadores

### Dual Strategy (IAFX + FIMATHE)

Se ambas ativas:
1. Avalia IAFX primeiro (confluência de indicadores)
2. Se IAFX não sinalar → avalia FIMATHE (canais)
3. **Primeira a sinalizar abre a ordem**
4. Depois, grid, trailing stop e breakeven funcionam identicamente

---

## 🛡️ Defesas Inteligentes

### 3 Alertas Automáticos

| Alerta | Ativação | Ação | Nível |
|--------|----------|------|-------|
| **A** | DD% ≥ 10% | Grid aumenta 1.5x | ⚠️ Amarelo |
| **B** | DD% ≥ 20% | Muda para M15 (segurança) | 🟠 Laranja |
| **C** | DD% ≥ 30% | Reduz lote pela metade | 🔴 Vermelho |

### Filtros Macro

- 📊 **VIX**: Bloqueia entrada com VIX alto
- 💱 **Carry Trade**: Monitora USDJPY + VIX para unwind
- 📈 **SP500**: Bloqueia em queda > 3%

### Meta Diária (3 Regras)

1. **Lucro 1%** → Fecha tudo
2. **17h-19h Brasília** → Se lucro > loss, fecha tudo
3. **Friday 3%** → Após 12h sexta, se semanal ≥ 3% fecha

---

## 💻 Características Técnicas

### Indicadores Suportados
- RSI (com divergência)
- MACD
- Bollinger Bands
- Bjacare
- ADX
- Heiken Ashi
- Estocástico
- Volume
- Custom Indicators (via iCustom)

### Parâmetros de Entrada

#### Estratégias (v8)
```
usar_IAFX [true/false]           → Confluência de indicadores
usar_FIMATHE [true/false]        → Canais e rompimentos
fimathe_barras [1-500]           → Janela do canal (default: 50)
fimathe_percentual_ruptura [0.1-1.0] → Zona de rompimento (default: 0.5)
```

#### Grid
```
grid_input [pontos]              → Espaçamento grid (default: 150)
grid_super_pontos [pontos]       → Grid agressivo (default: 75)
max_ordens_grid_medio [int]      → Máximo de ordens (default: 15)
```

#### Defesa
```
alertaDDA [%]                    → Alerta A por DD (default: 10)
alertaDDB [%]                    → Alerta B por DD (default: 20)
alertaDDC [%]                    → Alerta C por DD (default: 30)
timeframe_seguranca [timeframe]  → TF para Alert B (default: M15)
```

#### Risco
```
lote [0.01-100]                  → Lote base
x_lote [1.0-10.0]                → Multiplicador grid super
stop [USD]                       → Stop loss fixo (0 = desativado)
stopDD [%]                       → Stop loss por DD (0 = desativado)
```

---

## ✅ Checklist de Instalação

- [ ] Downloaded `IAFX Prime v8.ex5`
- [ ] Copied para `MQL5/Experts/`
- [ ] Reiniciou MetaTrader 5
- [ ] EA aparece em Expert Advisors
- [ ] Abriu em conta DEMO (não real!)
- [ ] Leu a documentação v8
- [ ] Configurou parâmetros conservadores
- [ ] Testou 1-2 semanas antes de conta real

---

## ⚠️ Avisos Importantes

### 🔴 Risco Alto
- Trading com EA envolve **risco elevado**
- Você pode perder **mais que investiu**
- Sempre teste em **DEMO** primeiro
- Use apenas **40-60% do capital** em risco

### 🟡 Recomendações
- Monitore o robô nas primeiras semanas
- Acompanhe DD% diariamente
- Respeite os Alertas A/B/C
- Revise configurações semanalmente
- Mantenha v7 como backup de contingência

### 🟢 Melhores Práticas
- Comece com FIMATHE desativado (apenas IAFX)
- Aumente risco gradualmente
- Use meta diária para ganhos consistentes
- Registre resultados por semana
- Teste novas configs antes em demo

---

## 🔄 Migração de v7 para v8

### Para usuários v7:

```
1. Baixe v8.ex5
2. Copie para pasta Experts
3. Novo gráfico, configure:
   usar_IAFX = true
   usar_FIMATHE = false        ← Assim funciona como v7
4. Teste 1-2 semanas
5. Depois ative FIMATHE se quiser
```

✅ **v7 permanece funcional** como backup
✅ **Todas as configs v7 são respeitadas** em v8
✅ **Nenhuma degradação de performance**

---

## 📞 Suporte & FAQ

### Problemas Comuns

**P: O EA não aparece em Expert Advisors**
> Certifique-se que está em `MQL5/Experts/` (não em subpastas)
> Reinicie MetaTrader

**P: Erro "License key not valid"**
> Configure a chave de acesso nos inputs
> Todo EA exige uma chave para operar

**P: Posso usar v7 e v8 ao mesmo tempo?**
> Sim! Cada um em um gráfico/par diferente
> Recomendado: limite a 2-3 pares por versão

**P: Qual a melhor estratégia, IAFX ou FIMATHE?**
> Ambas têm méritos diferentes:
> - IAFX: Mais confirmação (indicadores)
> - FIMATHE: Mais rápido (preço puro)
> Use DUAL para aproveitar ambas

**P: Perdi dinheiro, o que fazer?**
> 1. Revise suas configurações
> 2. Analise o DD% que atingiu
> 3. Aumente o espaçamento do grid
> 4. Reduza o lote
> 5. Teste em demo antes de voltar

---

## 📊 Estrutura do Repositório

```
IAFX_Prime/
├── IAFX Prime/
│   ├── IAFX Prime v7.mq5              ← Código fonte v7
│   ├── IAFX Prime v7.ex5              ← Compilado v7
│   ├── IAFX Prime v8.mq5              ← Código fonte v8
│   ├── IAFX Prime v8.ex5              ← Compilado v8
│   ├── GUIA_IAFX_PRIME_V7.md          ← Guia v7
│   ├── GUIA_IAFX_PRIME_V7.html        ← Guia v7 (web)
│   ├── GUIA_IAFX_PRIME_V8.md          ← Guia v8
│   ├── GUIA_IAFX_PRIME_V8.html        ← Guia v8 (web)
│   └── ...
├── README.md                           ← Este arquivo
└── LICENSE
```

---

## 🌟 Principais Melhorias v8

✨ **Estratégia FIMATHE** - Canais e rompimentos  
✨ **Dual Strategy** - IAFX + FIMATHE working together  
✨ **Guias Detalhados** - Documentação em MD + HTML  
✨ **Backward Compatible** - Tudo de v7 funciona igual  
✨ **Maior Flexibilidade** - Ative/desative estratégias via inputs  

---

## 📈 Resultados Esperados

Este é um EA de **gestão de risco**, não de geração milagrosa:

| Meta | Timeframe | Condição |
|------|-----------|----------|
| +1% semanal | 5-7 dias | Com meta diária ligada |
| +4% mensal | 30 dias | Consistente |
| DD máximo | - | 20-30% é normal |

**Importante:** Resultados variam com:
- Configuração escolhida
- Volatilidade do mercado
- Liquidez do par
- Slippage da corretora
- Seu gerenciamento

---

## 🔐 Segurança & Licença

Este EA requer uma **chave de licença** para operar.
- ✅ Licenças por período (mês, trimestre, ano)
- ✅ Suporte prioritário incluído
- ✅ Atualizações automáticas

Para adquirir licença ou mais informações:
> Contate: `dev@iafxprime.com` (exemplo)

---

## 📜 Créditos

**Desenvolvido por:** Diego Justo  
**Versão Atual:** 8.0  
**Data:** Março 2026  
**Plataforma:** MetaTrader 5 (MQL5)  

---

## ⭐ Deixe uma Estrela!

Se o IAFX Prime foi útil, considere deixar uma ⭐ no repositório!

[![GitHub stars](https://img.shields.io/github/stars/DiegoFJusto/IAFX_Prime?style=social)](https://github.com/DiegoFJusto/IAFX_Prime)

---

## 📋 Changelog

### v8.0 (Março 2026)
- ✨ Estratégia FIMATHE adicionada
- ✨ Dual strategy (IAFX + FIMATHE)
- 📖 Guias completos (MD + HTML)
- 🐛 Melhorias de código
- ✅ 100% backward compatible com v7

### v7.0 (Anterior)
- Grid trading com defesas
- Indicadores de confluência
- Sistema de meta diária
- Filtros macro VIX/Carry

---

## 📝 Licença

Proprietary License - Todos os direitos reservados

Uso não autorizado é proibido.

---

**Última atualização:** 6 de Março de 2026

**Próximas atualizações sempre em:** [GitHub Releases](https://github.com/DiegoFJusto/IAFX_Prime/releases)

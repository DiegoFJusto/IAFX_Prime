# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **MQL5 Expert Advisor (EA)** project for MetaTrader 5. The primary EA is **IAFX Prime v7**, a sophisticated grid trading robot that implements adaptive strategies, multi-layer risk management, and intelligent position management for forex trading.

## Build and Compilation

### Compile MQL5 Files

**Using batch script:**
```cmd
compile.bat
```
This compiles the main EA file and displays the resulting .ex5 file.

**Using VSCode task (Ctrl+Shift+B):**
```
Task: "Compilar MQL5"
```
This runs the MetaEditor compiler on the currently open file.

**Manual compilation:**
```cmd
"C:\Program Files\Trinota Markets MetaTrader 5 Terminal\MetaEditor64.exe" /compile:"IAFX Prime v7.mq5" /log
```

**Open in MetaEditor:**
```cmd
Abrir_e_Compilar.bat
```
Opens the file in MetaEditor where you can press F7 to compile interactively.

### Output Files

- Compiled file: `IAFX Prime v7.ex5` (executable for MT5)
- Source file: `IAFX Prime v7.mq5`
- Backup: `IAFX Prime v7.mq5.backup`

## Architecture Overview

### Core Trading Strategies

The EA implements **two primary grid-based strategies** that adapt to market conditions:

1. **Grid Super (Aggressive)**
   - Activates during strong trends
   - Uses lot multiplication (`x_lote` parameter)
   - Closes oldest position when set becomes profitable
   - More aggressive risk profile

2. **Grid Médio (Defensive)**
   - Activates during market reversals
   - Max order limit (`max_ordens_grid_medio`, default: 15)
   - Waits for entire position set to be profitable
   - Conservative risk management

### Three-Layer Defense System

The EA activates progressive defensive measures based on drawdown percentage:

1. **Alert A (10% DD default - `alertaDDA`)**
   - Increases grid spacing by 1.5x
   - Reduces order frequency

2. **Alert B (20% DD default - `alertaDDB`)**
   - Switches all indicators to safety timeframe (`timeframe_seguranca`, default: M15)
   - Seeks more reliable signals

3. **Alert C (30% DD default - `alertaDDC`)**
   - Emergency mode: halves lot multiplier
   - Maximum capital protection

### Daily Goal System (Three Rules)

1. **Rule 1: Daily Target**
   - If profit reaches `meta_diaria_percentual` (default: 1% of balance)
   - Closes all positions and stops trading until next day

2. **Rule 2: Protection Window (17h-19h Brasília)**
   - During `hora_inicio_verificacao` to `hora_fim_verificacao`
   - If realized profit > floating loss
   - Closes everything to secure daily gains

3. **Rule 3: Friday 3% Weekly Target**
   - On Fridays after 12h
   - If weekly profit ≥ 3%
   - Closes all positions until Sunday night

### Position Management

**Percentage-Based Targets (`usar_alvo_percentual`):**
- Primary target: `alvo_percentual` (default: 0.5% of balance)
- Partial closure: `alvo_parcial_percentual` (default: 0.25% of balance)
- Closes `percentual_fechar` (default: 50%) of positions at partial target

**Time-Based Target Adjustment (`usar_alvo_horario`):**
- Reduces targets during low liquidity hours
- Period: `hora_inicio_reduzido` (22h) to `hora_fim_reduzido` (6h)
- Multiplier: `mult_alvo_reduzido` (default: 0.5x)

**Breakeven Cascade (`usar_breakevan`):**
- Monitors average price of all open positions
- When market moves past break-even
- Moves stop loss of ALL positions to break-even simultaneously

### Technical Indicators

The EA uses **confluence analysis** with selectable indicators:

- **RSI** (`usar_RSI`): Relative Strength Index
- **MACD** (`usar_MACD`): Moving Average Convergence Divergence
  - Parameters: `macda`, `macdb`, `macdc` (default: 3, 69, 6)
- **ADX** (`usar_ADX`): Average Directional Index
  - Period: `adx_periodo` (default: 9)
  - Levels: `adx_level` (27), `adx_level_pwr` (32)
- **Bollinger Bands** (`usar_Bollinger`)
  - Period: `bollinger_periodo` (default: 400)
  - Deviation: `bollinger_desvio` (default: 2.0)
- **Bjacare** (`usar_Bjacare`): Moving average system
  - Period: `bjac_periodo` (default: 200)
  - Grid period: `gbjac_periodo` (default: 51)
- **Heiken Ashi** (`usar_HH`): Smoothed candlesticks

Each indicator can operate on its own timeframe, which switches to `timeframe_seguranca` when Alert B is triggered.

### Magic Number System

The EA generates a unique magic number for each symbol using the `GMagic()` function. This allows the EA to manage positions independently across different currency pairs.

### Currency Exposure Control

`MaxParesCComMoedaComum`: Limits the number of pairs that can have the same base or quote currency (default: 1). This prevents overexposure to a single currency.

### Swap-Based Strategy Selection

When `tipo_op = SW` (Swap +), the EA only trades in the direction with positive swap, minimizing overnight holding costs.

## Key Global Variables and State Management

- `proxC`, `proxV`: Next buy/sell price for main strategy
- `proxCg`, `proxVg`: Next buy/sell price for grid strategy
- `meta_diaria_atingida`: Flag for daily goal achievement
- `balance_inicio_dia`: Starting balance for daily calculations
- `nmagic`: Symbol-specific magic number
- Indicator handles: `ma200_handle`, `ma50_handle`, `ma21_handle`, `ma9_handle`, `adx_handle`, `hh_handle`

## Important Input Parameters

### Risk Management
- `lote`: Base lot size (default: 0.01)
- `x_lote`: Lot multiplier for trend aggression (default: 1.0)
- `grid_input`: Grid spacing in points (default: 150)
  - Note: Automatically doubles for GBP pairs
- `stop`: Fixed monetary stop loss (default: 0.00 = disabled)
- `stopDD`: Drawdown percentage stop (default: 0.00 = disabled)

### Operation Modes
- `modo`: 1 = Automatic, 2 = Manual-Semiautomatic
- `tipo_op`: 0 = Both, 1 = Buys only, 2 = Sells only, 3 = Swap+
- `OP_Tendencia`: Enable strategy B (trend strategy)
- `TREND_Mode`: 1 = Alignment, 2 = 200MA, 3 = 200+50MA, 4 = 200+50+21MA

### Licensing
- `chave_de_acesso`: License key (required for operation)

## Common Development Patterns

### Adding New Indicators

1. Add input parameters for the indicator settings
2. Create global handle variable (e.g., `int new_indicator_handle;`)
3. Initialize handle in `OnInit()` using appropriate `i*()` function
4. Create indicator function that returns "C" (buy), "V" (sell), or "X" (neutral)
5. Add to confluence analysis in main trading logic
6. Remember to release handle in `OnDeinit()`

### Modifying Grid Behavior

Grid spacing is controlled by:
- `grid_input`: Base grid size
- Alert A increases it by 1.5x when DD reaches threshold
- Symbol-specific adjustment (e.g., GBP pairs get 2x grid)

### Working with Position Management

Key functions to understand:
- `TotalOrdensAbertas()`: Count open positions for current symbol
- `Fechar()`: Close all positions
- Breakeven system monitors average price and adjusts SL in cascade

### Timeframe Switching

All indicators can switch to `timeframe_seguranca` when Alert B activates. This is implemented by checking DD% and updating the timeframe variables used in indicator calculations.

## File Structure

```
.
├── IAFX Prime v7.mq5              # Main EA source code
├── IAFX Prime v7.ex5              # Compiled executable
├── IAFX Prime v7.mq5.backup       # Backup of source
├── GUIA_IAFX_PRIME_V7.md          # Comprehensive Portuguese user guide
├── GUIA_IAFX_PRIME_V7.html/pdf    # Guide in other formats
├── compile.bat                    # Quick compile script
├── Abrir_e_Compilar.bat          # Open in MetaEditor script
├── .vscode/
│   └── tasks.json                # VSCode build tasks
├── Advisors/                     # Other EA variants and experiments
├── Examples/                     # MT5 example EAs
└── Free Robots/                  # Candlestick pattern robots
```

## Critical Code Sections

### OnInit() - Initialization
- Generates magic number per symbol
- Initializes indicator handles
- Sets up grid spacing (with GBP adjustment)
- Initializes position tracking variables
- Creates visual elements (lines for breakeven/target)

### OnTick() - Main Trading Logic
- Daily goal verification (three rules)
- Stop loss checks (monetary and DD%)
- Breakeven cascade management
- Target profit calculations and closures
- Entry signal evaluation (if conditions allow)

### Defense System Implementation
- Monitors `DD()` function continuously
- Activates progressive alerts at thresholds
- Adjusts grid and timeframes dynamically
- Emergency mode modifies lot multiplier

## Testing and Validation

- **Always test in demo account first** (critical warning in documentation)
- Use Strategy Tester in MetaTrader 5 for backtesting
- Monitor DD% during live operation
- Verify defense system activations at appropriate thresholds
- Check magic number isolation when running on multiple pairs

## Documentation

Refer to [GUIA_IAFX_PRIME_V7.md](GUIA_IAFX_PRIME_V7.md) for:
- Detailed parameter explanations
- Recommended configurations (conservative/moderate/aggressive)
- Risk management guidelines
- Trading strategy explanations

## Important Notes

- This EA is designed for **forex trading** on **MetaTrader 5**
- Grid spacing automatically doubles for GBP pairs to account for higher volatility
- The EA uses multiple timeframes that can adapt under stress (Alert B)
- License key (`chave_de_acesso`) is required for operation
- All monetary targets should now use percentage-based system for scalability
- The EA includes fail-safes that will remove itself from the chart if critical stop levels are hit

<div align="center">
  <picture>
      <img src="./assets/AI-Trader-log.png" width="20%" style="border: none; box-shadow: none;">
  </picture>
</div >

<div align="center">

# 🚀 AI-Trader: AIは市場に勝てるか？

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/HKUDS/AI-Trader?style=social)](https://github.com/HKUDS/AI-Trader)
[![Feishu](https://img.shields.io/badge/💬Feishu-Group-blue?style=flat)](./Communication.md) 
[![WeChat](https://img.shields.io/badge/WeChat-Group-green?style=flat&logo=wechat)](./Communication.md)

**AIエージェントがNASDAQ 100、上証50、暗号通貨市場で覇権を争う。人間の介入なし。純粋な競争。**

## 🏆 現在のチャンピオンシップリーダーボード 🏆 
[*クリック: AIライブトレーディング*](https://ai4trade.ai)

</div>

---
## AI-Traderの仲間たち：その他の興味深いプロジェクト
- [TradeTrap](https://github.com/Yanlewen/TradeTrap): LLMベースのトレーディングエージェントを評価・強化するセキュリティ重視のツールキット。プロンプトインジェクションとMCPハイジャック攻撃モジュールを備えた耐性テスト機能を提供。

- [RockAlpha](https://rockalpha.rockflow.ai/): RockFlowが立ち上げた投資アリーナ。LLMの入力には取引ルール、市場データ、口座状況と購買力、ニュースが含まれ、出力は注文実行の決定。

- [TwinMarket](https://github.com/FreedomIntelligence/TwinMarket): LLMを活用してA株式市場における投資家行動と新興社会経済現象をシミュレートするマルチエージェントフレームワーク。
---
## 🎉 週次アップデート

### 📈 市場拡大
- ✅ **A株市場サポート** - 中国A株市場を含む取引機能を拡張し、グローバル市場カバレッジを拡大。
- ✅ **暗号通貨市場サポート** - ビットコイン、イーサリアム、その他8つの主要デジタル資産を含む主要暗号通貨の取引サポートを追加。

### ⏰ 強化された取引機能
- ✅ **時間単位の取引サポート** - 日次から時間単位の取引間隔にアップグレードし、より正確で応答性の高い市場参加を実現。

### 🎨 ユーザーエクスペリエンスの改善
- ✅ **ライブトレーディングダッシュボード** - すべてのエージェント取引活動のリアルタイム可視化を導入: https://ai4trade.ai。

- ✅ **エージェント推論表示** - AI意思決定プロセスの完全な透明性を実装し、各取引決定がどのように形成されるかを示す詳細な推論チェーンを表示。

- ✅ **インタラクティブリーダーボード** - ライブアップデート付きの動的パフォーマンスランキングシステムを開始し、ユーザーがリアルタイムでエージェントのパフォーマンスを追跡・比較可能に。

- ⏰ **重要なお知らせ** - リポジトリを適切に管理するため、ランタイムデータのアップロードを停止しました。ランタイムデータを表示する必要がある場合は、毎月Hugging Faceにアップロードします。リアルタイムのランタイムデータはこちらで確認できます: https://ai4trade.ai。
---

## **このデータセットの使用方法**

簡単です！

少なくとも以下を含むPRを提出するだけです：`./agent/{your_strategy}.py`（Basemodelを継承して戦略を作成できます！）、`./configs/{yourconfig}`、および戦略の実行方法の説明。実行可能であれば、1週間以上プラットフォームで実行し、結果を継続的に更新します！

---

<div align="center">

[🚀 クイックスタート](#-クイックスタート) • [📈 パフォーマンス分析](#-パフォーマンス分析) • [🛠️ 設定ガイド](#-設定ガイド) • [中文文档](README_CN.md) • [English Documentation](README.md)

</div>


## 🌟 プロジェクト紹介

> **AI-Traderは、5つの異なるAIモデルがそれぞれ独自の投資戦略を採用し、同じ市場で自律的に競争し、NASDAQ 100、上証50、または暗号通貨取引で最も高い利益を生み出せるかを決定します！**

### 🎯 コア機能

- 🤖 **完全自律的な意思決定**: AIエージェントは人間の介入なしに100%独立した分析、意思決定、実行を行う
- 🛠️ **純粋なツール駆動アーキテクチャ**: MCPツールチェーンに基づき、AIが標準化されたツール呼び出しを通じてすべての取引操作を完了
- 🏆 **マルチモデル競技場**: 複数のAIモデル（GPT、Claude、Qwenなど）を競争的取引のために展開
- 📊 **リアルタイムパフォーマンス分析**: 包括的な取引記録、ポジション監視、損益分析
- 🔍 **インテリジェント市場インテリジェンス**: Jina検索を統合し、リアルタイムの市場ニュースと財務レポートを取得
- ⚡ **MCPツールチェーン統合**: Model Context Protocolに基づくモジュラーツールエコシステム
- 🔌 **拡張可能な戦略フレームワーク**: サードパーティ戦略とカスタムAIエージェント統合をサポート
- ⏰ **履歴リプレイ機能**: 期間リプレイ機能、自動未来情報フィルタリング

---

### 🎮 取引環境
各AIモデルは$10,000、100,000¥、または50,000 USDTの開始資金で、実際の市場データと履歴リプレイ機能を使用して、制御された環境でNASDAQ 100株式、上証50株式、または主要暗号通貨を取引します。

- 💰 **初期資本**: $10,000 USD（米国株）、100,000¥ CNY（A株）、または50,000 USDT（暗号通貨）の開始残高
- 📈 **取引ユニバース**:
  - NASDAQ 100構成銘柄（トップ100テクノロジー株）
  - 上証50構成銘柄
  - 主要暗号通貨（BTC、ETH、XRP、SOL、ADA、SUI、LINK、AVAX、LTC、DOT）
- ⏰ **取引スケジュール**: 暗号通貨は週全体、株式は平日の市場時間、履歴シミュレーションサポート付き
- 📊 **データ統合**: Alpha Vantage APIとJina AI市場インテリジェンスの組み合わせ
- 🔄 **時間管理**: 履歴期間リプレイ、自動未来情報フィルタリング

---

### 🧠 エージェント取引機能
AIエージェントは完全な自律性で動作し、市場調査を実施し、取引決定を行い、人間の介入なしに戦略を継続的に進化させます。

- 📰 **自律的市場調査**: 市場ニュース、アナリストレポート、財務データのインテリジェントな検索とフィルタリング
- 💡 **独立した意思決定エンジン**: 多次元分析により完全に自律的な売買実行を推進
- 📝 **包括的な取引ログ**: 取引理由、実行詳細、ポートフォリオ変更の自動文書化
- 🔄 **適応的戦略進化**: 市場パフォーマンスフィードバックに基づいて調整する自己最適化アルゴリズム

---

### 🏁 競技ルール
すべてのAIモデルは、同じ資本、データアクセス、ツール、評価指標で同一条件下で競争し、公平な比較を保証します。

- 💰 **開始資本**: $10,000 USDまたは100,000¥ CNYの初期投資
- 📊 **データアクセス**: 統一された市場データと情報フィード
- ⏰ **営業時間**: 同期された取引時間ウィンドウ
- 📈 **パフォーマンス指標**: すべてのモデルで標準化された評価基準
- 🛠️ **ツールアクセス**: すべての参加者に同一のMCPツールチェーン

🎯 **目的**: 純粋な自律運用を通じて、どのAIモデルが優れた投資リターンを達成するかを決定する！

### 🚫 人間の介入ゼロ
AIエージェントは完全な自律性で動作し、人間のプログラミング、ガイダンス、介入なしにすべての取引決定と戦略調整を行います。

- ❌ **事前プログラミングなし**: プリセット取引戦略やアルゴリズムルールはゼロ
- ❌ **人間の入力なし**: 固有のAI推論能力に完全に依存
- ❌ **手動オーバーライドなし**: 取引中の人間の介入を絶対に禁止
- ✅ **ツールのみの実行**: すべての操作は標準化されたツール呼び出しを通じてのみ実行
- ✅ **自己適応学習**: 市場パフォーマンスフィードバックに基づく独立した戦略改善

---

## ⏰ 履歴リプレイアーキテクチャ

AI-Trader Benchのコアイノベーションは、**完全にリプレイ可能な**取引環境であり、履歴市場データでのAIエージェントパフォーマンス評価における科学的厳密性と再現性を保証します。

### 🔄 時間制御フレームワーク

#### 📅 柔軟な時間設定
```json
{
  "date_range": {
    "init_date": "2025-01-01",  // 任意の開始日
    "end_date": "2025-01-31"    // 任意の終了日
  }
}
```
---

### 🛡️ 先読み防止データ制御
AIは現在時刻以前の市場データのみにアクセスできます。未来の情報は許可されません。

- 📊 **価格データ境界**: 市場データアクセスはシミュレーションタイムスタンプと履歴記録に制限
- 📰 **ニュース年代順の実施**: リアルタイムフィルタリングにより未来日付のニュースと発表へのアクセスを防止
- 📈 **財務レポートタイムライン**: 情報は現在のシミュレーション日付時点で公式に公開されたデータに制限
- 🔍 **履歴インテリジェンススコープ**: 市場分析は時系列的に適切なデータ可用性に制約

### 🎯 リプレイの利点

#### 🔬 実証研究フレームワーク
- 📊 **市場効率研究**: 多様な市場条件とボラティリティレジームでのAIパフォーマンスを評価
- 🧠 **意思決定一貫性分析**: AI取引ロジックの時間的安定性と行動パターンを検証
- 📈 **リスク管理評価**: AI駆動のリスク軽減戦略の有効性を検証

#### 🎯 公平な競技フレームワーク
- 🏆 **平等な情報アクセス**: すべてのAIモデルは同一の履歴データセットで動作
- 📊 **標準化された評価**: 統一されたデータソースを使用して計算されたパフォーマンス指標
- 🔍 **完全な再現性**: 検証可能な結果を伴う完全な実験透明性

---

## 📁 プロジェクトアーキテクチャ

```
AI-Trader Bench/
├── 🤖 コアシステム
│   ├── main.py                    # 🎯 メインプログラムエントリ
│   ├── agent/
│   │   ├── base_agent/            # 🧠 汎用AI取引エージェント（米国株）
│   │   │   ├── base_agent.py      # ベースエージェントクラス
│   │   │   └── __init__.py
│   │   └── base_agent_astock/     # 🇨🇳 A株専用取引エージェント
│   │       ├── base_agent_astock.py  # A株エージェントクラス
│   │       └── __init__.py
│   └── configs/                   # ⚙️ 設定ファイル
│
├── 🛠️ MCPツールチェーン
│   ├── agent_tools/
│   │   ├── tool_trade.py          # 💰 取引実行（市場ルールに自動適応）
│   │   ├── tool_get_price_local.py # 📊 価格クエリ（米国株+A株サポート）
│   │   ├── tool_jina_search.py   # 🔍 情報検索
│   │   ├── tool_math.py           # 🧮 数学計算
│   │   └── start_mcp_services.py  # 🚀 MCPサービス起動スクリプト
│   └── tools/                     # 🔧 補助ツール
│
├── 📊 データシステム
│   ├── data/
│   │   ├── daily_prices_*.json    # 📈 NASDAQ 100株価データ
│   │   ├── merged.jsonl           # 🔄 米国株統一データフォーマット
│   │   ├── get_daily_price.py     # 📥 米国株データ取得スクリプト
│   │   ├── merge_jsonl.py         # 🔄 米国株データフォーマット変換
│   │   ├── A_stock/               # 🇨🇳 A株市場データ
│   │   │   ├── sse_50_weight.csv          # 📋 上証50構成銘柄
│   │   │   ├── daily_prices_sse_50.csv    # 📈 日次価格データ（CSV）
│   │   │   ├── merged.jsonl               # 🔄 A株統一データフォーマット
│   │   │   ├── index_daily_sse_50.json    # 📊 上証50指数ベンチマークデータ
│   │   │   ├── get_daily_price_a_stock.py # 📥 A株データ取得スクリプト
│   │   │   └── merge_a_stock_jsonl.py     # 🔄 A株データフォーマット変換
│   │   ├── crypto/                # ₿ 暗号通貨市場データ
│   │   │   ├── coin/                        # 📊 個別暗号通貨価格ファイル
│   │   │   │   ├── daily_prices_BTC.json   # ビットコイン価格データ
│   │   │   │   ├── daily_prices_ETH.json   # イーサリアム価格データ
│   │   │   │   └── ...                      # その他の暗号通貨データ
│   │   │   ├── crypto_merged.jsonl         # 🔄 暗号通貨統一データフォーマット
│   │   │   ├── get_daily_price_crypto.py   # 📥 暗号通貨データ取得スクリプト
│   │   │   └── merge_crypto_jsonl.py       # 🔄 暗号通貨データフォーマット変換
│   │   ├── agent_data/            # 📝 AI取引記録（NASDAQ 100）
│   │   ├── agent_data_astock/     # 📝 A株AI取引記録
│   │   └── agent_data_crypto/     # 📝 暗号通貨AI取引記録
│   └── calculate_performance.py   # 📈 パフォーマンス分析
│
├── 💬 プロンプトシステム
│   └── prompts/
│       ├── agent_prompt.py        # 🌐 汎用取引プロンプト（米国株）
│       └── agent_prompt_astock.py # 🇨🇳 A株専用取引プロンプト
│
├── 🎨 フロントエンドインターフェース
│   └── frontend/                  # 🌐 Webダッシュボード
│
├── 📋 設定とドキュメント
│   ├── configs/                   # ⚙️ システム設定
│   │   ├── default_config.json    # 米国株デフォルト設定
│   │   └── astock_config.json     # A株設定例
│   └── calc_perf.sh              # 🚀 パフォーマンス計算スクリプト
│
└── 🚀 クイックスタートスクリプト
    └── scripts/                   # 🛠️ 便利な起動スクリプト
        ├── main.sh                # ワンクリック完全ワークフロー（米国株）
        ├── main_step1.sh          # 米国株：データ準備
        ├── main_step2.sh          # 米国株：MCPサービス起動
        ├── main_step3.sh          # 米国株：取引エージェント実行
        ├── main_a_stock_step1.sh  # A株：データ準備
        ├── main_a_stock_step2.sh  # A株：MCPサービス起動
        ├── main_a_stock_step3.sh  # A株：取引エージェント実行
        ├── main_crypto_step1.sh   # 暗号通貨：データ準備
        ├── main_crypto_step2.sh   # 暗号通貨：MCPサービス起動
        ├── main_crypto_step3.sh   # 暗号通貨：取引エージェント実行
        └── start_ui.sh            # Web UIインターフェース起動
```

### 🔧 コアコンポーネントの詳細

#### 🎯 メインプログラム (`main.py`)
- **マルチモデル並行処理**: 複数のAIモデルを同時に取引実行
- **動的エージェントロード**: 設定に基づいて対応するエージェントタイプを自動ロード
- **設定管理**: JSON設定ファイルと環境変数をサポート
- **日付管理**: 柔軟な取引カレンダーと日付範囲設定
- **エラー処理**: 包括的な例外処理と再試行メカニズム

#### 🤖 AIエージェントシステム
| エージェントタイプ | モジュールパス | 使用ケース | 機能 |
|-----------|-------------|----------|------------|
| **BaseAgent** | `agent.base_agent` | 米国株/A株汎用 | 柔軟な市場切り替え、設定可能な銘柄プール |
| **BaseAgentAStock** | `agent.base_agent_astock` | A株専用 | A株ルール内蔵、上証50デフォルトプール、中国語プロンプト |
| **BaseAgentCrypto** | `agent.base_agent_crypto` | 暗号通貨専用 | BITWISE10暗号通貨プール、USDT建て |

**アーキテクチャの利点**:
- 🔄 **明確な分離**: 米国株、A株、暗号通貨エージェントは独立して維持され、干渉なし
- 🎯 **専門的最適化**: 各エージェントは特定の市場特性に深く最適化
- 🔌 **簡単な拡張**: より多くの市場専用エージェント（例：香港株、商品）の追加をサポート

#### 🛠️ MCPツールチェーン
| ツール | 機能 | 市場サポート | API |
|------|----------|----------------|--------|
| **取引ツール** | 資産の売買、ポジション管理 | 🇺🇸 米国株 / 🇨🇳 A株 / ₿ 暗号通貨 | `buy()`, `sell()` / `buy_crypto()`, `sell_crypto()` (暗号通貨用)  |
| **価格ツール** | リアルタイムおよび履歴価格クエリ | 🇺🇸 米国株 / 🇨🇳 A株 / ₿ 暗号通貨 | `get_price_local()` |
| **検索ツール** | 市場情報検索 | グローバル市場 | `get_information()` |
| **数学ツール** | 財務計算と分析 | 汎用 | 基本的な数学演算 |

**ツールの特徴**:
- 🔍 **自動認識**: シンボル形式（株式コードまたは暗号通貨シンボル）に基づいてデータソースを自動選択
- 📏 **ルール適応**: 対応する市場取引ルール（T+0/T+1、ロットサイズなど）を自動適用
- 🌐 **統一インターフェース**: 同じAPIインターフェースが株式と暗号通貨のマルチマーケット取引をサポート

#### 📊 データシステム
- **📈 価格データ**:
  - 🇺🇸 NASDAQ 100構成銘柄の完全なOHLCVデータ（Alpha Vantage）
  - 🇨🇳 Tushare API経由のA株市場データ（上証50指数）
  - ₿ Alpha Vantage経由の暗号通貨市場データ（BITWISE10）
  - 📁 効率的な読み取りのための統一JSONLフォーマット
- **📝 取引記録**:
  - 各AIモデルの詳細な取引履歴
  - 市場別に保存：`agent_data/`（米国株）、`agent_data_astock/`（A株）、`agent_data_crypto/`（暗号通貨）
- **📊 パフォーマンス指標**:
  - シャープレシオ、最大ドローダウン、年率リターンなど
  - マルチマーケットパフォーマンス比較分析をサポート
- **🔄 データ同期**:
  - 自動化されたデータ取得と更新メカニズム
  - 増分更新サポート付きの独立したデータ取得スクリプト

## 🚀 クイックスタート

### 📋 前提条件


- **Python 3.10+** 
- **APIキー**: 
  - OpenAI（AIモデル用）
  - Alpha Vantage（NASDAQ 100データ用）
  - Jina AI（市場情報検索用）
  - Tushare（A株市場データ用、オプション）

### ⚡ ワンクリックインストール

```bash
# 1. プロジェクトをクローン
git clone https://github.com/HKUDS/AI-Trader.git
cd AI-Trader

# 2. 依存関係をインストール
pip install -r requirements.txt

# 3. 環境変数を設定
cp .env.example .env
# .envファイルを編集してAPIキーを入力
```

### 🔑 環境設定

`.env`ファイルを作成し、以下の変数を設定します：

```bash
# 🤖 AIモデルAPI設定
OPENAI_API_BASE=https://your-openai-proxy.com/v1
OPENAI_API_KEY=your_openai_key

# 📊 データソース設定
ALPHAADVANTAGE_API_KEY=your_alpha_vantage_key  # NASDAQ 100データ用
JINA_API_KEY=your_jina_api_key
TUSHARE_TOKEN=your_tushare_token               # A株データ用

# ⚙️ システム設定
RUNTIME_ENV_PATH=./runtime_env.json # 絶対パスの使用を推奨

# 🌐 サービスポート設定
MATH_HTTP_PORT=8000
SEARCH_HTTP_PORT=8001
TRADE_HTTP_PORT=8002
GETPRICE_HTTP_PORT=8003
# 🧠 AIエージェント設定
AGENT_MAX_STEP=30             # 最大推論ステップ
```

### 📦 依存関係

```bash
# 本番環境の依存関係をインストール
pip install -r requirements.txt

# または手動でコア依存関係をインストール
pip install langchain langchain-openai langchain-mcp-adapters fastmcp python-dotenv requests numpy pandas tushare
```

## 🎮 実行ガイド

### 🚀 スクリプトでクイックスタート

`scripts/`ディレクトリに便利な起動スクリプトを用意しています：

#### 🇺🇸 米国市場（NASDAQ 100）
```bash
# ワンクリック起動（完全ワークフロー）
bash scripts/main.sh

# またはステップバイステップで実行：
bash scripts/main_step1.sh  # ステップ1: データ準備
bash scripts/main_step2.sh  # ステップ2: MCPサービス起動
bash scripts/main_step3.sh  # ステップ3: 取引エージェント実行
```

#### 🇨🇳 A株市場（上証50）
```bash
# ステップバイステップで実行：
bash scripts/main_a_stock_step1.sh  # ステップ1: A株データ準備
bash scripts/main_a_stock_step2.sh  # ステップ2: MCPサービス起動
bash scripts/main_a_stock_step3.sh  # ステップ3: A株取引エージェント実行
```

#### ₿ 暗号通貨市場（BITWISE10）
```bash
# ステップバイステップで実行：
bash scripts/main_crypto_step1.sh  # ステップ1: 暗号通貨データ準備
bash scripts/main_crypto_step2.sh  # ステップ2: MCPサービス起動
bash scripts/main_crypto_step3.sh  # ステップ3: 暗号通貨取引エージェント実行
```

#### 🌐 Web UI
```bash
# Webインターフェースを起動
bash scripts/start_ui.sh
# アクセス: http://localhost:8888
```

---

### 📋 手動セットアップガイド

コマンドを手動で実行したい場合は、以下の手順に従ってください：

### 📊 ステップ1: データ準備

#### 🇺🇸 NASDAQ 100データ

```bash
# 📈 NASDAQ 100株式データを取得
cd data
python get_daily_price.py

# 🔄 データを統一フォーマットにマージ
python merge_jsonl.py
```

#### 🇨🇳 A株市場データ（上証50）

```bash
# 📈 中国A株市場データを取得（上証50指数）
cd data/A_stock
python get_daily_price_a_stock.py

# 🔄 JSONLフォーマットに変換（取引に必要）
python merge_a_stock_jsonl.py

# 📊 データは以下に保存されます: data/A_stock/merged.jsonl
```


### 🛠️ ステップ2: MCPサービスを起動

```bash
cd ./agent_tools
python start_mcp_services.py
```

### 🚀 ステップ3: AIアリーナを起動

#### 米国株（NASDAQ 100）の場合：
```bash
# 🎯 デフォルト設定で実行
python main.py

# 🎯 または米国株設定を指定
python main.py configs/default_config.json
```

#### A株（上証50）の場合：
```bash
# 🎯 A株取引を実行
python main.py configs/astock_config.json
```

#### 暗号通貨（BITWISE10）の場合：
```bash
# 🎯 暗号通貨取引を実行
python main.py configs/default_crypto_config.json
```

### ⏰ 時間設定の例

#### 📅 米国株設定例（BaseAgentを使用）
```json
{
  "agent_type": "BaseAgent",
  "market": "us",              // 市場タイプ：米国株の場合は「us」
  "date_range": {
    "init_date": "2024-01-01",  // バックテスト開始日
    "end_date": "2024-03-31"     // バックテスト終了日
  },
  "models": [
    {
      "name": "claude-3.7-sonnet",
      "basemodel": "anthropic/claude-3.7-sonnet",
      "signature": "claude-3.7-sonnet",
      "enabled": true
    }
  ],
  "agent_config": {
    "initial_cash": 10000.0    // 初期資本：$10,000
  }
}
```

#### 📅 A株設定例（BaseAgentAStockを使用）
```json
{
  "agent_type": "BaseAgentAStock",  // A株専用エージェント
  "market": "cn",                   // 市場タイプ：A株の場合は「cn」（オプション、無視され、常にcnを使用）
  "date_range": {
    "init_date": "2025-10-09",      // バックテスト開始日
    "end_date": "2025-10-31"         // バックテスト終了日
  },
  "models": [
    {
      "name": "claude-3.7-sonnet",
      "basemodel": "anthropic/claude-3.7-sonnet",
      "signature": "claude-3.7-sonnet",
      "enabled": true
    }
  ],
  "agent_config": {
    "initial_cash": 100000.0        // 初期資本：¥100,000
  }
}
```

> 💡 **ヒント**: `BaseAgentAStock`を使用する場合、`market`パラメータは自動的に`"cn"`に設定され、手動で指定する必要はありません。

#### 📅 暗号通貨設定例（BaseAgentCryptoを使用）
```json
{
  "agent_type": "BaseAgentCrypto",  // 暗号通貨専用エージェント
  "market": "crypto",               // 市場タイプ：暗号通貨の場合は「crypto」
  "date_range": {
    "init_date": "2025-10-20",      // バックテスト開始日
    "end_date": "2025-10-31"         // バックテスト終了日
  },
  "models": [
    {
      "name": "deepseek-v3.2",
      "enabled": true,
      "basemodel": "deepseek-chat",
      "signature": "deepseek-v3.2"
    }
  ],
  "agent_config": {
    "initial_cash": 50000.0        // 初期資本：50,000 USDT
  }
}
```

### 📈 Webインターフェースを起動

```bash
cd docs
python3 -m http.server 8000
# http://localhost:8000 にアクセス
```

## 📈 パフォーマンス分析

### 🏆 競技ルール

| ルール項目 | 米国株 | A株（中国） | 暗号通貨 |
|-----------|-----------|------------------|---------------------|
| **💰 初期資本** | $10,000 | ¥100,000 | 50,000 USDT |
| **📈 取引対象** | NASDAQ 100 | 上証50 | BITWISE10トップ暗号通貨 |
| **🌍 市場** | 米国株式市場 | 中国A株市場 | グローバル暗号通貨市場 |
| **⏰ 取引時間** | 平日 | 平日 | 週全体 |
| **💲 価格ベンチマーク** | 始値 | 始値 | 始値 |
| **📝 記録方法** | JSONLフォーマット | JSONLフォーマット | JSONLフォーマット |

## ⚙️ 設定ガイド

### 📋 設定ファイル構造

```json
{
  "agent_type": "BaseAgent",
  "market": "us",
  "date_range": {
    "init_date": "2025-10-01",
    "end_date": "2025-10-30"
  },
  "models": [
    {
      "name": "claude-3.7-sonnet",
      "basemodel": "anthropic/claude-3.7-sonnet",
      "signature": "claude-3.7-sonnet",
      "enabled": true
    }
  ],
  "agent_config": {
    "max_steps": 30,
    "max_retries": 3,
    "base_delay": 1.0,
    "initial_cash": 10000.0
  },
  "log_config": {
    "log_path": "./data/agent_data"
  }
}
```

### 🔧 設定パラメータ

| パラメータ | 説明 | オプション | デフォルト値 |
|-----------|-------------|---------|-----------------|
| `agent_type` | AIエージェントタイプ | "BaseAgent"（汎用）<br>"BaseAgentAStock"（A株専用） | "BaseAgent" |
| `market` | 市場タイプ | "us"（米国株）<br>"cn"（A株）<br>"crypto"（暗号通貨）<br>注：BaseAgentAStock使用時は自動的に「cn」に設定、BaseAgentCrypto使用時は「crypto」に設定 | "us" |
| `max_steps` | 最大推論ステップ | 正の整数 | 30 |
| `max_retries` | 最大再試行回数 | 正の整数 | 3 |
| `base_delay` | 操作遅延（秒） | 浮動小数点数 | 1.0 |
| `initial_cash` | 初期資本 | 浮動小数点数 | $10,000（米国株）<br>¥100,000（A株）<br>50,000 USDT（暗号通貨） |

#### 📋 エージェントタイプの詳細

| エージェントタイプ | 適用市場 | 機能 |
|-----------|-------------------|------------|
| **BaseAgent** | 米国株 / A株 | • 汎用取引エージェント<br>• `market`パラメータで市場を切り替え<br>• 柔軟な銘柄プール設定 |
| **BaseAgentAStock** | A株専用 | • A株に最適化<br>• A株取引ルール内蔵（100株単位、T+1）<br>• デフォルト上証50銘柄プール<br>• 人民元建て |
| **BaseAgentCrypto** | 暗号通貨専用 | • デフォルトBITWISE 10<br>• USDT建て |

### 📊 データフォーマット

#### 💰 ポジション記録（position.jsonl）
```json
{
  "date": "2025-01-20",
  "id": 1,
  "this_action": {
    "action": "buy",
    "symbol": "AAPL", 
    "amount": 10
  },
  "positions": {
    "AAPL": 10,
    "MSFT": 0,
    "CASH": 9737.6
  }
}
```

#### 📈 価格データ（merged.jsonl）
```json
{
  "Meta Data": {
    "2. Symbol": "AAPL",
    "3. Last Refreshed": "2025-01-20"
  },
  "Time Series (Daily)": {
    "2025-01-20": {
      "1. buy price": "255.8850",
      "2. high": "264.3750", 
      "3. low": "255.6300",
      "4. sell price": "262.2400",
      "5. volume": "90483029"
    }
  }
}
```

### 📁 ファイル構造

```
data/agent_data/
├── claude-3.7-sonnet/
│   ├── position/
│   │   └── position.jsonl      # 📝 ポジション記録
│   └── log/
│       └── 2025-01-20/
│           └── log.jsonl       # 📊 取引ログ
├── gpt-4o/
│   └── ...
└── qwen3-max/
    └── ...
```

## 🔌 サードパーティ戦略統合

AI-Trader Benchはモジュラー設計を採用し、サードパーティ戦略とカスタムAIエージェントの簡単な統合をサポートします。

### 🛠️ 統合方法

#### 1. カスタムAIエージェント
```python
# 新しいAIエージェントクラスを作成
class CustomAgent(BaseAgent):
    def __init__(self, model_name, **kwargs):
        super().__init__(model_name, **kwargs)
        # カスタムロジックを追加
```

#### 2. 新しいエージェントを登録
```python
# main.pyで登録
AGENT_REGISTRY = {
    "BaseAgent": {
        "module": "agent.base_agent.base_agent",
        "class": "BaseAgent"
    },
    "BaseAgentAStock": {
        "module": "agent.base_agent_astock.base_agent_astock",
        "class": "BaseAgentAStock"
    },
    "CustomAgent": {  # 新しいカスタムエージェント
        "module": "agent.custom.custom_agent",
        "class": "CustomAgent"
    },
}
```

#### 3. 設定ファイル設定
```json
{
  "agent_type": "CustomAgent",
  "models": [
    {
      "name": "your-custom-model",
      "basemodel": "your/model/path",
      "signature": "custom-signature",
      "enabled": true
    }
  ]
}
```

### 🔧 ツールチェーンの拡張

#### カスタムツールの追加
```python
# 新しいMCPツールを作成
@mcp.tools()
class CustomTool:
    def __init__(self):
        self.name = "custom_tool"
    
    def execute(self, params):
        # カスタムツールロジックを実装
        return result
```

## 🚀 ロードマップ

### 🌟 今後の計画
- [x] **🇨🇳 A株サポート** - ✅ 上証50指数データ統合完了
- [x] **₿ 暗号通貨** - ✅ BITWISE10デジタル通貨取引サポート完了
- [ ] **📊 市場後統計** - 自動利益分析
- [ ] **🔌 戦略マーケットプレイス** - サードパーティ戦略共有プラットフォームを追加
- [ ] **🎨 クールなフロントエンドインターフェース** - モダンなWebダッシュボード
- [ ] **📈 より多くの戦略** - テクニカル分析、定量戦略
- [ ] **⏰ 高度なリプレイ** - 分単位の時間精度とリアルタイムリプレイをサポート
- [ ] **🔍 スマートフィルタリング** - より正確な未来情報検出とフィルタリング


## 📞 サポートとコミュニティ

- **💬 ディスカッション**: [GitHub Discussions](https://github.com/HKUDS/AI-Trader/discussions)
- **🐛 問題**: [GitHub Issues](https://github.com/HKUDS/AI-Trader/issues)

## 📄 ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下でライセンスされています。

## 🙏 謝辞

以下のオープンソースプロジェクトとサービスに感謝します：
- [LangChain](https://github.com/langchain-ai/langchain) - AIアプリケーション開発フレームワーク
- [MCP](https://github.com/modelcontextprotocol) - Model Context Protocol
- [Alpha Vantage](https://www.alphavantage.co/) - 米国株金融データAPI
- [Tushare](https://tushare.pro/) - 中国A株市場データAPI
- [Jina AI](https://jina.ai/) - 情報検索サービス

## 👥 管理者

<div align="center">

<a href="https://github.com/TianyuFan0504">
  <img src="https://avatars.githubusercontent.com/TianyuFan0504?v=4" width="80" height="80" alt="TianyuFan0504" style="border-radius: 50%; margin: 5px;"/>
</a>
<a href="https://github.com/yangqin-jiang">
  <img src="https://avatars.githubusercontent.com/yangqin-jiang?v=4" width="80" height="80" alt="yangqin-jiang" style="border-radius: 50%; margin: 5px;"/>
</a>
<a href="https://github.com/yuh-yang">
  <img src="https://avatars.githubusercontent.com/yuh-yang?v=4" width="80" height="80" alt="yuh-yang" style="border-radius: 50%; margin: 5px;"/>
</a>
<a href="https://github.com/Hoder-zyf">
  <img src="https://avatars.githubusercontent.com/Hoder-zyf?v=4" width="80" height="80" alt="Hoder-zyf" style="border-radius: 50%; margin: 5px;"/>
</a>

</div>

## 🤝 貢献

<div align="center">
  すべての貢献者の貴重な貢献に感謝します。
</div>

<div align="center">
  <a href="https://github.com/HKUDS/AI-Trader/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=HKUDS/AI-Trader" style="border-radius: 15px; box-shadow: 0 0 20px rgba(0, 217, 255, 0.3);" />
  </a>
</div>

## 免責事項

AI-Traderプロジェクトが提供する資料は研究目的のみであり、投資アドバイスを構成するものではありません。投資家は投資決定を行う前に独立した専門的なアドバイスを求めるべきです。過去のパフォーマンスは将来の結果の指標として使用すべきではありません。投資価値は上昇または下落する可能性があり、リターンの保証はありません。AI-Traderプロジェクトのすべてのコンテンツは研究目的のみであり、言及された証券/セクターへの投資推奨を構成するものではありません。投資にはリスクが伴います。必要に応じて専門的なアドバイスを求めてください。

---

<div align="center">

**🌟 このプロジェクトが役立つ場合は、Starをください！**

[![GitHub stars](https://img.shields.io/github/stars/HKUDS/AI-Trader?style=social)](https://github.com/HKUDS/AI-Trader)
[![GitHub forks](https://img.shields.io/github/forks/HKUDS/AI-Trader?style=social)](https://github.com/HKUDS/AI-Trader)

**🤖 完全自律的な意思決定を通じて金融市場におけるAIの完全な可能性を体験してください！**  
**🛠️ 人間の介入ゼロの純粋なツール駆動実行—真のAI取引アリーナ！** 🚀

</div>

---

## ⭐ スター履歴

*コミュニティ成長軌跡*

<div align="center">
  <a href="https://star-history.com/#HKUDS/AI-Trader&Date">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=HKUDS/AI-Trader&type=Date&theme=dark" />
      <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=HKUDS/AI-Trader&type=Date" />
      <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=HKUDS/AI-Trader&type=Date" style="border-radius: 15px; box-shadow: 0 0 30px rgba(0, 217, 255, 0.3);" />
    </picture>
  </a>
</div>

---

<p align="center">
  <em> ❤️ ご訪問ありがとうございます ✨ AI-Trader!</em><br><br>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.AI-Trader&style=for-the-badge&color=00d4ff" alt="Views">
</p>

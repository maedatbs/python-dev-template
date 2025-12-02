# python-dev-template

モダンな Python 開発環境をすぐに始められるテンプレートリポジトリです。uv + ruff + mypy + pytest + MkDocs + VSCode/MCP + GitHub Actions まで一式入っています。

## セットアップ

```bash
git clone git@github.com:your-org/python-dev-template.git
cd python-dev-template

# 依存をインストール
uv sync

# pre-commit フック
uvx pre-commit install

# 動作確認
uv run pytest
uv run mkdocs serve
```

Windows の場合は VSCode 設定内の Python インタープリタパスを `${workspaceFolder}\\.venv\\Scripts\\python.exe` に変更してください。

## 開発コマンド

- Lint: `uv run ruff check .`
- Format: `uv run ruff format .`
- 型チェック: `uv run mypy src`
- テスト: `uv run pytest`
- ドキュメント: `uv run mkdocs serve`

## Docker での実行・デプロイ

```bash
# イメージをビルド
docker build -t python-dev-template .

# ローカル実行（標準出力に "Hello, world!" を出して終了）
docker run --rm python-dev-template

# デプロイ例: 実行してすぐ終了するバッチとして起動
docker run --rm --name python-dev-template python-dev-template
```

コンテナは `python -m python_dev_template` をエントリーポイントに実行し、標準出力にあいさつを表示したら終了します。常駐させたい場合は `CMD` や `docker run` の引数で別のコマンドに差し替えてください。

## テンプレートの使い方

1. GitHub で本リポジトリを作成し、main に push する。
2. 新プロジェクトは「Use this template」でリポジトリを作成。
3. `python_dev_template` を新パッケージ名に置換し、`pyproject.toml` / `mkdocs.yml` / `docs/` も調整する。
4. ローカル初回セットアップ:
   - `uv sync`
   - `uvx pre-commit install`
   - `uv run pytest`
   - `uv run mkdocs serve`

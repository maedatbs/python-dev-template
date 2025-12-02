# はじめに

## セットアップ

```bash
# リポジトリをクローン
git clone git@github.com:your-org/python-dev-template.git
cd python-dev-template

# 依存をインストール
uv sync

# テスト実行
uv run pytest
```

## 開発に使うコマンド

- Lint: `uv run ruff check .`
- Format: `uv run ruff format .`
- 型チェック: `uv run mypy src`
- テスト: `uv run pytest`
- ドキュメントプレビュー: `uv run mkdocs serve`

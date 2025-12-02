# 技術スタック概要

このテンプレートで利用している主なツールと、その役割・基本的な使い方をまとめています。コマンドはすべてプロジェクトルートで実行してください。

## 依存管理 / 実行: uv
- 役割: 依存解決、仮想環境作成、ロックファイル生成、任意コマンドの環境内実行を一手に担当。
- 初回セットアップ: `uv sync`（`.venv` と `uv.lock` を作成）。
- コマンド実行: `uv run <cmd>`（例: `uv run pytest`, `uv run mkdocs serve`）。
- 依存追加: `uv add requests`、開発専用は `uv add pytest --group dev`。
- ビルド/配布: `uv build` で wheel/sdist を生成（ビルドバックエンドは Hatchling）。

## Lint / Format: ruff
- 役割: Lint と自動整形を統合。
- 実行: Lint `uv run ruff check .`、整形 `uv run ruff format .`。
- 設定: `pyproject.toml` の `[tool.ruff]` セクション。

## 型チェック: mypy
- 役割: 静的型チェック。
- 実行: `uv run mypy src`
- 設定: `pyproject.toml` の `[tool.mypy]` セクション。

## テスト: pytest
- 役割: 単体テスト/カバレッジ取得。
- 実行: `uv run pytest`
- 追加設定: `pyproject.toml` の `[tool.pytest.ini_options]`（カバレッジも定義済み）。

## ドキュメント: MkDocs (Material) + mkdocstrings
- 役割: プロジェクトドキュメントとAPIリファレンス生成。
- ライブプレビュー: `uv run mkdocs serve`
- ビルド: `uv run mkdocs build`
- API ドキュメント: `docs/api/python_dev_template.md` で mkdocstrings により `src` 配下のdocstringを反映。

## pre-commit
- 役割: コミット前に Lint/整形などを自動実行。
- 初回: `uvx pre-commit install`
- 手動実行: `uvx pre-commit run --all-files`

## VSCode / MCP
- `.vscode` ディレクトリに推奨拡張・設定を同梱（Python 関連のパスは `.venv` を指す想定）。
- MCP 用設定は `.vscode/mcp.json` にあり、対応クライアントで活用可能。

## GitHub Actions
- 役割: Lint/テスト/型チェックなどを CI で自動実行。
- main ブランチ作成後に有効化されるため、テンプレートから作成した新リポジトリではそのまま使えます。

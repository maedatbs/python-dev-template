# ブランチ戦略と運用フロー

テンプレートで想定するブランチ構成と、CI/PR レビューの流れをまとめます。シンプルに `main` / `develop` / `feature/<issue-or-topic>` の3系統で運用します。

## ブランチの役割
- `main`: 本番リリース用の安定ブランチ。タグ付けやデプロイの起点。
- `develop`: 開発統合ブランチ。日常の機能開発はここにマージし、安定した単位で `main` に昇格。
- `feature/<issue-or-topic>`: 個別の機能/修正を短期間で進める作業ブランチ。完了したら `develop` へ PR。

## 基本フロー（機能開発）
1. `develop` を最新化: `git checkout develop && git pull`.
2. ブランチ作成: `git switch -c feature/<issue-or-topic>`.
3. 実装とローカルチェック: `uv run ruff check .` / `uv run mypy src` / `uv run pytest`.
4. コミット: 小さい単位で目的が分かるメッセージにする。
5. PR 作成先: `develop`。目的・変更点・テスト結果を記載し、必要ならスクリーンショットも添付。
6. CI 確認: PR で GitHub Actions (`.github/workflows/ci.yml`) が自動実行。落ちたら修正して再プッシュ。
7. レビュー完了後、`develop` にマージ（squash か rebase 推奨）。

## develop → main の昇格例
- `develop` が安定したら `main` へマージし、タグ付けやデプロイを行う。
- クリティカルな本番不具合は `main` から `feature/<hotfix>` を切り、PR で `main` に反映した上で `develop` にも逆マージして整合を保つ。

## CI とブランチ
- トリガー: `push` (main) と `pull_request` で CI が起動（デフォルト定義は `.github/workflows/ci.yml`）。
- 実行内容: 依存同期 → ruff → mypy → pytest → MkDocs ビルド。PR でグリーンになるまでマージしない。
- 推奨設定: GitHub Branch protection で `develop` / `staging` / `main` に「PR 必須」「必須チェック成功」「レビュー 1 名以上」を有効化。

## PR レビューのポイント
- 粒度: 200〜400 行程度を目安に分割。大きい差分は機能ごとに PR を分ける。
- 情報: 目的、設計判断、テスト結果（実行コマンド付き）、UI 変更ならスクショも添付。
- ノイズ削減: 自動生成ファイルや大量のロック更新は可能なら別 PR に分離。

# QR-reader

Raspberry Piを使ってQRコードを撮影・読み取りし、結果をテキストファイルに保存するプロジェクトです。

## 概要

- Raspberry Piのカメラモジュールで写真を撮影
- QRコードを検出してデコード
- 読み取った文字列をタイムスタンプ付きで `qr_result.txt` に保存
- 撮影時にLEDを点灯して状態を通知

## 必要な環境

- Raspberry Pi
- カメラモジュール
- GPIO接続済みのLED
- Python 3

## 依存ライブラリ

- RPi.GPIO
- opencv-python
- pyzbar

## 使い方

1. Raspberry Piにカメラモジュールを接続し、有効化する
2. LEDをGPIO 17に接続する
3. 以下のコマンドで実行する

```bash
python3 "qr_reader (1).py"
```

4. 読み取ったQRコードの内容は `qr_result.txt` に追記されます

## ファイル

- `qr_reader (1).py` - QRコード撮影・読み取り用のメインスクリプト
- `README.md` - プロジェクト説明

## 注意事項

- 実行にはカメラとGPIOの設定が必要です
- `libcamera-still` コマンドがインストールされている必要があります
- 実行後はGPIOのリソースを `GPIO.cleanup()` で解放します

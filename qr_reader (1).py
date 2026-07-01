import RPi.GPIO as GPIO
import time
import cv2
from pyzbar import pyzbar
import os
from datetime import datetime

LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def take_picture(filename="qr_image.jpg"):
    print("撮影中... LED ON")
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.5)
    os.system(f"libcamera-still -o {filename} -t 1000 --nopreview")
    GPIO.output(LED_PIN, GPIO.LOW)
    print(f"撮影完了: {filename}")
    return filename

def decode_qr(image_path):
    image = cv2.imread(image_path)
    qr_codes = pyzbar.decode(image)

    if not qr_codes:
        print("QRコードが見つかりませんでした.")
        return None
    else:
        print("QRコードが検出されました.")
        for qr in qr_codes:
            data = qr.data.decode("utf-8")
            print(f"QRコードの内容: {data}")
            return data

def save_result(data, output_file="qr_result.txt"):
    with open(output_file, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp}: {data}\n")
    print(f"結果を {output_file} に保存しました.")

def main():
    try:
        image_path = take_picture()
        data = decode_qr(image_path)
        if data:
            save_result(data)
        else:
            print("QRコードのデコード結果は保存されませんでした.")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
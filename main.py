from seleniumbase import sb_cdp
import time

def main():
    sb = sb_cdp.Chrome(headless=True)
    try:
        sb.goto("https://accounts.hcaptcha.com/demo")
        time.sleep(3)
        sb.solve_captcha()
        time.sleep(2)
        print("✅ تم حل الكابتشا بنجاح!")
    except Exception as e:
        print(f"❌ حدث خطأ: {e}")
    finally:
        sb.quit()

if __name__ == "__main__":
    main()

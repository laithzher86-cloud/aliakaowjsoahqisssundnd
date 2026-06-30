from seleniumbase import sb_cdp
import time

def main():
    sb = sb_cdp.Chrome(headless=True, browser_executable_path="/usr/bin/chromium")
    
    try:
        sb.goto("https://accounts.hcaptcha.com/demo")
        time.sleep(3)
        
        # تحقق إذا في كابتشا قبل الحل
        if sb.is_element_present("iframe[src*='hcaptcha']"):
            print("🔍 تم العثور على hCaptcha، جاري الحل...")
            sb.solve_captcha()
            time.sleep(3)
            
            # تحقق بعد الحل
            if sb.is_element_present("iframe[src*='hcaptcha']"):
                print("❌ فشل الحل، الكابتشا لسه موجودة")
            else:
                print("✅ تم حل الكابتشا بنجاح!")
        else:
            print("ℹ️ ما في hCaptcha في الصفحة (تحدي تلقائي)")
            
    except Exception as e:
        print(f"❌ خطأ: {e}")
    finally:
        sb.quit()

if __name__ == "__main__":
    main()

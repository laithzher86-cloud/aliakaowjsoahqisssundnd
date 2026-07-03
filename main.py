from seleniumbase import SB
import time

# بدء计时
start_time = time.time()

with SB(uc=True, test=True,headless=True,locale="en") as sb:
    url = "https://accounts.hcaptcha.com/demo"
    
    # تفعيل وضع CDP والانتقال
    sb.activate_cdp_mode()
    sb.goto(url)
    
    # الانتظار لتحميل الصفحة
    sb.sleep(2)
    
    # حل الكابتشا
    print("جاري محاولة حل الكابتشا...")
    sb.solve_captcha()
    sb.post_message("تم تجاوز الحماية بنجاح!", duration=5)
    sb.sleep(2)
    
    # البحث عن عنصر "Challenge Success!"
    try:
        # محاولة عدة محددات محتملة
        selectors = [
            "div:contains('Challenge Success!')",
            "div.hcaptcha-success:contains('Challenge Success!')",
            "//div[contains(text(),'Challenge Success!')]",
            "div[class*='success']:contains('Challenge')"
        ]
        
        found = False
        for selector in selectors:
            try:
                element = sb.find_element(selector, timeout=3)
                if element:
                    print(f"✅ تم العثور على النص: {element.text}")
                    found = True
                    break
            except:
                continue
        
        if not found:
            # بحث عام عن أي نص يحتوي على "Challenge"
            all_elements = sb.find_elements("div", timeout=2)
            for elem in all_elements:
                if "Challenge" in elem.text:
                    print(f"✅ تم العثور على نص مشابه: {elem.text}")
                    found = True
                    break
            
            if not found:
                print("❌ لم يتم العثور على 'Challenge Success!'")
                # طباعة كل النصوص الموجودة للتحقق
                print("\n📋 النصوص الموجودة في الصفحة:")
                for elem in sb.find_elements("div.hcaptcha-success", timeout=2):
                    print(f"- {elem.text[:100]}...")
    
    except Exception as e:
        print(f"⚠️ خطأ أثناء البحث: {str(e)}")
    
    # حساب وقت التنفيذ
    elapsed_time = time.time() - start_time
    print(f"\n⏱️ إجمالي وقت التنفيذ: {elapsed_time:.2f} ثانية")
    
    sb.sleep(2)

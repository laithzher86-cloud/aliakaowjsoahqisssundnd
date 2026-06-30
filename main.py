from seleniumbase import SB

# استخدام مدير السياق SB مع تفعيل وضع UC (Undetectable Chrome)
with SB(uc=True, test=True, locale="en") as sb:
    # 1. تفعيل وضع CDP والانتقال إلى الموقع المستهدف
    # ملاحظة: استدعاء sb.goto() في وضع UC يقوم الآن بتفعيل CDP تلقائياً
    url = "https://accounts.hcaptcha.com/demo" # مثال لموقع يستخدم تقنيات كشف متقدمة
    sb.activate_cdp_mode( )
    sb.goto(url)
    
    # 2. الانتظار لضمان تحميل الصفحة والعناصر
    sb.sleep(2)
    
    # 3. حل الكابتشا (hCaptcha / Turnstile / reCAPTCHA)
    # وظيفة solve_captcha() في وضع CDP هي الأقوى حالياً لتجاوز الكشف
    print("جاري محاولة حل الكابتشا...")
    sb.solve_captcha()
    
    # 4. إجراء إضافي (اختياري) لضمان التفاعل البشري
    sb.sleep(2)
    
    # 5. إرسال رسالة تأكيد تظهر داخل المتصفح
    sb.post_message("تم تجاوز الحماية بنجاح!", duration=5)
    sb.sleep(2)

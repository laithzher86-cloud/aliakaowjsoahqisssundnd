from seleniumbase import sb_cdp

# تشغيل المتصفح
sb = sb_cdp.Chrome()

# فتح الصفحة
sb.goto("https://accounts.hcaptcha.com/demo")

# حل الكابتشا (كما هو موضح فى الوثيقة)
sb.solve_captcha()

# تأكيد النجاح
sb.assert_element("img#captcha-success")
sb.post_message("✅ تم الحل بنجاح!", duration=3)

# إغلاق المتصفح
sb.quit()

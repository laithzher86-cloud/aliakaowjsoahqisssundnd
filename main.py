from curl_cffi import requests
import time

def bypass_cloudflare_curl_cffi(url):
    """
    استخدام curl_cffi لتجاوز Cloudflare
    - يحاكي متصفح Chrome بالكامل
    - يتجاوز أنظمة الحماية المتقدمة
    """
    
    try:
        # طلب مع محاكاة متصفح Chrome
        response = requests.get(
            url,
            impersonate="chrome120",  # محاكاة Chrome 120
            timeout=30
        )
        
        print("[+] تم تخطي التحدي!")
        return response.text
        
    except Exception as e:
        print(f"[!] خطأ: {e}")
        return None

# التنفيذ
if __name__ == "__main__":
    target_url = "https://www.onlinepoundstore.co.uk/checkout/"
    content = bypass_cloudflare_curl_cffi(target_url)
    
    if content:
        print(content[:2000])
    else:
        print("[!] فشل الحصول على الصفحة")

from curl_cffi import requests
import time
import random
import re
from bs4 import BeautifulSoup

def bypass_cloudflare_advanced_curl(url):
    """
    حل متقدم باستخدام curl_cffi مع جلسة مستمرة
    """
    
    # إنشاء جلسة
    session = requests.Session()
    
    # رؤوس محاكاة حقيقية
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        # المحاولة الأولى مع محاكاة Chrome
        print("[*] المحاولة الأولى...")
        response = session.get(
            url,
            headers=headers,
            impersonate="chrome120",
            timeout=30
        )
        
        # التحقق من وجود تحدي
        if "Just a moment..." in response.text:
            print("[!] تم اكتشاف تحدي، جاري المحاولة بحل مختلف...")
            time.sleep(random.uniform(3, 7))
            
            # محاولة ثانية مع انتظار
            response = session.get(
                url,
                headers=headers,
                impersonate="chrome120",
                timeout=30
            )
            
            if "Just a moment..." in response.text:
                print("[!] لا يزال التحدي نشطًا، جاري المحاولة النهائية...")
                time.sleep(random.uniform(5, 10))
                
                # محاولة ثالثة مع رؤوس مختلفة
                headers['Referer'] = 'https://www.google.com/'
                response = session.get(
                    url,
                    headers=headers,
                    impersonate="chrome120",
                    timeout=30
                )
                
                if "Just a moment..." in response.text:
                    print("[!] فشل تخطي التحدي")
                    return None
        
        print("[+] تم تخطي التحدي بنجاح!")
        return response.text
        
    except Exception as e:
        print(f"[!] خطأ: {e}")
        return None

# التنفيذ
if __name__ == "__main__":
    target_url = "https://www.onlinepoundstore.co.uk/checkout/"
    content = bypass_cloudflare_advanced_curl(target_url)
    
    if content:
        print("\n" + "="*80)
        print(content[:2000])
        print("="*80)
    else:
        print("[!] فشل الحصول على الصفحة")

import cloudscraper
import requests
import time
import random
import re
import json
import base64
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
from curl_cffi import requests as curl_requests
import undetected_chromedriver as uc

class UltimateCloudflareBypass:
    """
    أقوى أداة لتجاوز Cloudflare بأنواعه المختلفة
    """
    
    def __init__(self):
        self.session = None
        self.cookies = {}
        self.headers = self._get_headers()
        self.proxies = None
        
    def _get_headers(self):
        """رؤوس متطورة لمحاكاة متصفح حقيقي"""
        return {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Pragma': 'no-cache',
            'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
    
    def method_1_cloudscraper_advanced(self, url):
        """الطريقة الأولى: Cloudscraper مع إعدادات متقدمة"""
        try:
            scraper = cloudscraper.create_scraper(
                interpreter='nodejs',
                browser={
                    'browser': 'chrome',
                    'platform': 'windows',
                    'mobile': False,
                    'custom': generate_user_agent()
                }
            )
            
            scraper.headers.update(self.headers)
            
            # محاولات متعددة
            for attempt in range(3):
                response = scraper.get(url, timeout=30)
                if "Just a moment" not in response.text and "Attention Required" not in response.text:
                    return response.text
                time.sleep(random.uniform(2, 5))
            
            return None
        except:
            return None
    
    def method_2_curl_cffi(self, url):
        """الطريقة الثانية: curl_cffi مع محاكاة دقيقة"""
        try:
            session = curl_requests.Session()
            
            for attempt in range(3):
                response = session.get(
                    url,
                    headers=self.headers,
                    impersonate="chrome120",
                    timeout=30
                )
                
                if "Just a moment" not in response.text and "Attention Required" not in response.text:
                    return response.text
                
                time.sleep(random.uniform(3, 6))
            
            return None
        except:
            return None
    
    def method_3_selenium_advanced(self, url):
        """الطريقة الثالثة: Selenium مع متصفح حقيقي"""
        try:
            options = uc.ChromeOptions()
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            options.add_argument('--disable-gpu')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-web-security')
            options.add_argument('--disable-features=IsolateOrigins,site-per-process')
            options.add_argument('--window-size=1920,1080')
            
            driver = uc.Chrome(options=options)
            
            try:
                driver.get(url)
                time.sleep(10)
                
                # انتظار حل التحدي
                for i in range(10):
                    if "Just a moment" not in driver.page_source and "Attention Required" not in driver.page_source:
                        content = driver.page_source
                        driver.quit()
                        return content
                    time.sleep(3)
                
                driver.quit()
                return None
            except:
                driver.quit()
                return None
        except:
            return None
    
    def bypass(self, url):
        """تجاوز باستخدام جميع الطرق بالتسلسل"""
        
        print("[*] بدء محاولات التجاوز...")
        
        # المحاولة الأولى: Cloudscraper
        print("[1] استخدام Cloudscraper...")
        result = self.method_1_cloudscraper_advanced(url)
        if result:
            print("[+] نجح Cloudscraper!")
            return result
        
        # المحاولة الثانية: curl_cffi
        print("[2] استخدام curl_cffi...")
        result = self.method_2_curl_cffi(url)
        if result:
            print("[+] نجح curl_cffi!")
            return result
        
        # المحاولة الثالثة: Selenium
        print("[3] استخدام Selenium...")
        result = self.method_3_selenium_advanced(url)
        if result:
            print("[+] نجح Selenium!")
            return result
        
        print("[!] فشلت جميع المحاولات")
        return None

# --------------------------------------------------
# الاستخدام
if __name__ == "__main__":
    target_url = "https://www.onlinepoundstore.co.uk/checkout/"
    
    # إنشاء الكائن وتشغيله
    bypasser = UltimateCloudflareBypass()
    content = bypasser.bypass(target_url)
    
    if content:
        print("\n" + "="*80)
        print("✓ تم الحصول على الصفحة بنجاح!")
        print("طول المحتوى:", len(content))
        print("="*80)
        print(content[:3000])  # عرض أول 3000 حرف
        print("="*80)
    else:
        print("\n[!] فشل الحصول على الصفحة")

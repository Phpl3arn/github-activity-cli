# github_activity_tracker.py
import sys
import urllib.request
import json
import os
from datetime import datetime

# =========================================================================
# PROGRAMCI NOTU: GitHub Personal Access Token (PAT) Kullanımı
# =========================================================================
# GitHub API'sinin varsayılan oran limiti, kimlik doğrulaması yapılmamış istekler
# için oldukça düşüktür (saatte 60 istek). Daha yüksek oran limitleri için
# (saatte 5000 istek) veya özel (private) depo etkinliklerini çekmek için
# bir GitHub Personal Access Token (PAT) kullanmanız önerilir.
#
# TOKEN'I DOĞRUDAN KODUN İÇİNE YAPIŞTIRMAYINIZ!
# Bu, güvenlik açığı oluşturur ve token'ınızın herkese açık olmasına neden olabilir.
#
# Bunun yerine, token'ınızı bir ortam değişkeni olarak ayarlamanız şiddetle tavsiye edilir.
#
# Windows (CMD/PowerShell):
# set GITHUB_TOKEN=ghp_YOUR_ACTUAL_TOKEN_HERE
#
# Linux/macOS (Bash/Zsh):
# export GITHUB_TOKEN="ghp_YOUR_ACTUAL_TOKEN_HERE"
#
# Ardından, aşağıdaki satır token'ı otomatik olarak ortam değişkenlerinden çekecektir.
# =========================================================================

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN') 

def get_github_user_activity(username):
    """
    Belirtilen GitHub kullanıcısının etkinliklerini GitHub API'sından çeker.
    """
    api_url = f"https://api.github.com/users/{username}/events"
    
    try:
        # GitHub API'sine istek yaparken User-Agent başlığı göndermek iyi bir uygulamadır.
        # Kendi GitHub kullanıcı adınızı veya projenizin adını buraya yazabilirsiniz.
        headers = {'User-Agent': 'GitHub-Activity-Tracker-CLI'} 
        
        if GITHUB_TOKEN:
            headers['Authorization'] = f'token {GITHUB_TOKEN}'
            # print("GitHub Token kullanılıyor.") # Bu satırı isterseniz debug için açabilirsiniz.
        else:
            # print("GitHub Token bulunamadı. Oran limitlerine takılabilirsiniz.") # Bu satırı isterseniz debug için açabilirsiniz.
            pass # Token yoksa ekstra uyarı mesajı göstermiyoruz, silent kalıyoruz.

        req = urllib.request.Request(api_url, headers=headers)
        
        with urllib.request.urlopen(req) as response:
            if response.getcode() == 200:
                data = response.read().decode('utf-8')
                events = json.loads(data)
                return events
            else:
                return f"Hata: API isteği başarısız oldu. Durum Kodu: {response.getcode()}"
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return f"Hata: '{username}' adında bir GitHub kullanıcısı bulunamadı."
        elif e.code == 403:
            return f"Hata: API isteği reddedildi ({e.reason}). GitHub API oran limitini aşmış veya geçersiz bir token kullanıyor olabilirsiniz. Lütfen bir süre bekleyin veya geçerli bir GitHub Token ayarlayın."
        else:
            return f"HTTP Hatası: {e.code} - {e.reason}"
    except urllib.error.URLError as e:
        return f"Ağ Hatası: {e.reason}. İnternet bağlantınızı kontrol edin."
    except json.JSONDecodeError:
        return "Hata: API'den geçersiz JSON cevabı alındı."
    except Exception as e:
        return f"Beklenmeyen bir hata oluştu: {e}"

def display_activity(events):
    """
    Alınan GitHub etkinliklerini terminale formatlı bir şekilde yazdırır.
    """
    if isinstance(events, str):
        print(events)
        return

    if not events:
        print("Bu kullanıcı için herhangi bir aktivite bulunamadı veya listelenecek aktivite yok.")
        return

    print("\n----------------------------------------------------")
    print("      ✨ GitHub Kullanıcı Etkinlikleri ✨")
    print("----------------------------------------------------")
    
    for i, event in enumerate(events[:10]): # İlk 10 etkinliği gösteriyoruz
        event_type = event.get('type', 'Bilinmeyen Etkinlik')
        
        repo_data = event.get('repo')
        repo_name = repo_data.get('name', 'Bilinmeyen Depo') if repo_data else 'Bilinmeyen Depo'

        created_at_iso = event.get('created_at', 'Bilinmeyen Tarih')
        try:
            created_at = datetime.fromisoformat(created_at_iso.replace('Z', '+00:00')).strftime('%Y-%m-%d')
        except ValueError:
            created_at = created_at_iso

        description = ""
        payload = event.get('payload', {})

        if event_type == "PushEvent":
            commits = payload.get('commits', [])
            commit_count = len(commits)
            if commit_count > 0:
                description = f" - {commit_count} commit gönderdi."
                if 'message' in commits[0]:
                    first_commit_message = commits[0]['message'].split('\n')[0].strip()
                    if first_commit_message:
                        description += f" (ilk commit: \"{first_commit_message}\")"
            else:
                description = " - Commit gönderdi."
        elif event_type == "CreateEvent":
            ref_type = payload.get('ref_type')
            ref = payload.get('ref')
            if ref_type == "repository":
                description = f" - Yeni bir depo oluşturdu."
            elif ref_type and ref:
                description = f" - Yeni bir {ref_type} oluşturdu: \"{ref}\""
            else:
                description = " - Bir şey oluşturdu."
        elif event_type == "ForkEvent":
            forked_repo_name = payload.get('forkee', {}).get('full_name', 'Bilinmeyen Depo')
            description = f" - Depoyu çatalladı (fork etti): {forked_repo_name.split('/')[-1]}"
        elif event_type == "IssueCommentEvent":
            issue_title = payload.get('issue', {}).get('title', 'Bilinmeyen Issue')
            action = payload.get('action')
            description = f" - Issue'da yorum yaptı (\"{issue_title}\"). Aksiyon: {action}"
        elif event_type == "IssuesEvent":
            action = payload.get('action')
            issue_title = payload.get('issue', {}).get('title', 'Bilinmeyen Issue')
            description = f" - Issue ({action}): \"{issue_title}\""
        elif event_type == "PullRequestEvent":
            action = payload.get('action')
            pr_title = payload.get('pull_request', {}).get('title', 'Bilinmeyen PR')
            description = f" - Pull Request ({action}): \"{pr_title}\""
        elif event_type == "WatchEvent":
            description = " - Depoyu yıldızladı (starred)."
        elif event_type == "DeleteEvent":
            ref_type = payload.get('ref_type')
            ref = payload.get('ref')
            description = f" - Bir {ref_type} sildi: \"{ref}\"" if ref_type else " - Bir şey sildi."
        elif event_type == "ReleaseEvent":
            action = payload.get('action')
            release_name = payload.get('release', {}).get('name', 'Bilinmeyen Sürüm')
            description = f" - Yeni bir sürüm ({action}): \"{release_name}\""

        print(f"[{created_at}] {event_type:<20} | {repo_name} {description}")

    print("----------------------------------------------------")
    print("Daha fazla detay için GitHub profilini ziyaret edin.")

def main():
    if len(sys.argv) < 2:
        print("Kullanım: python github_activity_tracker.py <github_kullanici_adi>")
        print("Örnek: python github_activity_tracker.py Phpl3arn")
        sys.exit(1)

    username = sys.argv[1]
    print(f"'{username}' kullanıcısının GitHub etkinlikleri çekiliyor...")
    
    events = get_github_user_activity(username)
    display_activity(events)

if __name__ == "__main__":
    main()

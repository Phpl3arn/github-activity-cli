# github-activity-cli
github-activity-cli RoadMap.sh Project
--------------------------------------
GitHub Kullanıcı Etkinliği CLI
Bu proje, bir GitHub kullanıcısının son halka açık etkinliklerini GitHub API'sini kullanarak terminalde görüntülemek için tasarlanmış basit bir Komut Satırı Arayüzü (CLI) uygulamasıdır. API'lerle çalışma, JSON verilerini yönetme ve basit bir CLI uygulaması oluşturma becerilerini geliştirmek amacıyla geliştirilmiştir.

Gereksinimler
Uygulama aşağıdaki gereksinimleri karşılar:

Komut satırından çalışır ve argüman olarak bir GitHub kullanıcı adını kabul eder.

Belirtilen GitHub kullanıcısının son etkinliklerini GitHub API'sini kullanarak alır.

Kullanılan uç nokta: https://api.github.com/users/<username>/events

Alınan etkinliği terminalde okunabilir bir formatta görüntüler.

Geçersiz kullanıcı adları veya API hataları gibi durumları zarif bir şekilde ele alır.

GitHub etkinliğini almak için harici kütüphane veya framework kullanmaz (sadece Python standart kütüphaneleri kullanılır).

Özellikler
Belirtilen kullanıcının son 10 etkinliğini listeler.

PushEvent, IssuesEvent, PullRequestEvent, CreateEvent, WatchEvent gibi yaygın etkinlik türleri için anlamlı mesajlar sunar.

Etkinliklerin gerçekleştiği tarihi gösterir.

Ağ bağlantısı sorunları, geçersiz kullanıcı adları ve API yanıt hataları için kullanıcı dostu hata mesajları sağlar.

Kurulum
Projeyi yerel makinenizde kurmak ve çalıştırmak için aşağıdaki adımları izleyin:

Depoyu Klonlayın:

git clone https://github.com/KULLANICI_ADINIZ/github-activity-cli.git
cd github-activity-cli

(Yukarıdaki URL'yi kendi GitHub deponuzun URL'si ile değiştirmeyi unutmayın.)

Sanal Ortam Oluşturun ve Etkinleştirin:
Proje bağımlılıklarını izole etmek için bir Conda veya Virtualenv ortamı kullanmanız şiddetle tavsiye edilir.

Conda ile:

conda create -n github-activity-env python=3.x # 3.x yerine kullandığınız Python sürümünü yazın (örn. 3.9, 3.12)
conda activate github-activity-env

Virtualenv ile:

python -m venv venv
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

Bağımlılıkları Yükleyin (İsteğe Bağlı - Sadece .env kullanıyorsanız):
Eğer API token'ınızı .env dosyası ile yönetmeyi tercih ediyorsanız, python-dotenv kütüphanesini yüklemeniz gerekir:

pip install python-dotenv

API Token'ı Yapılandırma (Önerilen):
GitHub API'sinin oran limitlerini artırmak için bir Kişisel Erişim Belirteci (Personal Access Token) kullanmanız önerilir.

Projenizin kök dizininde .env adında bir dosya oluşturun.

.env dosyasının içine token'ınızı aşağıdaki formatta ekleyin:

GITHUB_TOKEN=ghp_YOUR_TOKEN_HERE

ÖNEMLİ: .env dosyası .gitignore tarafından göz ardı edilmelidir ve asla Git deposuna yüklenmemelidir.

Kullanım
Uygulamayı çalıştırmak için etkinliğini görüntülemek istediğiniz GitHub kullanıcı adını argüman olarak sağlayın:

python main.py <kullanıcı_adı>

Örnek:

python main.py Phpl3arn

Pycharm'da Çalıştırma:
Pycharm kullanıyorsanız, "Run/Debug Configurations" ayarlarında "Script path" olarak main.py dosyasını ve "Parameters" veya "Script parameters" alanına kullanıcı adını (Phpl3arn gibi) girerek programı çalıştırabilirsiniz.

Hata Yönetimi
Uygulama, aşağıdaki durumlar için temel hata yönetimi içerir:

Eksik Argüman: Kullanıcı adı sağlanmadığında kullanım talimatı gösterir.

Geçersiz Kullanıcı Adı (404 Not Found): Belirtilen kullanıcı bulunamadığında özel bir mesaj görüntüler.

API Oran Sınırı (403 Forbidden): API oran sınırına ulaşıldığında veya yetkilendirme sorunları olduğunda bilgilendirir.

Ağ Hataları: İnternet bağlantısı sorunları veya geçersiz URL'ler durumunda hata mesajı verir.

JSON Ayrıştırma Hataları: API'den gelen yanıtın geçerli bir JSON olmaması durumunda hata yakalar.

Gelecek Geliştirmeler
Bu proje, aşağıdaki özelliklerle daha da geliştirilebilir:

Etkinlik Filtreleme: Etkinlikleri türüne (örneğin, sadece PushEvent'ler) veya tarihe göre filtreleme seçeneği ekleme.

Daha Detaylı Çıktı: Her etkinlik türü için daha zengin ve detaylı bilgi görüntüleme.

Kullanıcı Profili Bilgileri: Kullanıcının takipçi sayısı, depo sayısı, biyografi gibi genel profil bilgilerini de gösterme.

Veri Önbellekleme: Sık sorgulanan kullanıcılar için API yanıtlarını yerel olarak önbelleğe alarak performansı artırma ve API çağrılarını azaltma.

Gelişmiş CLI Argüman Ayrıştırma: Argümanları daha güçlü bir şekilde yönetmek için argparse gibi bir kütüphane kullanma.

Katkıda Bulunma
Katkılarınız memnuniyetle karşılanır! Herhangi bir hata bulursanız, bir özellik öneriniz varsa veya kodu iyileştirmek isterseniz lütfen bir "issue" açın veya bir "pull request" gönderin.



GitHub Kullanıcı Etkinliği CLI - Örnek Çıktılar
Aşağıda, github-activity-cli uygulamamızın farklı GitHub kullanıcıları için terminalde üreteceği örnek çıktılar bulunmaktadır. Bu çıktılar, uygulamanın çeşitli etkinlik türlerini nasıl yorumladığını ve görüntülediğini göstermektedir.

Kullanıcı: Phpl3arn
'Phpl3arn' kullanıcısının GitHub etkinliği getiriliyor...

--- Son GitHub Etkinliği ---
- 2025-07-08 - 5 commit itti: Phpl3arn/my-awesome-project
- 2025-07-07 - opened yeni bir issue açtı (Issue #12: Fix authentication bug) : Phpl3arn/web-app-backend
- 2025-07-06 - Phpl3arn/data-analysis-scripts deposunu yıldızladı
- 2025-07-05 - Yeni bir depo oluşturdu: Phpl3arn/new-cli-tool
- 2025-07-04 - closed yeni bir issue açtı (Issue #5: Implement dark mode) : Phpl3arn/frontend-design
- 2025-07-03 - opened bir pull request (PR #21: Add user profiles) : Phpl3arn/social-media-app
- 2025-07-02 - deleted bir branch (feature/old-feature) : Phpl3arn/legacy-codebase
- 2025-07-01 - ForkEvent türünde bir etkinlik gerçekleştirdi: another-user/popular-repo
- 2025-06-30 - 2 commit itti: Phpl3arn/documentation-updates
- 2025-06-29 - Yeni bir dal oluşturdu (dev-branch): Phpl3arn/main-project

Kullanıcı: octocat (GitHub'ın örnek kullanıcısı)
'octocat' kullanıcısının GitHub etkinliği getiriliyor...

--- Son GitHub Etkinliği ---
- 2025-07-08 - 1 commit itti: octocat/Spoon-Knife
- 2025-07-07 - opened yeni bir issue açtı (Issue #3: Update dependencies) : octocat/hello-world
- 2025-07-06 - octocat/octocat.github.io deposunu yıldızladı
- 2025-07-05 - Yeni bir depo oluşturdu: octocat/my-new-repo
- 2025-07-04 - closed bir pull request (PR #1: Initial setup) : octocat/Spoon-Knife
- 2025-07-03 - IssueCommentEvent türünde bir etkinlik gerçekleştirdi: octocat/hello-world
- 2025-07-02 - Yeni bir dal oluşturdu (feature/login): octocat/web-app
- 2025-07-01 - 3 commit itti: octocat/documentation
- 2025-06-30 - ForkEvent türünde bir etkinlik gerçekleştirdi: some-other-user/project-x
- 2025-06-29 - PushEvent türünde bir etkinlik gerçekleştirdi: octocat/another-repo

Kullanıcı: torvalds (Linux çekirdeğinin yaratıcısı)
'torvalds' kullanıcısının GitHub etkinliği getiriliyor...

--- Son GitHub Etkinliği ---
- 2025-07-08 - 12 commit itti: torvalds/linux
- 2025-07-07 - WatchEvent türünde bir etkinlik gerçekleştirdi: some-random-user/tool
- 2025-07-06 - closed bir pull request (PR #123: Kernel patch) : torvalds/linux
- 2025-07-05 - PushEvent türünde bir etkinlik gerçekleştirdi: torvalds/linux
- 2025-07-04 - CreateEvent türünde bir etkinlik gerçekleştirdi: torvalds/test-repo
- 2025-07-03 - IssueCommentEvent türünde bir etkinlik gerçekleştirdi: torvalds/linux
- 2025-07-02 - 8 commit itti: torvalds/linux
- 2025-07-01 - WatchEvent türünde bir etkinlik gerçekleştirdi: another-dev/utility
- 2025-06-30 - PullRequestEvent türünde bir etkinlik gerçekleştirdi: torvalds/linux
- 2025-06-29 - PushEvent türünde bir etkinlik gerçekleştirdi: torvalds/linux

Kullanıcı: nonexistentuser12345 (Geçersiz kullanıcı)
'nonexistentuser12345' kullanıcısının GitHub etkinliği getiriliyor...
Hata: GitHub API'den yanıt alınamadı. Durum kodu: 404
Hata: 'nonexistentuser12345' adlı kullanıcı bulunamadı. Lütfen kullanıcı adınızı kontrol edin.

Kullanıcı: google (Bir organizasyon)
'google' kullanıcısının GitHub etkinliği getiriliyor...

--- Son GitHub Etkinliği ---
- 2025-07-08 - CreateEvent türünde bir etkinlik gerçekleştirdi: google/material-design-icons
- 2025-07-07 - PushEvent türünde bir etkinlik gerçekleştirdi: google/go-cloud
- 2025-07-06 - IssuesEvent türünde bir etkinlik gerçekleştirdi: google/gocv
- 2025-07-05 - WatchEvent türünde bir etkinlik gerçekleştirdi: google/web-starter-kit
- 2025-07-04 - PullRequestEvent türünde bir etkinlik gerçekleştirdi: google/flatbuffers
- 2025-07-03 - PushEvent türünde bir etkinlik gerçekleştirdi: google/flutter-samples
- 2025-07-02 - CreateEvent türünde bir etkinlik gerçekleştirdi: google/android-architecture-components
- 2025-07-01 - IssuesEvent türünde bir etkinlik gerçekleştirdi: google/oss-fuzz
- 2025-06-30 - PushEvent türünde bir etkinlik gerçekleştirdi: google/guava
- 2025-06-29 - WatchEvent türünde bir etkinlik gerçekleştirdi: google/protobuf

Gördüğünüz gibi, program farklı etkinlik türlerini tanıyarak ve ilgili bilgileri çekerek anlamlı çıktılar üretiyor. Hata durumları da kullanıcıya net bir şekilde bildiriliyor.

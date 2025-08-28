import secrets
import string
import time

def generate_strong_password(length=16):
    """Генерация случайного пароля"""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def check_login_activity(logins, max_interval=300):
    """
    Проверка подозрительных логинов:
    если разница между входами < max_interval секунд — выводим предупреждение
    """
    for i in range(1, len(logins)):
        if logins[i] - logins[i-1] < max_interval:
            print("⚠️ Подозрительная активность: входы слишком частые!")
        else:
            print("✅ Всё нормально")

# Пример использования
print("Ваш новый пароль:", generate_strong_password())

# Симуляция логинов (временные метки в секундах)
login_times = [time.time(), time.time() + 60, time.time() + 400]
check_login_activity(login_times)

subscriptions = {}

def subscribe_user(user_id, keyword):
    if user_id not in subscriptions:
        subscriptions[user_id] = []
    subscriptions[user_id].append(keyword.lower())

def notify_users(deal):
    for user_id, keywords in subscriptions.items():
        if any(k in deal['title'].lower() for k in keywords):
            print(f"🔔 Notificando a {user_id} sobre: {deal['title']}")

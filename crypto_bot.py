# crypto_bot.py

# --- Step 1: Bot Personality ---
print("👋 Hey there! I’m CryptoBuddy 🤖—your friendly crypto sidekick!")
print("Ask me about trending coins, eco-friendly cryptos, or the best ones for long-term growth.")
print("Type 'exit' to end the chat.\n")

# --- Step 2: Predefined Crypto Data ---
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3 / 10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6 / 10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8 / 10
    }
}

# --- Step 3: Chatbot Logic ---
while True:
    user_query = input("You: ").lower()

    if "exit" in user_query or "quit" in user_query:
        print("CryptoBuddy: Goodbye! 💸 Stay curious and invest wisely!")
        break

    elif "sustainable" in user_query or "eco" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"CryptoBuddy: Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!")

    elif "trending" in user_query or "rising" in user_query:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        print(f"CryptoBuddy: These coins are trending up: {', '.join(trending)} 🚀")

    elif "profitable" in user_query or "long-term" in user_query or "growth" in user_query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                print(f"CryptoBuddy: {coin} looks great for profitability—it’s trending up and has a strong market cap! 💰")
                break
        else:
            print("CryptoBuddy: Hmm… none of the coins seem ideal for long-term profit right now.")

    else:
        print("CryptoBuddy: I didn’t get that. Try asking about trending, sustainable, or profitable cryptos.")

# --- Optional: Ethics Disclaimer ---
print("\nDisclaimer: 🚨 Crypto is risky—always do your own research before investing!")

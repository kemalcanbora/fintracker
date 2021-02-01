from helper import Pool
from multiprocessing import cpu_count
from workers.twitter.app import TwitterEngine
from workers.telegram.app import TelegramStreamEngine
from workers.reddit.app import RedditEngine


telegramurls = ["https://t.me/DeCenterOrg",
                "https://t.me/wallstreetbets",
                "https://t.me/cointelegraph",
                "https://t.me/coinspot",
                "https://t.me/icoinvest",
                "https://t.me/bitcoinprivatenews",
                "https://t.me/satoshistreetbets",
                "https://t.me/SatoshiStreetBetsZH",
                "https://t.me/SatoshiStreetBetsRU"
                ]

twitter_urls = ["el33th4xor",
                "AnthonyLeeZhang",
                "AspenMartini",
                "AlamedaTrabucco",
                "aCryptoBiker",
                "Blockanalia",
                "bgarlinghouse",
                "AaronBuchwald",
                "j0eferrara",
                "hal2001",
                "ShitcoinDotCom",
                "CryptoKelso",
                "Don_wonton",
                "BerkTheBuidler",
                "timothyjcoulter",
                "elonmusk",
                "cz_binance"]

reddit_urls = ["bitcoin",
               "CryptoCurrency",
               "btc",
               "CryptoMarkets",
               "bitcoinbeginners",
               "altcoin",
               "blockchain"]




if __name__ == '__main__':
    pool = Pool(process_count=cpu_count())
    telegram_crawler = TelegramStreamEngine(telegramurls)
    twitter_crawler = pool.map(TwitterEngine().parser, twitter_urls)
    reddit_crawler = pool.map(RedditEngine.parser, reddit_urls)
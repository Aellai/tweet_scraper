import snscrape.modules.twitter as sntwitter
import pandas as pd
import openpyxl as xl

mode = sntwitter.TwitterTweetScraperMode
scraper = sntwitter.TwitterTweetScraper(tweetId=1661429589103525888, mode=mode.SCROLL)

# List for appending tweet data
replies = scraper.get_items()
reply_list = []

# Scraping data and append it to the list
for i, tweet in enumerate(replies):
    data = [
        tweet.id,
        tweet.rawContent,
        tweet.user.username,
    ]
    reply_list.append(data)
    if i > 1000:
        break

# Get number of rows in excel file (to determine where to append)
source_file = xl.load_workbook("kopia_content.xlsx", enumerate)
sheet = source_file["Sheet2"]
row_count = sheet.max_row
source_file.close()

reply_df = pd.DataFrame(reply_list, columns=['ID', 'RawContent', 'Username'])

with pd.ExcelWriter("kopia_content.xlsx", mode='a', if_sheet_exists='overlay') as writer:
    reply_df.to_excel(writer, sheet_name='Sheet2', index=False,  startrow=row_count)
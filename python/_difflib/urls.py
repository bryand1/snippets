import difflib

http_url = "http://www.harleyofdothan.com/default.asp?page=xNewInventory"
https_url = "https://www.harleyofdothan.com/default.asp?page=xNewInventory"

diff = difflib.SequenceMatcher(a=http_url, b=https_url)
print(diff.ratio())
print(diff.get_matching_blocks())

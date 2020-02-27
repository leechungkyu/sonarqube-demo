from notion.client import NotionClient
from notion.block import TodoBlock
from notion.block import PageBlock

# login
token_v2 = 'c6c629d29504bd10272...012345678901234512345' # 준비물의 token_v2
client = NotionClient(token_v2=token_v2)

# 스벅남 페이지 URL
url = "https://www.notion.so/openwiki/d8e3e99628eb4e21a258575367ee72c5"
page = client.get_block(url)

print("Page 제목은  :", page.title)

################################
# API 호출로 PageBlock 추가
################################
print(page.children.add_new(PageBlock, title='2020.01.11'))
print(page.children.add_new(PageBlock, title='2020.01.12'))
print(page.children.add_new(PageBlock, title='2020.01.13'))
print(page.children.add_new(PageBlock, title='2020.01.14'))
print(page.children.add_new(PageBlock, title='2020.01.15'))

####################################
# PageBlock에 TodoBlock 추가
####################################
for child in page.children :
    child_page = client.get_block(child.id)
    child_page.children.add_new(TodoBlock, title="09:00 아아벤티")

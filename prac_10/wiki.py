import wikipedia

page_title = input("Search for something: ")

page = wikipedia.page(page_title)
print(f"Title: {page.title}")
print(wikipedia.summary(page_title))
print(f"URL: {page.url}")
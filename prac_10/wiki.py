import wikipedia

title = input("Enter page title: ")
while title != '':
    try:
        page = wikipedia.page(title, auto_suggest=False)
        print(f"{page.title}\n{page.summary}\n{page.url}\n")
    except wikipedia.PageError:
        print(f'Page id "{title}" does not match any pages. Try another id!')
    except wikipedia.DisambiguationError as disambiguation_error:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(disambiguation_error.options)
    title = input("Enter page title: ")
print("Thank you.")


import json
from atlassian import Confluence

f = open(r"C:\Users\opusp\OneDrive\Desktop\confluence_token.json")
passWord = json.load(f)

print(f)

# confluence = Confluence(
#     url = "https://opus-fx.atlassian.net",
#     username = "opus.paulmoriaux@gmail.com",
#     password = passWord
# )


# confluence.append_page("98412", "Test for HDA Discoverability", "I'm adding this text")

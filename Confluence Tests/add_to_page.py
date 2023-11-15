import json
from atlassian import Confluence

passWord = json.load("C:\Users\opusp\OneDrive\Desktop\confluence_token.json.txt")

confluence = Confluence(
    url = "https://opus-fx.atlassian.net",
    username = "opus.paulmoriaux@gmail.com",
    password = passWord
)


confluence.append_page("98412", "Test for HDA Discoverability", "I'm adding this text")
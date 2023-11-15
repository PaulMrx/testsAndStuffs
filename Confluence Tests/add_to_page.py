from atlassian import Confluence

confluence = Confluence(
    url = "https://opus-fx.atlassian.net",
    username = "opus.paulmoriaux@gmail.com",
    password = "ATATT3xFfGF0SonOK9WIsUk7VlicVF1iDwzRgRPmNyI5mVyKEfmmZ6IpwYQ_wbVuxUW58BRv2l23Z6HwTjbcYsfLtbziNUiHOWZGNFIk2gaY9Ecjbfucecxi-aZ-as4mzj8SHg8S-m5C0uETlQJNIC_8iiZt_OrwGSrxqw0NgBKJcvVGzyYTwvc=D0AFEB8E"
)


confluence.append_page("98412", "Test for HDA Discoverability", "I'm adding this text")
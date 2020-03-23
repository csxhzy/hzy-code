from poium import Page,PageElement
class BaiduPage(Page):
    """百度page层，百度页面封装操作到元素"""
    search_input = PageElement(id_="kw")
    search_button = PageElement(id_="su")
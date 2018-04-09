c.tabs.position = 'left'
c.tabs.width = '8%'

c.qt.highdpi = True

c.url.searchengines = {
    'DEFAULT': 'https://google.com/search?q={}',
    'youtube': 'https://www.youtube.com/results?search_query={}'
}

c.completion.shrink = True

c.spellcheck.languages = ['en-US', 'et-EE']

c.input.insert_mode.auto_load = True

config.bind('<Ctrl-k>', 'tab-move -')
config.bind('<Ctrl-j>', 'tab-move +')
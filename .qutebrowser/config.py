config.load_autoconfig()

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

# with config.pattern('*://*.github.com/') as p:
#     p.content.user_stylesheets = ['github_dark.css']

c.editor.command = ['/usr/local/bin/oni', '{file}']

config.bind('sI', 'spawn --userscript /Users/deiwin/bin/instaqute {url}')